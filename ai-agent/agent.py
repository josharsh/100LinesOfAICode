#!/usr/bin/env python3
"""Autonomous AI Agent - Executes tasks with self-correction in <100 lines."""
import os, json, subprocess, sys
from pathlib import Path
from anthropic import Anthropic

class Agent:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.conversation = []
        self.tools = [
            {"name": "execute_code", "description": "Execute Python code safely",
             "input_schema": {"type": "object", "properties": {"code": {"type": "string"}}, "required": ["code"]}},
            {"name": "read_file", "description": "Read file contents",
             "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
            {"name": "write_file", "description": "Write content to file",
             "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}},
            {"name": "list_files", "description": "List files in directory",
             "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
            {"name": "search_code", "description": "Search for pattern in files",
             "input_schema": {"type": "object", "properties": {"pattern": {"type": "string"}, "path": {"type": "string"}}, "required": ["pattern"]}},
        ]

    def execute_code(self, code: str) -> str:
        try: return subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=10).stdout or "✓ Code executed"
        except Exception as e: return f"Error: {e}"

    def read_file(self, path: str) -> str:
        try: return Path(path).read_text()
        except Exception as e: return f"Error: {e}"

    def write_file(self, path: str, content: str) -> str:
        try: Path(path).write_text(content); return f"✓ Written to {path}"
        except Exception as e: return f"Error: {e}"

    def list_files(self, path: str) -> str:
        try: return "\n".join(str(p) for p in Path(path).rglob("*") if p.is_file())
        except Exception as e: return f"Error: {e}"

    def search_code(self, pattern: str, path: str = ".") -> str:
        try: return subprocess.run(["grep", "-r", pattern, path], capture_output=True, text=True).stdout or "No matches"
        except Exception as e: return f"Error: {e}"

    def call_tool(self, name: str, args: dict) -> str:
        tools_map = {"execute_code": self.execute_code, "read_file": self.read_file,
                     "write_file": self.write_file, "list_files": self.list_files, "search_code": self.search_code}
        return tools_map[name](**args) if name in tools_map else "Unknown tool"

    def run(self, task: str, max_iterations: int = 10) -> str:
        self.conversation = [{"role": "user", "content": f"Task: {task}\n\nComplete this task using available tools. Be concise and efficient."}]

        for i in range(max_iterations):
            response = self.client.messages.create(model="claude-3-5-sonnet-20241022", max_tokens=4096,
                                                   tools=self.tools, messages=self.conversation)

            self.conversation.append({"role": "assistant", "content": response.content})

            if response.stop_reason == "end_turn":
                result = next((block.text for block in response.content if hasattr(block, "text")), "Task completed")
                print(f"\n✓ Agent completed task in {i+1} iterations")
                return result

            if response.stop_reason == "tool_use":
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        print(f"→ Using tool: {block.name}")
                        result = self.call_tool(block.name, block.input)
                        print(f"  Result: {result[:100]}{'...' if len(result) > 100 else ''}")
                        tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": result})

                self.conversation.append({"role": "user", "content": tool_results})

        return "⚠ Max iterations reached"

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py \"<your task>\"")
        print("\nExamples:")
        print('  python agent.py "find all Python files in current dir"')
        print('  python agent.py "create a hello.txt file with greeting"')
        print('  python agent.py "count lines of code in all .py files"')
        sys.exit(1)

    agent = Agent()
    print(f"🤖 Agent starting task: {sys.argv[1]}\n")
    result = agent.run(sys.argv[1])
    print(f"\n📊 Final Result:\n{result}")

if __name__ == "__main__":
    main()
