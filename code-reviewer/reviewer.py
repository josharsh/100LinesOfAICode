#!/usr/bin/env python3
"""AI Code Reviewer - Automated code review in <100 lines."""
import os, sys, argparse, subprocess
from pathlib import Path
from anthropic import Anthropic

REVIEW_PROMPT = """Review this code for:
1. **Bugs & Errors**: Logic errors, edge cases, potential crashes
2. **Security**: Vulnerabilities, injection risks, unsafe operations
3. **Performance**: Inefficiencies, memory leaks, optimization opportunities
4. **Best Practices**: Code style, naming, design patterns
5. **Maintainability**: Readability, documentation, complexity

Provide:
- ✅ What's good
- ⚠️ Issues found (severity: 🔴 critical, 🟡 warning, 🔵 info)
- 💡 Specific suggestions with code examples

Code to review:
"""

class CodeReviewer:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def review_code(self, code: str, filename: str = "code") -> str:
        """Review code and return detailed feedback."""
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"{REVIEW_PROMPT}\n\n```{Path(filename).suffix[1:]}\n{code}\n```"}]
        )
        return response.content[0].text

    def review_file(self, filepath: str) -> dict:
        """Review a single file."""
        path = Path(filepath)
        if not path.exists(): return {"error": f"File not found: {filepath}"}
        code = path.read_text()
        return {"file": filepath, "review": self.review_code(code, filepath), "lines": len(code.splitlines())}

    def review_diff(self, diff: str) -> str:
        """Review git diff changes."""
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"Review these code changes:\n\n```diff\n{diff}\n```\n\nFocus on changed lines. Identify issues and suggest improvements."}]
        )
        return response.content[0].text

    def review_pr(self, pr_number: int = None, repo: str = None) -> dict:
        """Review GitHub PR (requires git and gh CLI)."""
        try:
            if not repo:
                repo = subprocess.run(["git", "config", "--get", "remote.origin.url"], capture_output=True, text=True).stdout.strip()
                repo = repo.replace("git@github.com:", "").replace("https://github.com/", "").replace(".git", "")

            diff = subprocess.run(["git", "diff", f"origin/main...HEAD"], capture_output=True, text=True).stdout if not pr_number else \
                   subprocess.run(["gh", "pr", "diff", str(pr_number)], capture_output=True, text=True).stdout

            return {"pr": pr_number or "current", "repo": repo, "review": self.review_diff(diff)}
        except Exception as e:
            return {"error": str(e)}

    def review_directory(self, path: str, extensions: list = [".py", ".js", ".ts", ".go", ".java"]) -> list:
        """Review all code files in directory."""
        results = []
        for ext in extensions:
            for file in Path(path).rglob(f"*{ext}"):
                print(f"Reviewing {file}...")
                results.append(self.review_file(str(file)))
        return results

def main():
    parser = argparse.ArgumentParser(description="AI-powered code reviewer")
    parser.add_argument("--file", help="Review a single file")
    parser.add_argument("--pr", type=int, help="Review GitHub PR number")
    parser.add_argument("--diff", action="store_true", help="Review current git diff")
    parser.add_argument("--dir", help="Review all files in directory")
    parser.add_argument("--output", help="Save review to file")
    args = parser.parse_args()

    reviewer = CodeReviewer()

    if args.file:
        result = reviewer.review_file(args.file)
        output = f"📝 Review of {result['file']}\n{'='*60}\n{result.get('review', result.get('error'))}"

    elif args.pr:
        result = reviewer.review_pr(args.pr)
        output = f"🔍 PR Review #{result.get('pr')}\n{'='*60}\n{result.get('review', result.get('error'))}"

    elif args.diff:
        diff = subprocess.run(["git", "diff"], capture_output=True, text=True).stdout
        output = f"🔍 Diff Review\n{'='*60}\n{reviewer.review_diff(diff)}"

    elif args.dir:
        results = reviewer.review_directory(args.dir)
        output = "\n\n".join([f"📝 {r['file']}\n{'-'*60}\n{r.get('review', r.get('error'))}" for r in results])

    else:
        print("Usage: python reviewer.py [--file FILE | --pr PR | --diff | --dir DIR]")
        print("\nExamples:")
        print("  python reviewer.py --file mycode.py")
        print("  python reviewer.py --pr 123")
        print("  python reviewer.py --diff")
        print("  python reviewer.py --dir ./src")
        sys.exit(1)

    if args.output:
        Path(args.output).write_text(output)
        print(f"✓ Review saved to {args.output}")
    else:
        print(output)

if __name__ == "__main__":
    main()
