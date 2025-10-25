# 🎤 Voice to Code - Speak Your Code

Turn speech into working code in **94 lines** - the future of programming is here!

## 🎯 What It Does

- 🎤 **Listen**: Capture your voice describing what you want
- 🧠 **Understand**: AI interprets your natural language
- 💻 **Generate**: Creates production-ready code
- 💾 **Save**: Optionally saves to file

## 🚀 Quick Start

```bash
# Install dependencies
pip install anthropic SpeechRecognition pyaudio

# macOS users may need
brew install portaudio

# Linux users may need
sudo apt-get install portaudio19-dev python3-pyaudio

# Set API key
export ANTHROPIC_API_KEY="your-key-here"

# Start coding by voice
python voice.py

# Speak: "Create a function that calculates fibonacci numbers"
```

## 💡 Usage Examples

### Basic Voice Input

```bash
python voice.py
```

**Example Session:**
```
🎤 Listening... (speak now)
💭 You said: "create a web scraper that extracts all links from a webpage"

============================================================
"""Web scraper to extract all links from a webpage."""
import requests
from bs4 import BeautifulSoup
from typing import List

def extract_links(url: str) -> List[str]:
    """Extract all links from a webpage.

    Args:
        url: The webpage URL to scrape

    Returns:
        List of all href links found on the page
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

# Usage
if __name__ == "__main__":
    links = extract_links("https://example.com")
    print(f"Found {len(links)} links")
    for link in links[:10]:
        print(f"  - {link}")
============================================================
```

### Different Languages

```bash
python voice.py --lang javascript
# Speak: "create a react component for a user profile card"

python voice.py --lang java
# Speak: "implement a binary search algorithm"

python voice.py --lang typescript
# Speak: "make a type safe API client"
```

### Save to File

```bash
python voice.py --save
# Automatically saves to generated.py

python voice.py --save --file mycode.py
# Saves to custom filename
```

### Text Input (No Voice)

```bash
python voice.py --text "create a REST API endpoint for user login" --save
```

## 🎮 Advanced Examples

### Quick Prototyping

```bash
# Speak multiple components
python voice.py --save --file database.py
# "create a SQLite database wrapper class"

python voice.py --save --file api.py
# "create a Flask API that uses the database"

python voice.py --save --file test.py
# "write unit tests for the API"
```

### Learning New Languages

```bash
# Learn Rust
python voice.py --lang rust
# "create a thread safe counter using Arc and Mutex"

# Learn Go
python voice.py --lang go
# "create a concurrent web crawler"
```

### Code Snippets

```bash
python voice.py --text "decorator for timing function execution"
python voice.py --text "regex pattern for email validation"
python voice.py --text "binary search tree implementation"
```

## 🧠 Supported Languages

- Python
- JavaScript / TypeScript
- Java
- Go
- Rust
- C / C++
- Ruby
- PHP
- And any language Claude understands!

## 🎯 Real-World Use Cases

### 1. Rapid Prototyping
Speak your ideas, get working code instantly.

### 2. Learning Programming
Describe what you want to learn, get example code.

### 3. Accessibility
Code without typing - great for RSI or disabilities.

### 4. Pair Programming
Describe algorithms while AI writes boilerplate.

### 5. Documentation to Code
Read requirements aloud, generate implementation.

## 📊 Tips for Better Results

### Be Specific
```
❌ "make a function"
✅ "create a function that validates email addresses using regex"
```

### Include Requirements
```
❌ "web server"
✅ "create a Flask web server with CORS enabled and error handling"
```

### Mention Language Features
```
✅ "async function that fetches data from multiple APIs concurrently"
✅ "type safe TypeScript interface for user data"
```

## 🔧 Troubleshooting

**"Microphone not found"**
```bash
# Test your mic
python -c "import speech_recognition as sr; sr.Microphone.list_microphone_names()"

# Specify mic index
# Edit voice.py line 17:
with sr.Microphone(device_index=1) as source:
```

**"Could not understand audio"**
- Speak clearly and at normal pace
- Reduce background noise
- Check microphone volume
- Try the --text option instead

**"Installation failed"**
```bash
# macOS
brew install portaudio
pip install pyaudio

# Linux
sudo apt-get install portaudio19-dev
pip install pyaudio

# Windows
pip install pipwin
pipwin install pyaudio
```

## 🎓 How It Works

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌──────┐
│  Voice  │ -> │ Speech   │ -> │ Claude  │ -> │ Code │
│  Input  │    │ to Text  │    │   AI    │    │      │
└─────────┘    └──────────┘    └─────────┘    └──────┘
                  (Google)      (Anthropic)
```

1. **Capture**: Records audio from microphone
2. **Transcribe**: Google Speech Recognition converts to text
3. **Generate**: Claude interprets and writes code
4. **Output**: Formatted, working code

## 🚀 Future Ideas

- [ ] Multi-turn conversations
- [ ] Edit existing code by voice
- [ ] Voice-activated debugging
- [ ] Code explanation by voice
- [ ] Team voice coding sessions

## 🤝 Contributing

Improvements welcome:
- [ ] Offline speech recognition
- [ ] Custom wake word
- [ ] Code quality validation
- [ ] Multi-language UI
- [ ] Voice-controlled IDE plugin

---

**Powered by Claude 3.5 Sonnet + Google Speech | 94 lines | The future of coding**
