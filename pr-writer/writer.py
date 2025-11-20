#!/usr/bin/env python3
"""PR Description Writer - Never write PR descriptions again, 68 lines"""
import os, sys, subprocess
from anthropic import Anthropic

class PRWriter:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def get_diff_info(self) -> dict:
        """Get current git diff and branch information."""
        try:
            # Get current branch
            branch = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True, text=True, check=True
            ).stdout.strip()

            # Get diff stats
            stats = subprocess.run(
                ["git", "diff", "--stat", "HEAD"],
                capture_output=True, text=True
            ).stdout.strip()

            # Get full diff (limit size)
            diff = subprocess.run(
                ["git", "diff", "HEAD"],
                capture_output=True, text=True
            ).stdout.strip()[:5000]  # Limit to 5KB

            # Get recent commits on this branch
            commits = subprocess.run(
                ["git", "log", "--oneline", "-5"],
                capture_output=True, text=True
            ).stdout.strip()

            return {"branch": branch, "stats": stats, "diff": diff, "commits": commits}
        except Exception as e:
            return {"error": str(e)}

    def generate_description(self) -> str:
        """Generate a professional PR description."""
        diff_info = self.get_diff_info()

        if "error" in diff_info:
            return f"❌ Error: {diff_info['error']}\nMake sure you have uncommitted changes."

        prompt = f"""Create a professional Pull Request description based on these changes:

Branch: {diff_info['branch']}
Recent commits: {diff_info['commits']}
Diff stats: {diff_info['stats']}
Changes: {diff_info['diff']}

Generate a PR description with:

## 🎯 What This Does
(Clear explanation of the changes)

## 🤔 Why We Need It
(Business value or problem being solved)

## ⚙️ How It Works
(Brief technical overview, numbered list)

## ✅ Testing
- [ ] List of testing done (be specific)

## 📸 Screenshots
(Note if screenshots would be helpful)

## 🚀 Deployment Notes
(Any special considerations, migrations, env vars, etc.)

Be professional, concise, and thorough. Focus on the "why" and "what", not just "how"."""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

def main():
    print("📝 Analyzing your changes...\n")

    if not os.path.exists(".git"):
        print("❌ Not a git repository")
        sys.exit(1)

    writer = PRWriter()
    description = writer.generate_description()

    print("Generated PR Description:")
    print("="*60)
    print(description)
    print("="*60)
    print("\n✅ Ready to paste into your PR!")
    print("💡 Edit as needed, then ship it! 🚀\n")

if __name__ == "__main__":
    main()
