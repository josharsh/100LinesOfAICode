# 🤖 Autonomous AI Agent

**Self-correcting agent** - Uses tools, plans, and executes complex tasks.

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

python agent.py "find all TODO comments in this codebase"
python agent.py "create a CSV with filenames and line counts"
```

## What It Does

5 built-in tools:
- **execute_code** - Run Python safely
- **read_file** - Read any file
- **write_file** - Create/update files
- **list_files** - Directory listing
- **search_code** - Grep patterns

Example:
```bash
$ python agent.py "analyze this codebase and create summary.md"

🤖 Agent starting task...
→ Using tool: list_files
→ Using tool: read_file (3 times)
→ Using tool: write_file
✓ Task completed in 4 iterations

📊 Created summary.md with codebase insights
```

**95 lines. Fully autonomous.**
