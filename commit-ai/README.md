# 💬 Commit AI

**Never write commit messages again** - AI analyzes diffs and generates perfect messages.

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

git add myfile.py
python commit.py                 # Generate message
python commit.py --commit        # Auto-commit
```

## Output

```
📝 Generated Commit Message:
feat(api): add user authentication endpoint

- Implement JWT token generation
- Add password hashing with bcrypt
- Create login and register routes
```

## Git Alias

Add to `~/.gitconfig`:
```ini
[alias]
    ai = !python /path/to/commit.py
    aic = !python /path/to/commit.py --commit
```

**76 lines. Never write commits again.**

## 🧪 Testing

This module includes comprehensive test coverage using pytest.

### Running Tests

```bash
cd commit-ai
pip install pytest
pytest test_commit.py -v
```

### Test Coverage

The test suite covers:
- ✅ Git diff parsing (staged/unstaged, empty diffs)
- ✅ Branch detection
- ✅ Recent commit history retrieval
- ✅ AI commit message generation (with mocked API)
- ✅ Conventional commit format validation
- ✅ Edge cases (special characters, unicode, large diffs)
- ✅ Auto-commit functionality

### Writing New Tests

When adding new features, please add corresponding tests in `test_commit.py`.
Follow the existing test patterns and ensure all tests pass before submitting a PR.
