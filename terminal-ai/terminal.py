#!/usr/bin/env python3
"""Terminal AI - Natural language to shell commands in <100 lines."""
import os, sys, subprocess, argparse, platform
from anthropic import Anthropic

DANGEROUS_COMMANDS = ["rm -rf /", ":(){ :|:& };:", "dd if=/dev/zero", "mkfs", "fork bomb", "> /dev/sda"]

class TerminalAI:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.os_info = f"{platform.system()} {platform.release()}"

    def generate_command(self, description: str, safe_mode: bool = True) -> dict:
        """Generate shell command from natural language."""
        prompt = f"""Convert this request to a shell command:

"{description}"

System: {self.os_info}
Current directory: {os.getcwd()}

Requirements:
1. Provide ONLY the exact command (no explanation before it)
2. Use proper flags and syntax
3. Be safe - no destructive operations unless explicitly requested
4. Explain what the command does AFTER the command
5. Warn about any risks

Format:
COMMAND: <the exact command>
EXPLANATION: <what it does>
RISKS: <any warnings or "None">
"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.content[0].text
        lines = content.split('\n')

        command, explanation, risks = "", "", "None"
        for line in lines:
            if line.startswith("COMMAND:"):
                command = line.replace("COMMAND:", "").strip()
            elif line.startswith("EXPLANATION:"):
                explanation = line.replace("EXPLANATION:", "").strip()
            elif line.startswith("RISKS:"):
                risks = line.replace("RISKS:", "").strip()

        if not command:
            command = lines[0].strip()
            explanation = " ".join(lines[1:]).strip()

        is_dangerous = any(dangerous in command.lower() for dangerous in DANGEROUS_COMMANDS)
        if safe_mode and is_dangerous:
            return {"error": "⛔ Dangerous command blocked by safe mode", "command": command, "risks": "CRITICAL"}

        return {"command": command, "explanation": explanation, "risks": risks}

    def execute_command(self, command: str, confirm: bool = True) -> dict:
        """Execute a shell command with optional confirmation."""
        if confirm:
            response = input(f"\n❓ Execute: {command}\n   Proceed? [y/N]: ")
            if response.lower() not in ['y', 'yes']:
                return {"cancelled": True}

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}
        except subprocess.TimeoutExpired:
            return {"error": "Command timed out (30s limit)"}
        except Exception as e:
            return {"error": str(e)}

    def interactive_mode(self):
        """Start interactive terminal AI session."""
        print("🤖 Terminal AI - Type your requests in natural language")
        print("   Commands: 'exit', 'quit' to leave | 'safe on/off' to toggle safe mode")
        print(f"   Safe mode: ON | OS: {self.os_info}\n")

        safe_mode = True

        while True:
            try:
                user_input = input("💭 What do you want to do? ").strip()

                if user_input.lower() in ['exit', 'quit']:
                    print("👋 Goodbye!")
                    break

                if user_input.lower() == 'safe off':
                    safe_mode = False
                    print("⚠️  Safe mode: OFF (use caution!)")
                    continue
                elif user_input.lower() == 'safe on':
                    safe_mode = True
                    print("✅ Safe mode: ON")
                    continue

                result = self.generate_command(user_input, safe_mode)

                if "error" in result:
                    print(f"\n{result['error']}\n")
                    continue

                print(f"\n💻 Command: {result['command']}")
                print(f"📖 Explanation: {result['explanation']}")
                if result['risks'] != "None":
                    print(f"⚠️  Risks: {result['risks']}")

                exec_result = self.execute_command(result['command'])

                if exec_result.get("cancelled"):
                    print("❌ Cancelled\n")
                elif "error" in exec_result:
                    print(f"❌ Error: {exec_result['error']}\n")
                else:
                    if exec_result['stdout']:
                        print(f"\n📤 Output:\n{exec_result['stdout']}")
                    if exec_result['stderr']:
                        print(f"\n⚠️  Errors:\n{exec_result['stderr']}")
                    print()

            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}\n")

def main():
    parser = argparse.ArgumentParser(description="Terminal AI - Natural language shell commands")
    parser.add_argument("request", nargs="*", help="Your request in natural language")
    parser.add_argument("--execute", action="store_true", help="Execute without confirmation")
    parser.add_argument("--unsafe", action="store_true", help="Disable safe mode")
    args = parser.parse_args()

    ai = TerminalAI()

    if args.request:
        request = " ".join(args.request)
        result = ai.generate_command(request, safe_mode=not args.unsafe)

        if "error" in result:
            print(result['error'])
            sys.exit(1)

        print(f"\n💻 Command: {result['command']}")
        print(f"📖 {result['explanation']}")
        if result['risks'] != "None":
            print(f"⚠️  {result['risks']}\n")

        if args.execute:
            exec_result = ai.execute_command(result['command'], confirm=False)
            if exec_result.get('stdout'):
                print(exec_result['stdout'])
    else:
        ai.interactive_mode()

if __name__ == "__main__":
    main()
