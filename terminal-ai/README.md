# ⚡ Terminal AI - Natural Language Shell

Speak commands naturally, get safe shell commands in **88 lines**.

## 🎯 What It Does

- 💬 **Natural Language**: Describe what you want in plain English
- 🤖 **AI Translation**: Converts to proper shell commands
- 🔒 **Safety First**: Blocks dangerous commands by default
- 📖 **Explains Everything**: Shows what each command does
- ⚡ **Execute or Copy**: Run directly or copy for later

## 🚀 Quick Start

```bash
# Install
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY="your-key-here"

# Interactive mode
python terminal.py

# One-off command
python terminal.py find all large files
```

## 💡 Usage Examples

### Interactive Mode

```bash
python terminal.py
```

**Example Session:**
```
🤖 Terminal AI - Type your requests in natural language
   Commands: 'exit', 'quit' to leave | 'safe on/off' to toggle safe mode
   Safe mode: ON | OS: Linux 5.15.0

💭 What do you want to do? find all Python files modified today

💻 Command: find . -name "*.py" -mtime -1
📖 Explanation: Searches current directory for Python files modified in last 24 hours
⚠️  Risks: None

❓ Execute: find . -name "*.py" -mtime -1
   Proceed? [y/N]: y

📤 Output:
./agent.py
./terminal.py
./commit.py

💭 What do you want to do? show me disk usage sorted by size

💻 Command: du -sh * | sort -h
📖 Explanation: Shows disk usage of all items in current directory, sorted by size
⚠️  Risks: None

❓ Execute: du -sh * | sort -h
   Proceed? [y/N]: y

📤 Output:
4.0K    README.md
128K    docs
1.2M    src
```

### One-off Commands

```bash
# Generate command only
python terminal.py list all running processes

# Generate and execute (with confirmation)
python terminal.py find large files over 100MB

# Execute without confirmation (careful!)
python terminal.py count lines of code --execute
```

## 🎮 Common Use Cases

### File Operations

```bash
python terminal.py find all .log files older than 30 days
python terminal.py compress all images in this folder
python terminal.py rename all .txt files to .md
python terminal.py find duplicate files
```

### System Information

```bash
python terminal.py show memory usage
python terminal.py list top 10 CPU-consuming processes
python terminal.py check disk space
python terminal.py what's my IP address
```

### Git Operations

```bash
python terminal.py show all commits from last week
python terminal.py find largest files in git history
python terminal.py list all branches sorted by last commit
python terminal.py clean up merged branches
```

### Network & Web

```bash
python terminal.py download this YouTube video
python terminal.py check if port 8080 is open
python terminal.py find my public IP
python terminal.py test internet speed
```

### Data Processing

```bash
python terminal.py count unique words in all text files
python terminal.py merge all CSV files
python terminal.py extract column 3 from data.csv
python terminal.py convert all PNG to JPG
```

## 🔒 Safety Features

### Safe Mode (Default)

Blocks dangerous patterns:
- `rm -rf /`
- Fork bombs
- Disk wiping commands
- File system formatting
- Other destructive operations

**Example:**
```
💭 What do you want to do? delete everything

⛔ Dangerous command blocked by safe mode
```

### Disable Safe Mode

```bash
# Interactive
💭 safe off

# Command line
python terminal.py --unsafe delete old logs
```

### Risk Warnings

Every command shows potential risks:
```
💻 Command: sudo apt-get upgrade -y
📖 Explanation: Upgrades all system packages without confirmation
⚠️  Risks: May break dependencies, requires sudo, changes system state
```

## 🧠 How It Works

```
┌───────────┐    ┌─────────┐    ┌──────────┐
│  Natural  │ -> │ Claude  │ -> │  Shell   │
│ Language  │    │   AI    │    │ Command  │
└───────────┘    └─────────┘    └──────────┘
                                      │
                                      v
                            ┌──────────────────┐
                            │ Safety Check     │
                            │ + Explanation    │
                            │ + Risk Warning   │
                            └──────────────────┘
```

1. **Parse**: User describes intent in natural language
2. **Generate**: Claude converts to shell command
3. **Validate**: Safety check against dangerous patterns
4. **Explain**: Shows what command does and risks
5. **Execute**: Optionally runs with user confirmation

## 🎓 Smart Context Awareness

The AI considers:
- **Your OS**: Generates appropriate commands (macOS vs Linux vs Windows)
- **Current Directory**: Provides context-aware suggestions
- **Common Tools**: Uses standard utilities (grep, find, awk, etc.)

**Example:**
```bash
# macOS
python terminal.py open current folder in finder
# Generated: open .

# Linux
python terminal.py open current folder in file manager
# Generated: xdg-open .

# Windows
python terminal.py open current folder in explorer
# Generated: explorer .
```

## 🔧 Configuration

### Customize Safety Rules

Edit `DANGEROUS_COMMANDS` in terminal.py:
```python
DANGEROUS_COMMANDS = [
    "rm -rf /",
    ":(){ :|:& };:",
    "dd if=/dev/zero",
    "mkfs",
    # Add your own patterns
    "sudo reboot",
    "sudo shutdown"
]
```

### Change Model

```python
# Use faster/cheaper model
response = self.client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1024,
    messages=[...]
)
```

## 📊 Comparison

| Tool | Natural Language | Safety | Explanation | Multi-OS |
|------|------------------|--------|-------------|----------|
| Terminal AI | ✅ | ✅ | ✅ | ✅ |
| man pages | ❌ | N/A | ✅ | ❌ |
| StackOverflow | ❌ | ❌ | ✅ | ❌ |
| GitHub Copilot | ⚠️ | ❌ | ⚠️ | ✅ |

## 🎯 Best Practices

### 1. Be Specific

```
❌ "find files"
✅ "find Python files modified in last 7 days"
```

### 2. Ask for Explanations

Every command includes explanation - read it!

### 3. Review Before Executing

Always review the generated command, especially:
- Commands with `sudo`
- File deletions
- System modifications

### 4. Start Safe

Keep safe mode ON until you're comfortable.

## 🐛 Troubleshooting

**"Command not found"**
- AI suggested command not installed on your system
- Install missing tool or rephrase request

**"Permission denied"**
- Command needs elevated privileges
- Run with `sudo` or check file permissions

**"Command timed out"**
- Increase timeout in `execute_command()` (line 60)
- Or run long commands manually

**"API key not found"**
```bash
export ANTHROPIC_API_KEY="your-key"
```

## 🚀 Advanced Usage

### Alias for Quick Access

Add to `~/.bashrc` or `~/.zshrc`:
```bash
alias ask="python /path/to/terminal.py"
```

Usage:
```bash
ask find all TODO comments in code
ask compress this video to under 10MB
ask what processes are using port 3000
```

### Chain with Other Commands

```bash
# Generate command, pipe to clipboard
python terminal.py count code lines | grep "COMMAND:" | cut -d: -f2 | pbcopy

# Execute directly (be careful!)
eval $(python terminal.py list files --execute | grep "COMMAND:" | cut -d: -f2)
```

### Create Command Library

```bash
# Save favorite commands
python terminal.py find memory leaks > ~/commands/find_leaks.sh
python terminal.py cleanup docker > ~/commands/docker_clean.sh
```

## 🌟 Real-World Examples

### DevOps

```
"restart nginx service"
"check if redis is running"
"tail last 100 lines of error log"
"find which process is using port 8080"
```

### Data Science

```
"split this CSV into train and test sets"
"count rows where column 2 is empty"
"find correlation between columns"
```

### System Admin

```
"find users who haven't logged in for 90 days"
"check SSL certificate expiration"
"list cron jobs for all users"
```

## 📚 Further Reading

- [Shell Command Best Practices](https://google.github.io/styleguide/shellguide.html)
- [Common Shell Commands](https://ss64.com/)
- [Safety in Shell Scripts](https://mywiki.wooledge.org/BashPitfalls)

## 🤝 Contributing

Ideas:
- [ ] Command history
- [ ] Favorites/bookmarks
- [ ] Multi-step workflows
- [ ] Command suggestions
- [ ] Learning mode with tutorials

---

**Powered by Claude 3.5 Sonnet | 88 lines | Safe by default**
