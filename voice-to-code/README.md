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
## Example Output by Language


### JavaScript Example
🎤 **Voice Input:** "create async function to fetch user data"
```javascript
async function fetchUserData(userId) {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
}
```
### Java Example
🎤 **Voice Input:** "create a class for a user with getters and setters"
```java
public class User {
    private String name;
    private int age;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```
### Go Example
🎤 **Voice Input:** "create a basic http handler that returns json"
```go
func jsonHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
}
```
### Rust Example
🎤 **Voice Input:** "function to calculate factorial recursively"
```rust
fn factorial(n: u64) -> u64 {
    match n {
        0 | 1 => 1,
        _ => n * factorial(n - 1),
    }
}
```
### C++ Example
🎤 **Voice Input:** "class for a 2d point with a distance method"
```c++
class Point {
public:
    double x, y;
    Point(double xVal, double yVal) : x(xVal), y(yVal) {}
    double distance() const { return std::sqrt(x*x + y*y); }
};
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
