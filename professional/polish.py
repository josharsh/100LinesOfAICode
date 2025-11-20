#!/usr/bin/env python3
"""Make Me Sound Professional - No more 3am message regret, 65 lines"""
import os, sys
from anthropic import Anthropic

class ProfessionalPolish:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def polish(self, casual_message: str) -> str:
        """Transform casual message to professional versions."""
        prompt = f"""Transform this casual message into professional versions:

Original message: "{casual_message}"

Provide 4 different formality levels:

━━━━━━━━━━━━━━━━━━━━━━━━━━━
😎 CASUAL BUT CLEAR:
[Friendly and approachable, but clear]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
👔 PROFESSIONAL:
[Standard professional tone]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
💼 EXTRA PROFESSIONAL:
[Very formal, executive-level communication]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤝 FRIENDLY PROFESSIONAL:
[Professional but warm and collaborative]

━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Quick Tip:
[One-liner about when to use each version]

Keep each version concise and natural-sounding!"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def interactive_mode(self):
        """Interactive polishing session."""
        print("💼 Make Me Sound Professional\n")
        print("Transform casual messages into professional ones!")
        print("Type 'quit' to exit\n")
        print("═" * 50 + "\n")

        while True:
            print("Paste your message (or 'quit'):")
            message = input("> ").strip()

            if not message:
                continue

            if message.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Professional communication awaits!\n")
                break

            print("\n✨ Polishing your message...\n")
            polished = self.polish(message)
            print(polished)
            print("\n" + "═" * 50 + "\n")

def main():
    if len(sys.argv) > 1:
        # Direct mode
        message = " ".join(sys.argv[1:])
        polisher = ProfessionalPolish()
        print(polisher.polish(message))
    else:
        # Interactive mode
        polisher = ProfessionalPolish()
        polisher.interactive_mode()

if __name__ == "__main__":
    main()
