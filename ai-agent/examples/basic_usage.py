"""Example: Using the AI Agent programmatically"""
import sys
sys.path.append('..')
from agent import Agent

# Initialize agent
agent = Agent()

# Example 1: Simple file operation
print("Example 1: File Analysis")
result = agent.run("count how many Python files are in the parent directory")
print(f"Result: {result}\n")

# Example 2: Code analysis
print("Example 2: Code Search")
result = agent.run("find any TODO or FIXME comments in the codebase")
print(f"Result: {result}\n")

# Example 3: Data processing
print("Example 3: Generate Report")
result = agent.run("create a file called stats.txt with total line count of all Python files")
print(f"Result: {result}")
