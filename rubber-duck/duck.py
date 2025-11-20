#!/usr/bin/env python3
"""AI Rubber Duck - Your debugging buddy that talks back, 80 lines"""
import os, sys
from anthropic import Anthropic

class RubberDuck:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.conversation = []

    def quack(self, user_message: str) -> str:
        """The duck responds!"""
        # Build conversation history
        self.conversation.append({"role": "user", "content": user_message})

        system_prompt = """You are a helpful rubber duck debugging assistant. Your job is to help developers
think through problems using the rubber duck debugging method.

Key behaviors:
1. Ask clarifying questions to help them think
2. Use the Socratic method - guide them to the answer
3. Be encouraging and friendly
4. Use duck emojis 🦆 occasionally
5. When they have an "aha moment", celebrate with excitement
6. If they're stuck, provide gentle hints
7. Keep responses concise and conversational

Remember: Often just explaining the problem out loud helps them solve it!"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            system=system_prompt,
            messages=self.conversation
        )

        assistant_message = response.content[0].text
        self.conversation.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    def start_session(self):
        """Interactive debugging session."""
        print("🦆 AI Rubber Duck Debugging\n")
        print("═" * 50)
        print("Hi! I'm your rubber duck. Tell me what's bugging you!")
        print("(I'll help you think through it)")
        print("Type 'quit' to exit, 'clear' to start over")
        print("═" * 50 + "\n")

        while True:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n🦆 *quack* Happy debugging! Come back anytime!\n")
                break

            if user_input.lower() == 'clear':
                self.conversation = []
                print("\n🦆 Memory cleared! What's the new problem?\n")
                continue

            if user_input.lower() == 'help':
                print("\n🦆 Just tell me about your bug! I'll ask questions to help you think.")
                print("Commands: 'quit' to exit, 'clear' to start over\n")
                continue

            # Get duck's response
            response = self.quack(user_input)
            print(f"\n🦆 Duck: {response}\n")

def main():
    if len(sys.argv) > 1:
        # Quick mode - single question
        question = " ".join(sys.argv[1:])
        duck = RubberDuck()
        print(f"\n🦆 Duck: {duck.quack(question)}\n")
    else:
        # Interactive mode
        duck = RubberDuck()
        duck.start_session()

if __name__ == "__main__":
    main()
