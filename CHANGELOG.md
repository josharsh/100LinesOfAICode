# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-20

### 🎉 Initial Release

The first public release of 100 Lines Of AI Code!

### ✨ Added

**Tier S - Cutting Edge Tools:**
- **AI Agent** (95 lines) - Autonomous agent with tool use and self-correction
  - Execute code, read/write files, search codebases
  - Multi-step task planning
  - Error recovery and retries

- **MCP Server** (87 lines) - Model Context Protocol implementation
  - Full MCP 2024-11-05 spec compliance
  - Resource serving (files, documents)
  - Tool registration and execution
  - stdio transport

- **Code Reviewer** (99 lines) - AI-powered code review
  - Single file review
  - GitHub PR review
  - Git diff analysis
  - Security, bugs, performance, best practices

**Tier A - High Utility Tools:**
- **Mini RAG** (94 lines) - Document Q&A with embeddings
  - Index documents from files/directories
  - Semantic search with simple embeddings
  - Question answering with citations
  - Persistent knowledge base

- **Commit AI** (76 lines) - Automatic commit message generation
  - Analyzes git diffs
  - Conventional Commits format
  - Learns from commit history
  - One-line git integration

- **Voice to Code** (94 lines) - Speech to code generation
  - Voice input via microphone
  - Multi-language support (Python, JS, Java, Go, etc.)
  - Production-ready code output
  - Save to file

- **Terminal AI** (88 lines) - Natural language to shell commands
  - Safe mode with dangerous command blocking
  - Multi-OS support (macOS, Linux, Windows)
  - Command explanation and risk warnings
  - Interactive or one-shot mode

### 📚 Documentation
- Comprehensive README with quick start guide
- Individual README for each tool with examples
- CONTRIBUTING.md with detailed guidelines
- CODE_OF_CONDUCT.md for community standards
- SECURITY.md with security policy
- This CHANGELOG

### 🛠️ Infrastructure
- One-click install script (`install.sh`)
- requirements.txt with all dependencies
- .env.example for API key configuration
- .gitignore for Python best practices
- GitHub Actions CI/CD workflow
- Issue templates (bug report, feature request, new tool)
- PR template
- GitHub Sponsors configuration

### 🎨 Features
- Type hints throughout
- Error handling in all tools
- Security best practices
- Production-ready code
- Educational documentation
- Real-world examples

## [Unreleased]

### 🚀 Planned

**New Tools:**
- AI Meme Generator (multimodal)
- Smart Screenshot Analyzer (vision)
- LLM Router (cost optimization)
- AI PR Description Generator
- Minimal AI Coding Assistant

**Improvements:**
- Demo GIFs for each tool
- Video tutorials
- More usage examples
- Performance optimizations
- Additional language support

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute to this project.

## Links

- [GitHub Repository](https://github.com/josharsh/100LinesOfAICode)
- [Issue Tracker](https://github.com/josharsh/100LinesOfAICode/issues)
- [Discussions](https://github.com/josharsh/100LinesOfAICode/discussions)
