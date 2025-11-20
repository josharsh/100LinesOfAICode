#!/usr/bin/env python3
"""Commit Message Roaster - Get brutally judged, 55 lines"""
import os, sys, subprocess
from anthropic import Anthropic

class CommitRoaster:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def get_commit_messages(self, count: int = 100) -> list:
        """Get recent commit messages."""
        try:
            result = subprocess.run(
                ["git", "log", f"-{count}", "--format=%s"],
                capture_output=True, text=True, check=True
            )
            return [msg for msg in result.stdout.strip().split("\n") if msg]
        except Exception:
            return []

    def roast_commits(self, messages: list) -> str:
        """Roast those terrible commit messages."""
        messages_text = "\n".join(messages[:50])  # Limit to 50

        prompt = f"""Analyze these commit messages and roast them humorously:

{messages_text}

Provide:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 HALL OF SHAME
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pick the 5 worst commits and roast them with humor:
1. "[commit message]"
   👉 [witty, sarcastic roast]

2-5. [more roasts]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 YOUR GRADE: [A-F]
[Funny assessment of overall quality]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 How to Write Good Commits:
[3 quick tips with examples]

Be funny but not mean. Educational + entertaining!"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

def main():
    if not os.path.exists(".git"):
        print("❌ Not a git repository")
        sys.exit(1)

    print("🔥 Commit Message Roaster\n")
    print("Analyzing your commit history...\n")

    roaster = CommitRoaster()
    messages = roaster.get_commit_messages()

    if not messages:
        print("❌ No commits found!")
        sys.exit(1)

    print(roaster.roast_commits(messages))
    print("\n💡 Want to improve? Write commits like:")
    print('   ✅ "fix(auth): resolve token expiration in Safari"')
    print('   ✅ "feat(api): add user profile endpoint"')
    print('   ✅ "docs: update installation guide"\n')

if __name__ == "__main__":
    main()
