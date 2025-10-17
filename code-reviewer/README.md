# 👁️ AI Code Reviewer

Automated code review powered by Claude - **99 lines** of pure insight.

## 🎯 What It Does

Get instant, expert-level code reviews:
- 🐛 **Bug Detection**: Logic errors, edge cases, crashes
- 🔒 **Security Analysis**: Vulnerabilities, injection risks
- ⚡ **Performance**: Inefficiencies, optimizations
- 📚 **Best Practices**: Style, patterns, maintainability
- 💡 **Actionable Suggestions**: Specific improvements with examples

## 🚀 Quick Start

```bash
# Install dependencies
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY="your-key-here"

# Review a file
python reviewer.py --file mycode.py

# Review a PR
python reviewer.py --pr 123

# Review your changes
python reviewer.py --diff
```

## 💡 Usage Examples

### Review Single File
```bash
python reviewer.py --file app.py
```

**Output:**
```
📝 Review of app.py
============================================================
✅ What's Good:
- Clean function structure
- Good error handling
- Type hints used

⚠️ Issues Found:

🔴 CRITICAL - SQL Injection Risk (line 23)
Current:
  cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
Fix:
  cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))

🟡 WARNING - Missing Input Validation (line 15)
Add validation before processing user input.

💡 Suggestions:
- Add docstrings to public functions
- Consider using connection pooling for DB
- Extract magic numbers to constants
```

### Review GitHub PR
```bash
# Review specific PR
python reviewer.py --pr 456

# Review current branch
python reviewer.py --diff
```

### Review Entire Directory
```bash
python reviewer.py --dir ./src --output review_report.md
```

### Integrate with Git Hooks
```bash
# Add to .git/hooks/pre-commit
python /path/to/reviewer.py --diff
```

## 🎮 Advanced Usage

### Custom Review Criteria

Edit the `REVIEW_PROMPT` in reviewer.py to focus on specific aspects:

```python
REVIEW_PROMPT = """Review focusing on:
1. TypeScript best practices
2. React hooks usage
3. Performance optimizations
...
"""
```

### Batch Review

```python
from reviewer import CodeReviewer

reviewer = CodeReviewer()
files = ["file1.py", "file2.py", "file3.py"]
for f in files:
    result = reviewer.review_file(f)
    print(result['review'])
```

### CI/CD Integration

```yaml
# .github/workflows/review.yml
name: AI Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: AI Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          pip install anthropic
          python reviewer.py --diff > review.md
          gh pr comment --body-file review.md
```

## 📊 Review Categories

### 1. Bugs & Errors
- Off-by-one errors
- Null pointer issues
- Race conditions
- Unhandled exceptions
- Type mismatches

### 2. Security
- SQL injection
- XSS vulnerabilities
- Path traversal
- Insecure crypto
- Exposed secrets

### 3. Performance
- O(n²) algorithms
- Memory leaks
- Unnecessary loops
- Missing caching
- DB N+1 queries

### 4. Best Practices
- Code duplication
- Magic numbers
- Poor naming
- Missing tests
- Lack of documentation

### 5. Maintainability
- High complexity
- Long functions
- Deep nesting
- Tight coupling
- Missing error handling

## 🎯 Real-World Examples

### Example 1: Security Issue Found

**Before:**
```python
def login(username, password):
    query = f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"
    return db.execute(query)
```

**AI Review:**
```
🔴 CRITICAL: SQL Injection vulnerability
An attacker can inject SQL: username = "admin'--"

Fix:
def login(username, password):
    query = "SELECT * FROM users WHERE user=? AND pass=?"
    return db.execute(query, (username, hash_password(password)))
```

### Example 2: Performance Optimization

**Before:**
```python
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**AI Review:**
```
🟡 WARNING: O(n²) complexity
For large lists, this is slow.

Fix (O(n)):
def find_duplicates(items):
    seen, duplicates = set(), set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
```

## 🔧 Configuration

### Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-...

# Optional
GITHUB_TOKEN=ghp_...  # For private repos
```

### File Extensions

By default reviews: `.py`, `.js`, `.ts`, `.go`, `.java`

Customize:
```python
reviewer.review_directory("./src", extensions=[".rs", ".cpp", ".c"])
```

## 📈 Performance & Cost

- **Speed**: ~5-10 seconds per file
- **Cost**: ~$0.01-0.03 per review (Claude Sonnet)
- **Accuracy**: Expert-level feedback
- **Languages**: Supports 20+ programming languages

## 🎓 How It Works

```
┌──────────┐    ┌─────────────┐    ┌──────────┐
│   Code   │ -> │   Claude    │ -> │  Review  │
│  (File)  │    │ (3.5 Sonnet)│    │ (Report) │
└──────────┘    └─────────────┘    └──────────┘
                      ▲
                      │
                 Review Prompt
              (Security, Bugs, etc.)
```

The reviewer:
1. Reads code file or git diff
2. Sends to Claude with expert review prompt
3. Claude analyzes against best practices
4. Returns structured feedback
5. Formats output for readability

## 🚀 Integration Ideas

### 1. Pre-commit Hook
```bash
#!/bin/bash
python reviewer.py --diff || echo "Review complete"
```

### 2. PR Bot
```python
# Auto-comment on PRs
import os
from reviewer import CodeReviewer

pr_number = os.getenv("PR_NUMBER")
review = CodeReviewer().review_pr(int(pr_number))
# Post to GitHub via API
```

### 3. IDE Plugin
```python
# VSCode extension
@command
def review_current_file():
    file = vscode.window.activeTextEditor.document.fileName
    review = CodeReviewer().review_file(file)
    vscode.window.showInformationMessage(review)
```

### 4. Slack Bot
```python
@slack_app.command("/review")
def review_command(ack, command):
    file_url = command['text']
    review = CodeReviewer().review_code(fetch_file(file_url))
    ack(review)
```

## 🐛 Troubleshooting

**"API key not found"**
```bash
export ANTHROPIC_API_KEY="your-key"
```

**"gh: command not found" (for PR reviews)**
```bash
# Install GitHub CLI
brew install gh  # macOS
sudo apt install gh  # Ubuntu
```

**Reviews are too slow**
- Use `--file` for single files instead of `--dir`
- Claude Haiku is faster (change model in code)
- Run in parallel for multiple files

**Review is too generic**
- Customize REVIEW_PROMPT for your use case
- Add specific coding standards
- Include project context

## 🌟 Best Practices

1. **Review Before Commit**: Catch issues early
2. **Focus Reviews**: Use for changed files only
3. **Customize Prompts**: Tailor to your tech stack
4. **Automate**: Integrate into CI/CD
5. **Iterate**: Apply suggestions, re-review

## 📊 Comparison

| Tool | Speed | Depth | Languages | Cost |
|------|-------|-------|-----------|------|
| This | Fast | Expert | All | Low |
| SonarQube | Medium | Good | Many | Free |
| CodeClimate | Slow | Good | Limited | $$ |
| Human Review | Slow | Varies | All | $$$ |

**Advantage**: Expert-level insights without setup or config.

## 📚 Further Reading

- [Claude Code Analysis Guide](https://docs.anthropic.com/claude/docs/code-analysis)
- [Secure Code Review Practices](https://owasp.org/www-project-code-review-guide/)
- [Google Code Review Guidelines](https://google.github.io/eng-practices/review/)

## 🤝 Contributing

Improvements welcome:
- [ ] Support for more languages
- [ ] Custom rule sets
- [ ] Severity scoring
- [ ] Auto-fix suggestions
- [ ] Team review workflows

---

**Powered by Claude 3.5 Sonnet | 99 lines | Expert-level reviews**
