# 📊 Week Recap

**"What did I even do this week?"** → Instant standup answer from your git history.

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

python recap.py        # Last 7 days
python recap.py 14     # Last 2 weeks
```

## Usage Demo

```bash
$ python recap.py

📊 Analyzing your git history...

🎯 Your Week: Mar 10-14, 2025

Highlights:
• Added user authentication (PR #456)
• Fixed memory leak in data processor  
• Refactored API endpoints for performance
• Code reviewed 8 PRs

💬 Copy-Paste Ready:
"This week I added user authentication, fixed a memory leak,
refactored API endpoints, and reviewed 8 PRs."

📈 Productivity: 47 commits across 12 files

✅ Ready for your standup!
```

## Output

```
📊 Your Week: Nov 18-22

🎯 Highlights:
• Shipped user dashboard (merged PR #234)
• Fixed critical login bug affecting 2.3K users
• Code reviewed 12 PRs

💬 Copy-Paste Status:
"This week I shipped the user dashboard, resolved a critical
auth bug, and reviewed 12 PRs."

✅ Ready for your standup!
```

## Use Cases

- Friday standups
- 1-on-1 meetings
- Weekly reports
- Performance reviews

**65 lines. Never draw a blank again.**
