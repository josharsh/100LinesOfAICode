# Contributing to 100 Lines Of AI Code

Thank you for your interest in contributing! This project aims to provide powerful AI tools in minimal, understandable code.

## 🎯 Philosophy

Every contribution should follow these principles:

1. **Simplicity**: Keep it under 100 lines
2. **Clarity**: Code should be readable and well-commented
3. **Utility**: Solve real problems
4. **Education**: Help others learn AI development

## 🚀 How to Contribute

### Adding a New AI Tool

1. **Fork the repository**
   ```bash
   git clone https://github.com/josharsh/100LinesOfAICode.git
   cd 100LinesOfAICode
   ```

2. **Create a new directory**
   ```bash
   mkdir my-ai-tool
   cd my-ai-tool
   ```

3. **Write your tool** (≤100 lines)
   - Main file: `tool.py`
   - Keep it functional and well-documented
   - Add type hints
   - Include error handling

4. **Create README.md**
   Include:
   - Clear description
   - Installation instructions
   - Usage examples
   - How it works section
   - Real-world use cases

5. **Add examples**
   ```bash
   mkdir examples
   # Add example usage files
   ```

6. **Update main README**
   Add your tool to the project table

7. **Test thoroughly**
   ```bash
   python tool.py --help
   # Test all features
   ```

8. **Submit PR**
   - Clear title: "Add: [Tool Name]"
   - Description of what it does
   - Why it's useful
   - Line count

### Improving Existing Tools

1. **Bug Fixes**: Always welcome!
2. **Optimizations**: If it reduces lines without losing functionality
3. **Documentation**: Better examples, clearer explanations
4. **Features**: Only if they don't exceed 100 line limit

### Guidelines

#### Code Quality

```python
# ✅ Good
def generate_code(self, description: str, language: str = "python") -> dict:
    """Generate code from description.

    Args:
        description: Natural language description
        language: Target programming language

    Returns:
        dict with 'code' and 'explanation'
    """
    # Implementation
    pass

# ❌ Avoid
def gen(d, l="py"):
    # What does this do?
    pass
```

#### Keep It Minimal

```python
# ✅ Good - Concise but clear
def search(self, query: str, top_k: int = 3) -> List[Tuple[dict, float]]:
    query_emb = self.simple_embedding(query)
    scores = [np.dot(query_emb, doc_emb) for doc_emb in self.embeddings]
    top_indices = np.argsort(scores)[-top_k:][::-1]
    return [(self.documents[i], scores[i]) for i in top_indices]

# ❌ Avoid - Unnecessarily verbose
def search(self, query: str, top_k: int = 3) -> List[Tuple[dict, float]]:
    query_embedding = self.simple_embedding(query)
    all_scores = []
    for document_embedding in self.embeddings:
        score = np.dot(query_embedding, document_embedding)
        all_scores.append(score)
    sorted_indices = np.argsort(all_scores)
    top_indices = sorted_indices[-top_k:]
    reversed_indices = top_indices[::-1]
    results = []
    for index in reversed_indices:
        results.append((self.documents[index], all_scores[index]))
    return results
```

#### README Template

```markdown
# [Tool Icon] Tool Name

[One-line description] in **XX lines**.

## 🎯 What It Does
[Clear explanation of purpose]

## 🚀 Quick Start
[Copy-paste installation and usage]

## 💡 Usage Examples
[At least 3 real examples]

## 🧠 How It Works
[Brief architecture explanation]

## 🎓 Why This Matters
[Educational value]

---
**Powered by [AI Model] | XX lines | [Tagline]**
```

## 🐛 Bug Reports

When reporting bugs, include:

1. **Description**: What went wrong?
2. **Reproduction**: Steps to reproduce
3. **Expected**: What should happen?
4. **Actual**: What actually happened?
5. **Environment**: OS, Python version, dependencies

Example:
```markdown
**Bug**: Voice-to-Code crashes on Windows

**Steps**:
1. Run `python voice.py`
2. Speak into microphone
3. Crashes with error

**Expected**: Should transcribe speech
**Actual**: `ImportError: pyaudio not found`

**Environment**: Windows 11, Python 3.11
```

## 💡 Feature Requests

Use this template:

```markdown
**Feature**: [Brief title]

**Problem**: What problem does this solve?

**Solution**: Proposed implementation

**Line Count**: Estimated lines needed

**Example**:
[Code example of how it would work]
```

## 📏 The 100-Line Rule

### Counting Lines

```bash
# Count lines (excluding comments and blanks)
grep -v '^\s*#' tool.py | grep -v '^\s*$' | wc -l
```

### What Counts?

✅ **Include**:
- All code
- Docstrings
- Inline comments
- Imports

❌ **Exclude**:
- Blank lines
- File headers (shebang, encoding)

### If You're Over 100 Lines

Strategies to reduce:
1. Use list/dict comprehensions
2. Combine related operations
3. Remove unnecessary error messages
4. Simplify control flow
5. Use lambda functions where appropriate

**But NEVER sacrifice**:
- Code clarity
- Error handling
- Security
- Type safety

## 🎨 Code Style

We follow **PEP 8** with these preferences:

- **Line length**: 120 chars (we need to save vertical space!)
- **Imports**: Standard, third-party, local (separated)
- **Docstrings**: Google style
- **Type hints**: Always for public functions
- **Naming**: Descriptive but concise

```python
# ✅ Good import order
import os, sys, argparse  # Standard (can combine to save lines)
from typing import List, Dict  # Standard typing

import anthropic  # Third-party
import numpy as np  # Third-party

from .utils import helper  # Local
```

## 🧪 Testing

While we keep tools minimal, they should work reliably:

```python
# Add basic tests in examples/
def test_basic_functionality():
    tool = MyTool()
    result = tool.run("test input")
    assert result is not None
    assert "expected" in result
```

## 📝 Documentation

Good documentation is crucial:

1. **README**: Clear, with examples
2. **Docstrings**: Explain purpose and parameters
3. **Comments**: Why, not what
4. **Examples**: Real-world use cases

## 🏆 Recognition

Contributors will be:
- Listed in project README
- Credited in tool documentation
- Mentioned in release notes

## 📞 Questions?

- **GitHub Discussions**: For general questions
- **Issues**: For bugs and features
- **Pull Requests**: For code contributions

## 🎯 Current Needs

We're especially interested in:

- [ ] AI tools for new domains (audio, video, etc.)
- [ ] Performance optimizations
- [ ] Better documentation
- [ ] More usage examples
- [ ] Bug fixes
- [ ] Support for more AI models

## 🌟 Star Contributors

Making significant contributions? You'll be featured as a star contributor!

---

**Thank you for helping make AI accessible, one hundred lines at a time!** ⭐

## Contributor Recognition

This project uses the All Contributors specification.
To add a contributor:
```bash
npx all-contributors-cli add <username> <contribution-type>
```
then run:
```bash
npx all-contributors-cli generate
```
