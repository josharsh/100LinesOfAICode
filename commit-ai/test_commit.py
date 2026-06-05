"""Unit tests for commit-ai message generator."""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCommitAI:
    """Tests for CommitAI class."""

    @patch('subprocess.run')
    def test_get_diff_staged(self, mock_run):
        """Test getting staged diff."""
        mock_run.return_value = MagicMock(stdout="+ new line\n- old line")
        
        from commit import CommitAI
        ai = CommitAI()
        diff = ai.get_diff(staged_only=True)
        
        assert "+ new line\n- old line" == diff
        mock_run.assert_called()

    @patch('subprocess.run')
    def test_get_diff_all(self, mock_run):
        """Test getting all diff."""
        mock_run.return_value = MagicMock(stdout="+ added")
        
        from commit import CommitAI
        ai = CommitAI()
        diff = ai.get_diff(staged_only=False)
        
        assert "+ added" == diff

    @patch('subprocess.run')
    def test_get_branch(self, mock_run):
        """Test getting current branch."""
        mock_run.return_value = MagicMock(stdout="feature-branch")
        
        from commit import CommitAI
        ai = CommitAI()
        branch = ai.get_branch()
        
        assert "feature-branch" == branch

    @patch('subprocess.run')
    def test_get_recent_commits(self, mock_run):
        """Test getting recent commits."""
        mock_run.return_value = MagicMock(stdout="feat: add new\nfix: bug")
        
        from commit import CommitAI
        ai = CommitAI()
        recent = ai.get_recent_commits(count=5)
        
        assert "feat: add new\nfix: bug" == recent

    def test_generate_commit_message_conventional(self):
        """Test conventional commit format generation."""
        from commit import CommitAI
        
        # Mock the API response
        with patch.object(CommitAI, '__init__', lambda x: None):
            ai = CommitAI()
            ai.client = MagicMock()
            
            mock_response = MagicMock()
            mock_response.content = [MagicMock(text="feat(api): add new endpoint")]
            ai.client.messages.create.return_value = mock_response
            
            diff = "+ def new_func(): pass"
            branch = "main"
            recent = "feat: init"
            
            result = ai.generate_commit_message(diff, conventional=True, branch=branch, recent_style=recent)
            
            assert result == "feat(api): add new endpoint"

    def test_generate_commit_message_simple(self):
        """Test simple commit format."""
        from commit import CommitAI
        
        with patch.object(CommitAI, '__init__', lambda x: None):
            ai = CommitAI()
            ai.client = MagicMock()
            
            mock_response = MagicMock()
            mock_response.content = [MagicMock(text="Add new function")]
            ai.client.messages.create.return_value = mock_response
            
            diff = "+ def new_func(): pass"
            
            result = ai.generate_commit_message(diff, conventional=False)
            
            assert result == "Add new function"

    def test_empty_diff(self):
        """Test handling empty diff."""
        from commit import CommitAI
        
        with patch.object(CommitAI, '__init__', lambda x: None):
            ai = CommitAI()
            
            with patch.object(ai, 'get_diff', return_value=""):
                result = ai.generate(staged_only=True)
                
                assert "No changes to commit" in result

    @patch('subprocess.run')
    def test_auto_commit(self, mock_run):
        """Test auto commit functionality."""
        from commit import CommitAI
        
        with patch.object(CommitAI, '__init__', lambda x: None):
            ai = CommitAI()
            
            # Mock all the methods
            with patch.object(ai, 'get_diff', return_value="+ new"), \
                 patch.object(ai, 'get_branch', return_value="main"), \
                 patch.object(ai, 'get_recent_commits', return_value="init"), \
                 patch.object(ai, 'generate_commit_message', return_value="feat: add"):
                
                result = ai.generate(staged_only=True, auto_commit=True)
                
                assert "Committed" in result
                mock_run.assert_any_call(["git", "commit", "-m", "feat: add"], check=True)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
