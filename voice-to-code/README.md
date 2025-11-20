# 🎤 Voice to Code

**Speak your code into existence** - Turn natural language into working programs.

## Quick Start

```bash
pip install anthropic SpeechRecognition pyaudio
brew install portaudio  # macOS

export ANTHROPIC_API_KEY=your_key

python voice.py
# Speak: "Create a function that calculates fibonacci numbers"
```

## Example Output

```
🎤 Listening...
💭 You said: "create a web scraper that extracts all links"

============================================================
import requests
from bs4 import BeautifulSoup

def extract_links(url: str) -> list:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [a.get('href') for a in soup.find_all('a', href=True)]
============================================================
```

## Options

```bash
python voice.py --lang javascript  # Different languages
python voice.py --save             # Save to file
python voice.py --text "..."       # Text input (no voice)
```

## Use Cases

- **Rapid Prototyping**: Speak ideas, get working code
- **Learning**: Describe concepts, get examples
- **Accessibility**: Code without typing

**94 lines. The future of coding.**
