# 💬 PR Writer

**Stop writing essays** - Professional PR descriptions in 10 seconds.

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

# Make your changes and commit
git add . && git commit -m "your changes"

# Generate PR description
python writer.py
```

## Usage Demo

```bash
$ git add . && git commit -m "added auth"
$ python writer.py

📝 Analyzing your changes...

## 🎯 What This Does
Implements JWT-based authentication with token refresh

## 🤔 Why We Need It  
Users were logged out randomly (40+ tickets/week)

## ⚙️ How It Works
1. User logs in → server generates JWT
2. Token stored in httpOnly cookie
3. Middleware validates each request

## ✅ Testing
- [x] Unit tests (12 new tests)
- [x] Integration tests
- [x] Manual staging testing

## 🚀 Deployment Notes
Requires REDIS_URL environment variable

✨ Copied to clipboard! Ready to paste into GitHub/GitLab!
```

## Output

```
## 🎯 What This Does
Implements JWT-based authentication with token refresh

## 🤔 Why We Need It
Users were logged out randomly (40+ tickets/week)

## ⚙️ How It Works
1. User logs in → server generates JWT
2. Token stored in httpOnly cookie
3. Middleware validates each request

## ✅ Testing
- [x] Unit tests (12 new tests)
- [x] Integration tests
- [x] Manual staging testing

## 🚀 Deployment Notes
Requires REDIS_URL environment variable
```

**68 lines. Professional PRs every time.**
