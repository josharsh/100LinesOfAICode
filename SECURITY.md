# Security Policy

## 🔒 Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < 1.0   | :x:                |

## 🐛 Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please:

### 📧 Contact Us

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead:
1. Email: security@example.com (or open a private security advisory)
2. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### ⏱️ Response Time

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: 1-3 days
  - High: 1-2 weeks
  - Medium: 2-4 weeks
  - Low: Best effort

## 🛡️ Security Best Practices

When using these tools:

### API Keys
- ✅ **DO**: Store API keys in `.env` file (not committed to git)
- ✅ **DO**: Use environment variables
- ❌ **DON'T**: Hardcode API keys in code
- ❌ **DON'T**: Commit `.env` files

### Code Execution
- ⚠️ **AI Agent**: Executes Python code - review generated code before running
- ⚠️ **Terminal AI**: Executes shell commands - always confirm before running
- ⚠️ **Voice to Code**: Generates code - review before using in production

### Safe Defaults
- Terminal AI has **safe mode enabled** by default
- Code execution has **timeouts** (10-30 seconds)
- File operations are **relative to current directory**

## 🔐 Known Security Considerations

### AI Agent (`ai-agent/agent.py`)
- Executes arbitrary Python code
- Has file system access
- **Mitigation**: 10-second timeout, sandboxed execution

### Terminal AI (`terminal-ai/terminal.py`)
- Generates shell commands
- Can execute system commands
- **Mitigation**: Safe mode blocks dangerous patterns, confirmation required

### Code Reviewer (`code-reviewer/reviewer.py`)
- Reads source code
- **Mitigation**: Read-only, no modifications without user action

### Voice to Code (`voice-to-code/voice.py`)
- Sends audio to Google Speech API
- **Mitigation**: No audio is stored, processed in real-time

## 🚨 Security Features

All tools include:
- ✅ Input validation
- ✅ Error handling
- ✅ Timeout mechanisms
- ✅ No credential storage
- ✅ Minimal permissions required

## 📖 Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Anthropic Security](https://www.anthropic.com/security)

## 🤝 Responsible Disclosure

We appreciate responsible disclosure of security vulnerabilities. Contributors who report valid security issues will be:
- Credited in the CHANGELOG (if desired)
- Listed in our security hall of fame
- Sent a thank you note

## 📜 Security Updates

Security updates are announced via:
- GitHub Security Advisories
- Release notes
- README updates

## ✅ Audit Log

| Date | Issue | Severity | Status |
|------|-------|----------|--------|
| TBD  | -     | -        | -      |

---

**Last Updated**: 2025-01-20
**Next Review**: 2025-04-20
