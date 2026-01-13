#!/usr/bin/env python3
"""AI Commit Message Generator - Perfect commits in <100 lines."""
import os, sys, subprocess, argparse
from anthropic import Anthropic

class CommitAI:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def get_diff(self, staged_only: bool = True) -> str:
        """Get git diff."""
        cmd = ["git", "diff", "--cached"] if staged_only else ["git", "diff", "HEAD"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    def get_branch(self) -> str:
        """Get current git branch."""
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
        return result.stdout.strip()

    def get_recent_commits(self, count: int = 5) -> str:
        """Get recent commit messages for style reference."""
        result = subprocess.run(["git", "log", f"-{count}", "--pretty=format:%s"], capture_output=True, text=True)
        return result.stdout.strip()

    def generate_commit_message(self, diff: str, conventional: bool = True, branch: str = None, recent_style: str = None) -> str:
        """Generate commit message from diff using AI."""
        prompt = f"""Generate a commit message for these changes:

```diff
{diff[:4000]}
```

Current branch: {branch or 'unknown'}

Recent commit style examples:
{recent_style or 'None available'}

Requirements:
1. {"Use Conventional Commits format: type(scope): description" if conventional else "Clear, concise description"}
2. Types: feat, fix, docs, style, refactor, test, chore
3. First line ≤50 chars (subject)
4. Optional body after blank line explaining "why" not "what"
5. List breaking changes if any

Output ONLY the commit message, no explanation."""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()

    def generate(self, staged_only: bool = True, conventional: bool = True, auto_commit: bool = False) -> str:
        """Main function to generate commit message."""
        diff = self.get_diff(staged_only)

        if not diff:
            return "❌ No changes to commit. Stage changes first with 'git add'."

        branch = self.get_branch()
        recent = self.get_recent_commits()

        print("🤖 Analyzing changes...")
        message = self.generate_commit_message(diff, conventional, branch, recent)

        if auto_commit:
            subprocess.run(["git", "commit", "-m", message], check=True)
            return f"✅ Committed with message:\n{message}"
        else:
            return message

def main():
    parser = argparse.ArgumentParser(description="AI-powered commit message generator")
    parser.add_argument("--all", action="store_true", help="Include unstaged changes")
    parser.add_argument("--conventional", action="store_true", default=True, help="Use Conventional Commits format")
    parser.add_argument("--simple", action="store_true", help="Simple format (not conventional)")
    parser.add_argument("--commit", action="store_true", help="Auto-commit with generated message")
    parser.add_argument("--silent", action="store_true", help="Output only message (for scripting)")
    args = parser.parse_args()

    ai = CommitAI()
    message = ai.generate(
        staged_only=not args.all,
        conventional=not args.simple,
        auto_commit=args.commit
    )

    if args.silent:
        print(message.split('\n')[0])  # Only first line for git commit -m
    else:
        print(f"\n📝 Generated Commit Message:\n{'='*50}")
        print(message)
        print(f"{'='*50}\n")

        if not args.commit:
            print("💡 To commit with this message:")
            print(f"   git commit -m \"{message.split(chr(10))[0]}\"")
            print("\nOr use: python commit.py --commit")

if __name__ == "__main__":
    main()
