# 💡 Stack Overflow Terminal

**Stop context switching** - Get answers without leaving your terminal.

## Quick Start

```bash
pip install anthropic requests
export ANTHROPIC_API_KEY=your_key

python so.py                              # Interactive
python so.py "reverse list in python"     # Direct
```

## Output

```
🔍 Searching: reverse list in python

📚 Best Answer:

# Method 1: In-place
my_list.reverse()

# Method 2: New list
new_list = my_list[::-1]

# Method 3: Iterator
list(reversed(my_list))

⚠️ Important:
- Use .reverse() to modify original
- Use [::-1] for new list
- reversed() is memory-efficient

🔗 Source: Stack Overflow (342K views, 2.4K upvotes)
```

## Why It's Better

**Without:** Open browser → Read → Copy → Switch back → Lost focus
**With:** Type question → Get answer → Keep coding → Stay in flow

**78 lines. Zero context switching.**
