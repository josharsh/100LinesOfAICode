# 🏷️ Name Variable

**The hardest problem in CS** - Solved in 60 lines.

> *"There are only two hard problems: cache invalidation, naming things, and off-by-one errors."*

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

python namer.py                          # Interactive
python namer.py "list of active users"   # Direct
```

## Output

```
What does this variable store?
> user's email address

📝 Top Suggestions:
1. userEmail - camelCase, most common
2. user_email - snake_case, Python style
3. email - simple, context-dependent

🎯 In Different Contexts:
• Class: self.user_email
• Function: def send_mail(user_email):
• Database: user_email
• JSON: "email" or "userEmail"

⚡ Tip: Python uses snake_case for variables
```

**60 lines. Never write `temp2_final` again.**
