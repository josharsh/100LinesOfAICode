import pytest
from unittest.mock import patch, MagicMock
from commit import CommitAI


@pytest.fixture
def ai():
    with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test-key"}):
        return CommitAI()


class TestGetDiff:
    def test_returns_stripped_stdout(self, ai):
        with patch("commit.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "  diff content\n  "
            result = ai.get_diff(staged_only=True)
            assert result == "diff content"
            mock_run.assert_called_once_with(
                ["git", "diff", "--cached"], capture_output=True, text=True
            )

    def test_uses_staged_diff_by_default(self, ai):
        with patch("commit.subprocess.run") as mock_run:
            mock_run.return_value.stdout = ""
            ai.get_diff()
            mock_run.assert_called_once_with(
                ["git", "diff", "--cached"], capture_output=True, text=True
            )

    def test_includes_unstaged_when_requested(self, ai):
        with patch("commit.subprocess.run") as mock_run:
            mock_run.return_value.stdout = ""
            ai.get_diff(staged_only=False)
            mock_run.assert_called_once_with(
                ["git", "diff", "HEAD"], capture_output=True, text=True
            )

    def test_returns_empty_string_on_no_changes(self, ai):
        with patch("commit.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "  "
            assert ai.get_diff() == ""


class TestGetBranch:
    def test_returns_current_branch(self, ai):
        with patch("commit.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "feature-branch\n"
            assert ai.get_branch() == "feature-branch"

    def test_strips_whitespace(self, ai):
        with patch("commit.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "  main  \n"
            assert ai.get_branch() == "  main  "


class TestGetRecentCommits:
    def test_returns_recent_commits(self, ai):
        with patch("commit.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "feat: add login\nfix: fix crash\ndocs: update readme"
            result = ai.get_recent_commits(3)
            assert "feat: add login" in result
            mock_run.assert_called_once_with(
                ["git", "log", "-3", "--pretty=format:%s"], capture_output=True, text=True
            )


class TestGenerateCommitMessage:
    def test_mocks_anthropic_call(self, ai):
        with patch.object(ai.client.messages, "create") as mock_create:
            mock_create.return_value.content = [
                MagicMock(text="feat(api): add user authentication")
            ]
            result = ai.generate_commit_message(
                diff="+def login(): pass",
                conventional=True,
                branch="feature/login",
                recent_style="feat: stuff",
            )
            assert result == "feat(api): add user authentication"
            assert mock_create.called

    def test_truncates_large_diff_to_4000_chars(self, ai):
        with patch.object(ai.client.messages, "create") as mock_create:
            mock_create.return_value.content = [MagicMock(text="fix: big change")]
            large_diff = "a" * 5000
            ai.generate_commit_message(diff=large_diff, conventional=True)
            prompt = mock_create.call_args[1]["messages"][0]["content"]
            assert prompt.count("a") == 4000

    def test_adds_conventional_commit_requirement(self, ai):
        with patch.object(ai.client.messages, "create") as mock_create:
            mock_create.return_value.content = [MagicMock(text="fix: stuff")]
            ai.generate_commit_message(diff="+x", conventional=True)
            prompt = mock_create.call_args[1]["messages"][0]["content"]
            assert "Conventional Commits" in prompt

    def test_omits_conventional_when_not_requested(self, ai):
        with patch.object(ai.client.messages, "create") as mock_create:
            mock_create.return_value.content = [MagicMock(text="some change")]
            ai.generate_commit_message(diff="+x", conventional=False)
            prompt = mock_create.call_args[1]["messages"][0]["content"]
            assert "Conventional Commits" not in prompt


class TestGenerate:
    def test_returns_error_on_empty_diff(self, ai):
        with patch.object(ai, "get_diff", return_value=""):
            result = ai.generate()
            assert "No changes" in result

    def test_generates_message_with_diff(self, ai):
        with (
            patch.object(ai, "get_diff", return_value="+new code"),
            patch.object(ai, "get_branch", return_value="main"),
            patch.object(ai, "get_recent_commits", return_value="fix: prior"),
            patch.object(ai, "generate_commit_message", return_value="feat: add feature"),
        ):
            result = ai.generate()
            assert result == "feat: add feature"

    def test_auto_commit_runs_git_commit(self, ai):
        with (
            patch.object(ai, "get_diff", return_value="+new code"),
            patch.object(ai, "get_branch", return_value="main"),
            patch.object(ai, "get_recent_commits", return_value="fix: prior"),
            patch.object(ai, "generate_commit_message", return_value="feat: add feature"),
            patch("commit.subprocess.run") as mock_run,
        ):
            result = ai.generate(auto_commit=True)
            assert "Committed" in result
            mock_run.assert_called_once_with(
                ["git", "commit", "-m", "feat: add feature"], check=True
            )
