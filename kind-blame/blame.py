#!/usr/bin/env python3
"""Git Blame But Kind - Wholesome debugging in 70 lines"""
import os, sys, subprocess, re
from anthropic import Anthropic

class KindBlame:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def get_blame_info(self, file_path: str, line_num: int = None) -> list:
        """Get git blame information for a file."""
        try:
            cmd = ["git", "blame", "-w", "--line-porcelain", file_path]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            blame_data = []
            lines = result.stdout.split("\n")
            i = 0
            while i < len(lines):
                if lines[i].startswith("author "):
                    author = lines[i].replace("author ", "")
                    date = lines[i+2].replace("author-time ", "") if i+2 < len(lines) else ""
                    # Find the code line
                    code_line = ""
                    j = i
                    while j < len(lines) and not lines[j].startswith("\t"):
                        j += 1
                    if j < len(lines):
                        code_line = lines[j].replace("\t", "")

                    blame_data.append({"author": author, "date": date, "code": code_line})
                i += 1

            return blame_data[:50]  # Limit to 50 lines for AI context
        except Exception as e:
            return [{"error": str(e)}]

    def make_it_kind(self, blame_info: list, file_path: str) -> str:
        """Transform blame into something wholesome."""
        # Prepare context
        blame_text = "\n".join([f"{b.get('author', 'Unknown')}: {b.get('code', '')}" for b in blame_info[:10]])

        prompt = f"""Transform this git blame output into something kind and encouraging.

File: {file_path}
Blame info:
{blame_text}

Create a friendly summary that:
1. Acknowledges contributors positively (use emojis ✨, ☕, 💡)
2. Frames mistakes as learning opportunities
3. Uses phrases like "had a creative idea", "we've all been there", "coffee was needed"
4. Adds encouraging comments
5. If you spot obvious bugs (like = instead of ==), gently point them out with humor

Keep it short, friendly, and wholesome. Make people feel good about their code."""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def display_kind_blame(self, file_path: str, line_num: int = None):
        """Show the kind blame output."""
        print(f"\n🌟 Kind Blame for: {file_path}\n")
        print("Analyzing with kindness...\n")

        blame_info = self.get_blame_info(file_path, line_num)

        if not blame_info or "error" in blame_info[0]:
            print("❌ Could not get blame info. Is this a git repository?")
            return

        kind_output = self.make_it_kind(blame_info, file_path)
        print(kind_output)
        print("\n💚 Remember: We're all learning, and every commit is progress!\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python blame.py <file_path> [line_number]")
        print("\nExample:")
        print("  python blame.py app.py")
        print("  python blame.py src/auth.py 42")
        sys.exit(1)

    file_path = sys.argv[1]
    line_num = int(sys.argv[2]) if len(sys.argv) > 2 else None

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    blamer = KindBlame()
    blamer.display_kind_blame(file_path, line_num)

if __name__ == "__main__":
    main()
