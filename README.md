# 🤖 100 Lines Of AI Code

<p align="center">
  <a href="https://github.com/josharsh/100LinesOfAICode/stargazers">
    <img src="https://img.shields.io/github/stars/josharsh/100LinesOfAICode?style=for-the-badge&logo=github&logoColor=white&color=yellow" alt="Stars">
  </a>
  <a href="https://github.com/josharsh/100LinesOfAICode/network/members">
    <img src="https://img.shields.io/github/forks/josharsh/100LinesOfAICode?style=for-the-badge&logo=github&logoColor=white&color=blue" alt="Forks">
  </a>
  <a href="https://github.com/josharsh/100LinesOfAICode/issues">
    <img src="https://img.shields.io/github/issues/josharsh/100LinesOfAICode?style=for-the-badge&logo=github&logoColor=white&color=red" alt="Issues">
  </a>
  <a href="https://github.com/josharsh/100LinesOfAICode/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/josharsh/100LinesOfAICode?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=green" alt="License">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AI_Tools-8-FF6B6B?style=for-the-badge&logo=anthropic&logoColor=white" alt="AI Tools">
  <img src="https://img.shields.io/badge/Lines-1908-4ECDC4?style=for-the-badge&logo=codesandbox&logoColor=white" alt="Lines">
</p>


> **Powerful AI tools in less than 100 lines each.** No bloat, just results.

Because naming variables IS hard, writing READMEs sucks, and your commit messages could use some work.

---

## 📊 Repository Stats

- 🛠️ **8 AI Tools** - Each under 100 lines
- 🎯 **1,908 lines** of production-ready code
- ⚡ **5 minutes** to try any tool
- 🌟 **Zero dependencies** (except Claude API)

## ⚡ Instant Productivity Wins

Tools every developer uses daily:

| Tool | What It Does | Why You Need It | Lines |
|------|--------------|-----------------|-------|
| [📊 Week Recap](./week-recap/) | "What did I even do this week?" → instant status report | Friday standup panic solver | 65 |
| [📝 README Gen](./readme-gen/) | Generate professional README in 10 seconds | Stop staring at blank README.md | 75 |
| [💬 PR Writer](./pr-writer/) | Write PR descriptions automatically | Never write "fixed stuff" again | 68 |
| [🏷️ Name Variable](./name-it/) | Solve the hardest problem in CS | Because `temp2_final` is not a name | 60 |

## 😊 Make Coding Fun Again

Wholesome tools that spark joy:

| Tool | What It Does | Viral Potential | Lines |
|------|--------------|-----------------|-------|
| [💚 Kind Blame](./kind-blame/) | Git blame but encouraging | "We've all been there ☕" | 70 |
| [🔥 Commit Roaster](./roast-commits/) | Get roasted for your terrible commits | "asdf" - Did your cat walk on your keyboard? | 55 |
| [🦆 Rubber Duck AI](./rubber-duck/) | Debugging buddy that talks back! | Quack quack 🦆 | 80 |

## 🗣️ Communication Helpers

Bridge the dev/business gap:

| Tool | What It Does | Career Impact | Lines |
|------|--------------|---------------|-------|
| [🗣️ Explain to PM](./explain-to-pm/) | Translate tech to business speak | Make your work understood | 72 |
| [💼 Sound Professional](./professional/) | Make messages professional | No more 3am Slack regret | 65 |

## 🚀 Power User Tools

Stay in flow state:

| Tool | What It Does | Time Saved | Lines |
|------|--------------|------------|-------|
| [💡 SO Terminal](./so-terminal/) | Stack Overflow without leaving terminal | Stop context switching | 78 |

---

## 🎯 Quick Start

Get started in under 2 minutes:

```bash
# Clone the repo
git clone https://github.com/josharsh/100LinesOfAICode.git
cd 100LinesOfAICode

# Install dependencies
pip install anthropic requests

# Set your API key
export ANTHROPIC_API_KEY=your_key_here

# Try your first tool!
python week-recap/recap.py
```
## 🛠️ Troubleshooting

- **Missing API key (`ANTHROPIC_API_KEY not found`)**  
  Set the environment variable first: `export ANTHROPIC_API_KEY="your-key"`  
  Get your key at `https://console.anthropic.com/`.

- **API or network errors**  
  Terminal AI automatically retries Anthropic calls **3 times** with a short backoff.  
  If errors persist, check your internet connection or try again later.

- **Command timed out**  
  Shell commands are limited to **30 seconds** to keep the experience responsive.  
  Try a narrower request or run the suggested command manually in your terminal.
  
## 💡 Featured Examples

### Never Forget What You Did

```bash
python week-recap/recap.py

📊 Your Week: Nov 18-22, 2025

🎯 Highlights:
• Shipped user dashboard (merged PR #234)
• Fixed critical login bug affecting 2.3K users
• Code reviewed 12 PRs across 3 repos

💬 Copy-Paste Ready:
"This week I shipped the user dashboard, resolved a critical
auth bug affecting 2.3K users, and reviewed 12 PRs."

✅ Ready for your standup!
```

### Get Roasted by Your Own Code

```bash
python roast-commits/roaster.py

🏆 HALL OF SHAME

1. "asdf"
   👉 Did your cat walk on the keyboard?

2. "fix stuff"
   👉 Wow. Such detail. Very helpful.

3. "final FINAL v3"
   👉 Commitment issues much?

📊 YOUR GRADE: D+
You're better than 12% of developers!
```

### Stop Naming Things Wrong

```bash
python name-it/namer.py

What does this variable store?
> user's email address

📝 Best: userEmail (camelCase - most common)
   Alt: user_email (Python style)
   Simple: email (context-dependent)

💡 Tip: Python uses snake_case for variables!
```
---

## 📖 Philosophy

### Why 100 Lines?

**Constraint breeds creativity.** When you have 100 lines:
- Every line matters
- No framework bloat
- Easy to understand
- Easy to modify
- Actually read the code in minutes

### The Truth About Frameworks

```python
# LangChain: 10,000+ lines of abstraction
from langchain import complicated_chains

# This repo: Direct and clear
from anthropic import Anthropic
client = Anthropic()
response = client.messages.create(...)
```

**You learn more. You understand more. You build better.**

### Mass Market > Technical Brilliance

The best Udemy courses aren't from MIT professors.
The most popular dev tools aren't the most advanced.
**The most viral tools solve universal problems simply.**

---

## 🤝 Contributing

We love contributions! Here's how:

### Adding a New Tool

1. **Solve a real problem** - Must be something developers actually complain about
2. **Keep it ≤100 lines** - Constraint is the feature
3. **Make it shareable** - "OMG look at this!" factor
4. **Write a great README** - Sell the problem, then the solution

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.


## 🌟 Get Started

### For Developers

1. Pick a tool that solves your problem
2. Read the 60-100 line source code
3. Understand exactly how it works
4. Modify it for your needs
5. Share what you built!

### For Learners

Perfect for:
- Understanding AI APIs without frameworks
- Learning practical AI applications
- Seeing production-quality minimal code
- Building your own AI tools

### For Teams

Use these as:
- Daily productivity boosters
- Team culture builders (Kind Blame!)
- Communication improvers
- Code quality maintainers

---

## 💬 Community

- **GitHub Discussions**: Ask questions, share ideas
- **Issues**: Report bugs, request features
- **Twitter**: Share your wins with #100LinesOfAICode
- **Discord**: (coming soon!)

---

## 📜 License

MIT License - see [LICENSE](LICENSE) file.

**Use them. Modify them. Ship them. Make them better.**

---

## 🙏 Acknowledgments

- Inspired by the #100LinesOfCode movement
- Built for developers who hate bloat


**Made for developers.**

**Star this repo if you:**
- Hate writing READMEs
- Forget what you did this week
- Struggle naming variables
- Write "asdf" commits
- Want to sound more professional
- Love simple, working code

⭐ **[Star on GitHub](https://github.com/josharsh/100LinesOfAICode)**
