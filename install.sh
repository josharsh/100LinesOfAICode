#!/bin/bash
# One-click installer for 100 Lines Of AI Code
# Usage: curl -sSL https://raw.githubusercontent.com/josharsh/100LinesOfAICode/main/install.sh | bash

set -e

echo "🤖 Installing 100 Lines Of AI Code..."
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "   Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Found Python $PYTHON_VERSION"

# Clone or update repository
if [ -d "100LinesOfAICode" ]; then
    echo "📦 Updating existing installation..."
    cd 100LinesOfAICode
    git pull
else
    echo "📦 Cloning repository..."
    git clone https://github.com/josharsh/100LinesOfAICode.git
    cd 100LinesOfAICode
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip3 install -q -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your API keys:"
    echo "   - ANTHROPIC_API_KEY (get from https://console.anthropic.com/)"
    echo "   - OPENAI_API_KEY (optional, from https://platform.openai.com/)"
    echo ""
fi

echo "✅ Installation complete!"
echo ""
echo "🚀 Quick Start:"
echo "   cd 100LinesOfAICode"
echo "   python ai-agent/agent.py 'your task here'"
echo ""
echo "📖 Read the README: cat README.md"
echo "💡 Explore tools: ls -d */"
echo ""
echo "⭐ Don't forget to star the repo: https://github.com/josharsh/100LinesOfAICode"
