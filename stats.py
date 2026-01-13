import glob
import requests
import os

files = glob.glob("**/*.py", recursive=True)

tool_dirs = [
    "ai-agent", "code-reviewer", "commit_ai", "explain-to-pm",
    "kind-blame", "mcp-server", "mini-rag", "name-it",
    "pr-writer", "professional", "readme-gen", "roast-commits",
    "rubber-duck", "so-terminal", "terminal-ai", "voice-to-code",
    "week-recap"
]

ai_tools = []
for tool_dir in tool_dirs:
   tool_files = glob.glob(f"{tool_dir}/*.py")
   tool_files = [f for f in tool_files if not f.endswith("__init__.py")]
   
   for file in tool_files:
       if os.path.exists(file):
           with open(file, encoding="utf-8") as f:
               lines = f.readlines()
               code_lines = [line for line in lines if line.strip() and not line.strip().startswith("#")]
               if len(lines) <= 100:
                   ai_tools.append((file, len(lines), len(code_lines)))

total_lines = sum(len(open(f, encoding="utf-8").readlines()) for f in files if os.path.exists(f))

print(f"Number of AI Tools (<100 lines): {len(ai_tools)}")
print(f"Total lines of code: {total_lines}")
print("\nAI Tools found:")
for f, total, code in ai_tools:
    print(f" - {f}: {total} lines total, {code} lines of code")

GITHUB_USER = "josharsh"
REPO_NAME = "100LinesOfAICode"

badges = {
    "stars": f"https://img.shields.io/github/stars/{GITHUB_USER}/{REPO_NAME}?style=flat-square",
    "forks": f"https://img.shields.io/github/forks/{GITHUB_USER}/{REPO_NAME}?style=flat-square",
    "issues": f"https://img.shields.io/github/issues/{GITHUB_USER}/{REPO_NAME}?style=flat-square",
    "license": f"https://img.shields.io/github/license/{GITHUB_USER}/{REPO_NAME}?style=flat-square",
    "python": "https://img.shields.io/badge/python-3.8+-blue?style=flat-square",
    "ai_tools": f"https://img.shields.io/badge/AI_Tools-{len(ai_tools)}-blue?style=flat-square",
    "lines": f"https://img.shields.io/badge/Lines-{total_lines}-blue?style=flat-square"
}

print("\n📋 Badges Markdown for README.md:")
print("\nCopy-paste this after the title in README.md:\n")
for name, url in badges.items():
    print(f"![{name.title()}]({url})")

print("\n\n📊 Stats Section:")
print("\nCopy-paste this before 'Try It Now':\n")
print(f"""## 📊 Repository Stats

- 🛠️ **{len(ai_tools)} AI Tools** - Each under 100 lines
- 🎯 **{total_lines:,} lines** of production-ready code
- ⚡ **5 minutes** to try any tool
- 🌟 **Zero dependencies** (except Claude API)
""")

print("\n Script completed! Update your README.md with the sections above.")