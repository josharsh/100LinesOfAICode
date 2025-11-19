# 🤖 100 Lines Of AI Code

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **Powerful AI tools in less than 100 lines each.** No bloat, just results.

Inspired by the #100LinesOfCode movement, this collection proves you don't need thousands of lines to build production-ready AI tools. Each project is self-contained, well-documented, and ready to use.

## 🎯 Why This Matters

- **Learn Fast**: See exactly how AI tools work without framework complexity
- **Production Ready**: Despite being minimal, these tools solve real problems
- **No Dependencies Hell**: Minimal, carefully chosen dependencies
- **Educational**: Perfect for understanding AI fundamentals

## 🚀 Projects

### ⭐ Tier S - Cutting Edge (2025 Trends)

| Project | Description | Lines | Status |
|---------|-------------|-------|--------|
| [🤖 AI Agent](./ai-agent/) | Autonomous agent that executes tasks, self-corrects | 95 | ✅ |
| [🔌 MCP Server](./mcp-server/) | Model Context Protocol server (brand new Anthropic protocol) | 87 | ✅ |
| [👁️ Code Reviewer](./code-reviewer/) | AI-powered code review with GitHub integration | 99 | ✅ |

### 💎 Tier A - High Utility

| Project | Description | Lines | Status |
|---------|-------------|-------|--------|
| [📚 Mini RAG](./mini-rag/) | Chat with your documents using embeddings | 94 | ✅ |
| [💬 Commit AI](./commit-ai/) | Generate perfect commit messages from git diffs | 76 | ✅ |
| [🎤 Voice to Code](./voice-to-code/) | Speak requirements, get working code | 94 | ✅ |
| [⚡ Terminal AI](./terminal-ai/) | Natural language → safe shell commands | 88 | ✅ |

## 📦 Quick Start

### Prerequisites
```bash
# Python 3.8 or higher
python --version

# Install uv (fast Python package manager) - optional but recommended
pip install uv
```

### Installation

```bash
# Clone the repository
git clone https://github.com/josharsh/100LinesOfAICode.git
cd 100LinesOfAICode

# Install dependencies (choose one method)

# Method 1: Using uv (faster)
uv pip install -r requirements.txt

# Method 2: Using pip
pip install -r requirements.txt
```

### Environment Setup

All projects use AI APIs. Create a `.env` file in the root:

```bash
# Required for most projects
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here

# Optional: for specific projects
GITHUB_TOKEN=your_github_token_here
```

Get your API keys:
- Anthropic (Claude): https://console.anthropic.com/
- OpenAI (GPT): https://platform.openai.com/api-keys
- GitHub: https://github.com/settings/tokens

## 🎮 Usage Examples

### AI Agent - Autonomous Task Execution
```bash
cd ai-agent
python agent.py "find all TODO comments in this codebase and create a summary"
```

### Code Reviewer - Instant Code Reviews
```bash
cd code-reviewer
python reviewer.py --pr 123  # Review PR #123
python reviewer.py --file mycode.py  # Review a file
```

### Commit AI - Never Write Commit Messages Again
```bash
cd commit-ai
python commit.py  # Analyzes staged changes and generates message
git commit -m "$(python commit.py --silent)"  # One-liner commit
```

### Voice to Code - Speak Your Code
```bash
cd voice-to-code
python voice.py  # Start listening, speak your requirements
```

## 🏗️ Project Structure

```
100LinesOfAICode/
├── ai-agent/           # Autonomous AI agent
│   ├── agent.py        # Main agent (95 lines)
│   ├── README.md       # Detailed docs
│   └── examples/       # Usage examples
├── mcp-server/         # Model Context Protocol
├── code-reviewer/      # AI code reviewer
├── mini-rag/          # RAG system
├── commit-ai/         # Commit message generator
├── voice-to-code/     # Voice to code
├── terminal-ai/       # Terminal assistant
├── requirements.txt   # All dependencies
└── README.md          # This file
```

## 🎯 Design Philosophy

### Why 100 Lines?

1. **Constraint Breeds Creativity**: Forces us to focus on what matters
2. **Easy to Understand**: You can read the entire codebase in minutes
3. **Easy to Modify**: Change behavior without framework knowledge
4. **Educational Value**: See exactly how AI tools work

### Code Quality Standards

Despite the line limit, we maintain:
- ✅ Type hints for clarity
- ✅ Error handling for robustness
- ✅ Docstrings for understanding
- ✅ Security best practices
- ✅ Production-ready code

## 🤝 Contributing

We love contributions! Here's how:

1. **Add a New Tool**: Must be ≤100 lines, solve a real problem
2. **Improve Existing**: Optimize, fix bugs, add features
3. **Documentation**: Better READMEs, more examples, GIFs

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📈 What's Next?

Upcoming additions based on 2025 AI trends:
- [ ] AI Meme Generator (multimodal)
- [ ] Smart Screenshot Analyzer (vision)
- [ ] LLM Router (cost optimization)
- [ ] AI PR Description Generator
- [ ] Minimal AI Coding Assistant

Vote for what you want next by opening an issue!

## 🌟 Star History

If you find this useful, please star the repo! ⭐

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

- Inspired by the #100LinesOfCode movement
- Built for the AI developer community
- Powered by Claude, GPT-4, and open-source AI models

## 📞 Contact

- **Issues**: [GitHub Issues](https://github.com/josharsh/100LinesOfAICode/issues)
- **Discussions**: [GitHub Discussions](https://github.com/josharsh/100LinesOfAICode/discussions)
- **Twitter**: Share your creations with #100LinesOfAICode

---

**Made with ❤️ by developers who believe less is more.**
