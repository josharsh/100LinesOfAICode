# ⚡ Terminal AI

**Natural language shell** - Describe what you want, get safe shell commands.

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

python terminal.py
python terminal.py find all large files
```

## Usage Demo

```bash
$ python terminal.py find all files larger than 100MB

🤖 Analyzing your request...

💻 Command: find . -type f -size +100M -exec ls -lh {} \; | sort -k5 -h
📖 Explanation: Finds files over 100MB, lists them with human-readable sizes, sorted by size
⚠️  Risks: None

❓ Execute? [y/N]: y

📤 Output:
1.2G ./backups/old_backup.tar.gz
450M ./videos/project_demo.mp4
120M ./datasets/training_data.csv

✅ Complete! Found 3 large files.
```

## Example Session

```
💭 What do you want to do? find all Python files modified today

💻 Command: find . -name "*.py" -mtime -1
📖 Explanation: Searches for Python files modified in last 24 hours
⚠️  Risks: None

❓ Execute? [y/N]: y

📤 Output:
./agent.py
./terminal.py
```

## Safety Features

- **Safe Mode**: Blocks `rm -rf /`, fork bombs, disk wiping
- **Risk Warnings**: Shows potential dangers before execution
- **Explanations**: Understand what each command does

## Common Uses

```bash
python terminal.py find all .log files older than 30 days
python terminal.py show memory usage
python terminal.py list top 10 CPU-consuming processes
python terminal.py compress all images in this folder
```

## Troubleshooting

### 🔑 Missing API Key
```
⚠️  ANTHROPIC_API_KEY not found!

Set it with:
  export ANTHROPIC_API_KEY="your-key"

Get your key: https://console.anthropic.com/
```

### 🌐 Network Errors
The tool automatically retries failed API calls **3 times** with exponential backoff. If errors persist:
- Check your internet connection
- Verify firewall/proxy settings
- Try again later (possible API outage)

### ⏰ Command Timeout
Shell commands are limited to **30 seconds**. If your command times out:
- Try a more specific/narrow request
- Run the suggested command directly in your terminal
- Use `safe off` mode for more flexibility

### 🚫 Command Blocked
```
⛔ Dangerous command blocked by safe mode
```
This is intentional! Safe mode protects you from destructive commands. Use `--unsafe` flag if you really need to run it.

### ❓ Empty Input
```
💭 What do you want to do?
⚠️  Please describe what you'd like to do!
```
Simply describe what you want to accomplish in natural language.

**88 lines. Safe by default.**
