#!/usr/bin/env python3
"""What Did I Even Do This Week? - Weekly Developer Recap in 65 lines"""
import os, subprocess, sys
from datetime import datetime, timedelta
from anthropic import Anthropic

class WeekRecap:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def get_git_activity(self, days: int = 7) -> dict:
        """Get git activity for the past N days."""
        since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        try:
            # Get commits
            commits = subprocess.run(
                ["git", "log", f"--since={since}", "--all", "--format=%h|%s|%an"],
                capture_output=True, text=True, check=True
            ).stdout.strip().split("\n")

            # Get stats
            stats = subprocess.run(
                ["git", "log", f"--since={since}", "--all", "--shortstat", "--format="],
                capture_output=True, text=True
            ).stdout.strip()

            # Get branches
            branches = subprocess.run(
                ["git", "branch", "-a"], capture_output=True, text=True
            ).stdout.strip().split("\n")

            return {
                "commits": [c for c in commits if c],
                "stats": stats,
                "branches": len([b for b in branches if "remotes" not in b])
            }
        except Exception as e:
            return {"error": str(e), "commits": [], "stats": "", "branches": 0}

    def generate_recap(self, days: int = 7) -> str:
        """Generate a friendly weekly recap."""
        activity = self.get_git_activity(days)

        if not activity["commits"]:
            return "📊 No git activity found in the last week. Time to ship some code! 🚀"

        # Prepare context for AI
        commit_list = "\n".join(activity["commits"][:50])  # Limit to 50 commits

        prompt = f"""Analyze this developer's work from the past {days} days and create a friendly, professional recap.

Git Activity:
{commit_list}

Stats: {activity["stats"]}
Active branches: {activity["branches"]}

Create a recap with:
1. 🎯 Highlights (3-5 key accomplishments in bullet points)
2. 📈 Stats That Make Them Look Good (commits, features, bugs fixed, PRs reviewed if mentioned)
3. 💬 Copy-Paste Ready Status Update (2-3 sentences for standup/manager)

Be positive, concise, and make them look productive. Focus on impact, not just activity."""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def display_recap(self, days: int = 7):
        """Display the weekly recap."""
        start_date = (datetime.now() - timedelta(days=days)).strftime("%b %d")
        end_date = datetime.now().strftime("%b %d, %Y")

        print(f"\n📊 Your Week: {start_date} - {end_date}\n")
        print("Analyzing git history...\n")

        recap = self.generate_recap(days)
        print(recap)
        print("\n✅ Ready for your standup!\n")

def main():
    if not os.path.exists(".git"):
        print("❌ Not a git repository. Run this in a git project.")
        sys.exit(1)

    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    recapper = WeekRecap()
    recapper.display_recap(days)

if __name__ == "__main__":
    main()
