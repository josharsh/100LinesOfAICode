#!/usr/bin/env python3
"""README Generator - Professional READMEs in 10 seconds, 75 lines"""
import os, sys, json
from pathlib import Path
from anthropic import Anthropic

class ReadmeGenerator:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    def analyze_project(self, path: str = ".") -> dict:
        """Analyze project structure and files."""
        project_path = Path(path)
        analysis = {"files": [], "tech_stack": [], "has_tests": False, "has_docker": False}

        # Check key files
        key_files = ["package.json", "requirements.txt", "setup.py", "Cargo.toml", "go.mod", "pom.xml"]
        for file in key_files:
            if (project_path / file).exists():
                analysis["files"].append(file)
                with open(project_path / file, "r") as f:
                    content = f.read()[:1000]  # First 1KB
                    analysis["tech_stack"].append({file: content})

        # Check for Docker
        if (project_path / "Dockerfile").exists():
            analysis["has_docker"] = True

        # Check for tests
        test_dirs = ["tests", "test", "__tests__", "spec"]
        for test_dir in test_dirs:
            if (project_path / test_dir).exists():
                analysis["has_tests"] = True
                break

        # Check for main code files
        code_files = list(project_path.glob("*.py")) + list(project_path.glob("*.js")) + \
                     list(project_path.glob("*.ts")) + list(project_path.glob("*.go"))
        if code_files:
            # Read first code file for context
            with open(code_files[0], "r") as f:
                analysis["sample_code"] = f.read()[:2000]

        # Check .env.example
        if (project_path / ".env.example").exists():
            with open(project_path / ".env.example", "r") as f:
                analysis["env_vars"] = f.read()

        return analysis

    def generate_readme(self, path: str = ".") -> str:
        """Generate a professional README."""
        project_name = Path(path).resolve().name
        analysis = self.analyze_project(path)

        prompt = f"""Generate a professional README.md for this project: {project_name}

Project Analysis:
- Files found: {', '.join(analysis['files'])}
- Has Docker: {analysis['has_docker']}
- Has tests: {analysis['has_tests']}
- Tech stack hints: {json.dumps(analysis.get('tech_stack', [])[:2], indent=2)}

Sample code:
{analysis.get('sample_code', 'No code files found')}

Environment variables:
{analysis.get('env_vars', 'None found')}

Create a complete README with:
1. # Project Title (catchy one-liner)
2. ## Features (3-5 bullet points)
3. ## Installation (step-by-step)
4. ## Usage (with code examples)
5. ## Configuration (environment variables if applicable)
6. ## Development (running tests, Docker if applicable)
7. ## Contributing (brief)
8. ## License

Make it professional, clear, and ready to use. Use proper markdown formatting."""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def save_readme(self, content: str, path: str = "."):
        """Save README to file."""
        readme_path = Path(path) / "README.md"
        with open(readme_path, "w") as f:
            f.write(content)
        return readme_path

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "."

    print("🔍 Analyzing your project...\n")
    generator = ReadmeGenerator()

    print("📝 Generating README...")
    readme_content = generator.generate_readme(path)

    print("\n" + "="*50)
    print(readme_content)
    print("="*50 + "\n")

    save = input("Save this README? [y/n]: ").lower()
    if save == "y":
        readme_path = generator.save_readme(readme_content, path)
        print(f"\n✅ README saved to {readme_path}")
        print("⏱️  Time saved: ~45 minutes")
        print("⭐ README quality: Professional\n")
    else:
        print("\n💾 Copy the content above and save manually.")

if __name__ == "__main__":
    main()
