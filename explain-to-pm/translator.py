#!/usr/bin/env python3
"""Code → PM Speak - Bridge the communication gap, 72 lines"""
import os, sys
from pathlib import Path
from anthropic import Anthropic

class PMTranslator:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def translate(self, technical_text: str, code_context: str = "") -> str:
        """Translate technical description to multiple audiences."""
        prompt = f"""Translate this technical work into language for different audiences:

Technical description: {technical_text}

Code context (if any): {code_context}

Provide translations for:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤓 WHAT YOU BUILT (Technical):
[Keep the technical description]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👔 FOR YOUR PM (Business Value):
[Translate to business impact, user benefits]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💼 FOR EXECUTIVES (ROI Focus):
[Focus on metrics, cost savings, risk reduction]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👶 ELI5 (Explain Like I'm 5):
[Super simple, no jargon]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 FOR YOUR DEMO:
[What to show and say during a demo]

Be concise and clear for each audience!"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1200,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def interactive_mode(self):
        """Interactive translation session."""
        print("🗣️  Code → PM Speak Translator\n")
        print("Bridge the dev/business communication gap!\n")

        while True:
            print("─" * 50)
            print("\nWhat did you build? (technical description)")
            print("Or paste code filename, or 'q' to quit:")
            user_input = input("> ").strip()

            if user_input.lower() in ['q', 'quit', 'exit']:
                print("\n👋 Happy communicating!\n")
                break

            code_context = ""
            if Path(user_input).exists():
                # User provided a file
                with open(user_input, 'r') as f:
                    code_context = f.read()[:2000]  # First 2KB
                print("\n📝 What does this code do? (brief description):")
                tech_description = input("> ").strip()
            else:
                tech_description = user_input

            if not tech_description:
                print("⚠️  Please provide a description.")
                continue

            print("\n🔄 Translating to multiple audiences...\n")
            translations = self.translate(tech_description, code_context)
            print(translations)
            print("\n💡 Tip: Copy the version you need!\n")

def main():
    translator = PMTranslator()
    translator.interactive_mode()

if __name__ == "__main__":
    main()
