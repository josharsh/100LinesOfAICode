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

## Testing

```bash
pip install pytest anthropic
pytest
```

Tests mock the Anthropic API, so no API key is needed. They cover diff parsing, message generation, edge cases, and auto-commit flow.

**76 lines. Never write commits again.**
