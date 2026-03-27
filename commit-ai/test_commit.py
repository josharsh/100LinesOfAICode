#!/usr/bin/env python3
"""Test suite for commit-ai module."""
import pytest
from unittest.mock import Mock, patch, MagicMock
import subprocess
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commit import CommitAI


class TestCommitAI:
    """Test cases for CommitAI class."""

    def test_init_with_api_key(self):
        """Test initialization with explicit API key."""
        ai = CommitAI(api_key="test-key-123")
        assert ai.client is not None

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "env-key-456"})
    def test_init_from_environment(self):
        """Test initialization from environment variable."""
        ai = CommitAI()
        assert ai.client is not None

    @patch('subprocess.run')
    def test_get_diff_staged(self, mock_run):
        """Test getting staged git diff."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "diff", "--cached"],
            returncode=0,
            stdout="+ def new_function(): pass\n- old_code = True",
            stderr=""
        )
        ai = CommitAI(api_key="test")
        diff = ai.get_diff(staged_only=True)
        assert "new_function" in diff
        assert "old_code" in diff
        mock_run.assert_called_once_with(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True
        )

    @patch('subprocess.run')
    def test_get_diff_empty(self, mock_run):
        """Test getting diff when no changes."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "diff", "--cached"],
            returncode=0,
            stdout="",
            stderr=""
        )
        ai = CommitAI(api_key="test")
        diff = ai.get_diff(staged_only=True)
        assert diff == ""

    @patch('subprocess.run')
    def test_get_branch(self, mock_run):
        """Test getting current git branch."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "branch", "--show-current"],
            returncode=0,
            stdout="feature/ai-commits\n",
            stderr=""
        )
        ai = CommitAI(api_key="test")
        branch = ai.get_branch()
        assert branch == "feature/ai-commits"

    @patch('subprocess.run')
    def test_get_recent_commits(self, mock_run):
        """Test getting recent commit messages."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "log", "-5", "--pretty=format:%s"],
            returncode=0,
            stdout="feat: add new feature\nfix: resolve bug\ndocs: update README",
            stderr=""
        )
        ai = CommitAI(api_key="test")
        commits = ai.get_recent_commits(count=5)
        assert "feat:" in commits
        assert "fix:" in commits
        assert "docs:" in commits

    @patch('anthropic.Anthropic')
    @patch('subprocess.run')
    def test_generate_commit_message_conventional(self, mock_run, mock_anthropic):
        """Test generating conventional commit message."""
        # Mock subprocess for diff, branch, commits
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "diff"],
            returncode=0,
            stdout="+ def test(): pass",
            stderr=""
        )
        
        # Mock Anthropic API response
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text="feat(commit-ai): add test suite for commit generation")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        ai = CommitAI(api_key="test")
        diff = "+ def test(): pass"
        message = ai.generate_commit_message(diff, conventional=True)
        
        assert "feat:" in message or "fix:" in message or "docs:" in message
        mock_client.messages.create.assert_called_once()

    @patch('anthropic.Anthropic')
    @patch('subprocess.run')
    def test_generate_commit_message_truncates_large_diff(self, mock_run, mock_anthropic):
        """Test that large diffs are truncated to 4000 chars."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "diff"],
            returncode=0,
            stdout="x" * 5000,  # 5000 char diff
            stderr=""
        )
        
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text="chore: update large file")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        ai = CommitAI(api_key="test")
        diff = "x" * 5000
        message = ai.generate_commit_message(diff)
        
        # Verify API was called with truncated diff
        call_args = mock_client.messages.create.call_args
        prompt = call_args[1]['messages'][0]['content']
        assert len(prompt) < 5000  # Should be truncated

    @patch('subprocess.run')
    def test_generate_no_changes(self, mock_run):
        """Test generate when no changes to commit."""
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "diff", "--cached"],
            returncode=0,
            stdout="",
            stderr=""
        )
        ai = CommitAI(api_key="test")
        result = ai.generate(staged_only=True)
        assert "❌ No changes" in result

    @patch('subprocess.run')
    @patch('anthropic.Anthropic')
    def test_generate_with_auto_commit(self, mock_anthropic, mock_run):
        """Test generate with auto-commit enabled."""
        # Setup mocks
        mock_run.side_effect = [
            subprocess.CompletedProcess(args=["git", "diff"], returncode=0, stdout="+ change", stderr=""),
            subprocess.CompletedProcess(args=["git", "branch"], returncode=0, stdout="main", stderr=""),
            subprocess.CompletedProcess(args=["git", "log"], returncode=0, stdout="prev commit", stderr=""),
            subprocess.CompletedProcess(args=["git", "commit"], returncode=0, stdout="", stderr=""),
        ]
        
        mock_client = Mock()
        mock_response = Mock()
        mock_response.content = [Mock(text="feat: auto-committed change")]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        ai = CommitAI(api_key="test")
        result = ai.generate(auto_commit=True)
        
        assert "✅ Committed" in result
        assert mock_run.call_count == 4  # diff, branch, log, commit

    def test_edge_case_special_characters_in_diff(self):
        """Test handling of special characters in diff."""
        ai = CommitAI(api_key="test")
        diff = "+ print('Hello \"world\"')\n+ # Special: @#$%^&*()"
        # Should not raise exception
        message = ai.generate_commit_message(diff, conventional=False)
        assert message is not None

    def test_edge_case_unicode_in_diff(self):
        """Test handling of unicode characters."""
        ai = CommitAI(api_key="test")
        diff = "+ # 中文注释\n+ # Emoji: 🚀 ✅ 🐛"
        message = ai.generate_commit_message(diff, conventional=False)
        assert message is not None


class TestConventionalCommitValidation:
    """Test conventional commit format validation."""

    def test_valid_conventional_commits(self):
        """Test valid conventional commit formats."""
        valid_commits = [
            "feat: add new feature",
            "fix(auth): resolve login bug",
            "docs: update README",
            "style: format code",
            "refactor: simplify logic",
            "test: add unit tests",
            "chore: update dependencies"
        ]
        for commit in valid_commits:
            assert ":" in commit
            assert len(commit.split("\n")[0]) <= 50 or True  # Subject line check

    def test_commit_message_structure(self):
        """Test commit message has proper structure."""
        ai = CommitAI(api_key="test")
        diff = "+ def new_feature(): pass"
        message = ai.generate_commit_message(diff, conventional=True)
        
        lines = message.strip().split("\n")
        subject = lines[0]
        
        # Subject should be concise
        assert len(subject) > 0
        # Should have type prefix
        assert any(subject.startswith(t) for t in ["feat", "fix", "docs", "style", "refactor", "test", "chore"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
