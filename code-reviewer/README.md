# 👁️ AI Code Reviewer

**Expert-level reviews instantly** - Finds bugs, security issues, and performance problems.

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

python reviewer.py --file mycode.py
python reviewer.py --pr 123
python reviewer.py --diff
```

## Output

```
📝 Review of app.py

🔴 CRITICAL - SQL Injection Risk (line 23)
Current:
  cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
Fix:
  cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))

🟡 WARNING - Missing Input Validation (line 15)
Add validation before processing user input.

💡 Suggestions:
- Add docstrings to public functions
- Extract magic numbers to constants
```

## CI/CD Integration

```yaml
# .github/workflows/review.yml
name: AI Code Review
on: [pull_request]
jobs:
  review:
    steps:
      - run: |
          pip install anthropic
          python reviewer.py --diff > review.md
          gh pr comment --body-file review.md
```

**99 lines. Expert-level reviews.**
