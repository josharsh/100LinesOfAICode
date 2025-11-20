#!/usr/bin/env python3
"""Name This Variable - Solve the hardest problem in programming, 60 lines"""
import os, sys
from anthropic import Anthropic

class VariableNamer:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def suggest_names(self, description: str, language: str = "python") -> str:
        """Suggest variable names based on description."""
        prompt = f"""The developer needs a variable name for: "{description}"

Programming language: {language}

Suggest variable names following these rules:
1. Best practices (camelCase, snake_case, etc. based on language)
2. Clear and descriptive
3. Not too long, not too short
4. Language conventions

Provide:
📝 Top 5 Name Suggestions (ranked best to worst):
1. [name] - [why it's good]
2. [name] - [why it's good]
3-5. [more options]

🎯 In Different Contexts:
- Class property/field: [example]
- Function parameter: [example]
- Local variable: [example]
- Constant: [example]
- Database column: [example]
- API field (JSON): [example]

⚡ Quick Convention Tip:
[One-liner about naming in this language]

Keep it concise and practical!"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def interactive_mode(self):
        """Run interactive naming session."""
        print("🏷️  Variable Namer - Solve the hardest problem in CS\n")
        print('"There are only two hard problems in CS: cache invalidation,')
        print('naming things, and off-by-one errors." - Phil Karlton\n')

        while True:
            print("─" * 50)
            description = input("\nWhat does this variable store? (or 'q' to quit)\n> ").strip()

            if description.lower() in ['q', 'quit', 'exit']:
                print("\n👋 Happy naming!\n")
                break

            if not description:
                print("⚠️  Please describe what the variable stores.")
                continue

            language = input("Language (python/javascript/go/etc.): ").strip().lower() or "python"

            print("\n🤔 Thinking of great names...\n")
            suggestions = self.suggest_names(description, language)
            print(suggestions)

def main():
    if len(sys.argv) > 1:
        # Direct mode
        description = " ".join(sys.argv[1:])
        namer = VariableNamer()
        print(namer.suggest_names(description))
    else:
        # Interactive mode
        namer = VariableNamer()
        namer.interactive_mode()

if __name__ == "__main__":
    main()
