# 💬 Commit AI - Never Write Commit Messages Again

AI-powered commit message generator in **76 lines** - following Conventional Commits and your project's style.

## 🎯 What It Does

- ✅ Analyzes your git diff
- ✅ Generates perfect commit messages
- ✅ Follows Conventional Commits format
- ✅ Learns from your commit history
- ✅ One-line integration with git workflow

## 🚀 Quick Start

```bash
# Install
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY="your-key-here"

# Make changes and stage them
git add myfile.py

# Generate commit message
python commit.py

# Auto-commit with generated message
python commit.py --commit
```

## 💡 Usage

### Basic Usage

```bash
# Stage your changes
git add .

# Generate message
python commit.py
```

**Output:**
```
📝 Generated Commit Message:
==================================================
feat(api): add user authentication endpoint

- Implement JWT token generation
- Add password hashing with bcrypt
- Create login and register routes

Breaking changes: None
==================================================

💡 To commit with this message:
   git commit -m "feat(api): add user authentication endpoint"
```

### Auto-Commit

```bash
python commit.py --commit
```

### One-Liner Commit

```bash
git commit -m "$(python commit.py --silent)"
```

### Include Unstaged Changes

```bash
python commit.py --all
```

### Simple Format (Non-Conventional)

```bash
python commit.py --simple
```

## 🎮 Advanced Integration

### Git Alias

Add to `~/.gitconfig`:
```ini
[alias]
    ai = !python /path/to/commit.py
    aic = !python /path/to/commit.py --commit
```

Usage:
```bash
git add .
git ai      # Generate message
git aic     # Generate and commit
```

### Pre-Commit Hook

Create `.git/hooks/prepare-commit-msg`:
```bash
#!/bin/bash
# Auto-generate commit message if none provided
if [ -z "$2" ]; then
    python /path/to/commit.py --silent > "$1"
fi
```

```bash
chmod +x .git/hooks/prepare-commit-msg
```

Now:
```bash
git add .
git commit  # Message auto-generated!
```

### Shell Function

Add to `~/.bashrc` or `~/.zshrc`:
```bash
gaic() {
    git add "$@"
    python /path/to/commit.py --commit
}
```

Usage:
```bash
gaic myfile.py  # Stage and commit in one command
```

## 📊 Conventional Commits Format

The tool generates messages following [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style (formatting, semicolons, etc.)
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples

```bash
feat(auth): add OAuth2 login support
fix(api): resolve race condition in user creation
docs(readme): update installation instructions
refactor(database): optimize query performance
```

## 🧠 How It Works

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ Git Diff │ -> │  Claude  │ -> │ Commit   │
│          │    │ Analysis │    │ Message  │
└──────────┘    └──────────┘    └──────────┘
     ▲                                │
     │         ┌──────────────┐       │
     └─────────│ Recent Commits│<─────┘
               │  (for style) │
               └──────────────┘
```

1. Reads git diff (staged or all changes)
2. Gets recent commit messages for style learning
3. Sends to Claude with format requirements
4. Claude generates commit message matching your style
5. Returns formatted message

## 🎯 Real-World Examples

### Example 1: Feature Addition

**Changes:**
```python
+ def send_email(to, subject, body):
+     smtp = smtplib.SMTP('smtp.gmail.com', 587)
+     smtp.sendmail('from@example.com', to, f"Subject: {subject}\n\n{body}")
```

**Generated:**
```
feat(email): add email sending functionality

- Implement SMTP email sending
- Support custom subject and body
- Use Gmail SMTP server
```

### Example 2: Bug Fix

**Changes:**
```python
- if user_id == None:
+ if user_id is None:
```

**Generated:**
```
fix(auth): use 'is None' instead of '== None'

Follow Python best practices for None comparison
```

### Example 3: Refactoring

**Changes:**
```python
- result = []
- for item in items:
-     if item > 0:
-         result.append(item)
+ result = [item for item in items if item > 0]
```

**Generated:**
```
refactor(utils): convert filter loop to list comprehension

Improve code readability and performance
```

## 🔧 Configuration

### Customize the Prompt

Edit the `generate_commit_message()` function to change style:

```python
prompt = f"""Generate a commit message...

Requirements:
1. Maximum 72 characters per line
2. Use imperative mood ("add" not "added")
3. Include ticket number from branch name
4. Add emojis for visual categorization
...
```

### Change Model

```python
# Use faster/cheaper model
response = self.client.messages.create(
    model="claude-3-haiku-20240307",  # Faster
    max_tokens=500,
    messages=[...]
)
```

## 📈 Benefits

### Time Savings
- **Before**: 2-5 minutes per commit
- **After**: 5 seconds
- **Saved**: ~95% time on commit messages

### Consistency
- All commits follow same format
- Professional message quality
- Easier to navigate git history

### Best Practices
- Forces you to review changes
- Encourages atomic commits
- Better documentation

## 🎓 Tips & Tricks

### 1. Review Before Committing
```bash
python commit.py  # Review message
git commit -m "$(python commit.py --silent)"  # Commit if good
```

### 2. Edit If Needed
```bash
python commit.py > /tmp/msg.txt
vim /tmp/msg.txt  # Edit
git commit -F /tmp/msg.txt
```

### 3. Learn Your Style
The AI learns from your recent commits. Better commit history = better suggestions.

### 4. Break Up Large Changes
```bash
git add -p  # Stage parts of files
python commit.py --commit  # Commit each logical change
```

## 🐛 Troubleshooting

**"No changes to commit"**
- Stage changes first: `git add <files>`

**"Git not found"**
- Install git and ensure it's in PATH

**"Poor commit messages"**
- Check your diff isn't too large (>4000 chars)
- Improve your recent commit history
- Use `--simple` for non-conventional format

## 📊 Comparison

| Method | Time | Quality | Consistency |
|--------|------|---------|-------------|
| Manual | 2-5 min | Varies | Low |
| Commit AI | 5 sec | High | High |
| Git templates | 1 min | Medium | Medium |

## 🌟 Why This Matters

### Better Git History
```bash
# Before
git log --oneline
a1b2c3d stuff
e4f5g6h fixes
h7i8j9k updates

# After
git log --oneline
a1b2c3d feat(auth): add password reset functionality
e4f5g6h fix(api): resolve race condition in user creation
h7i8j9k docs(readme): update API documentation
```

### Easier Navigation
```bash
git log --grep="feat"  # Find all features
git log --grep="fix"   # Find all bug fixes
```

### Better Release Notes
Use commit messages to auto-generate changelogs.

## 📚 Further Reading

- [Conventional Commits](https://www.conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Semantic Versioning](https://semver.org/)

## 🤝 Contributing

Ideas:
- [ ] Co-author detection
- [ ] Breaking change highlighting
- [ ] Multi-language support
- [ ] Custom commit templates
- [ ] Integration with issue trackers

---

**Powered by Claude 3.5 Sonnet | 76 lines | Never write commits again**
