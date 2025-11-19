"""Example: Custom MCP Server with multiple data sources"""
import sys
sys.path.append('..')
from server import MCPServer
from datetime import datetime

# Create server
server = MCPServer(name="example-mcp", version="1.0.0")

# Add resources (static data)
server.register_resource(
    uri="doc://welcome",
    content="Welcome! This server provides project information.",
    mime_type="text/plain"
)

server.register_resource(
    uri="doc://readme",
    content="# Project Guide\n\nThis is an example MCP server.",
    mime_type="text/markdown"
)

# Add tools (dynamic functions)
def get_time() -> str:
    return datetime.now().isoformat()

server.register_tool(
    name="current_time",
    description="Get current server time",
    func=get_time
)

def calculate(operation: str, a: float, b: float) -> float:
    ops = {"+": a + b, "-": a - b, "*": a * b, "/": a / b if b != 0 else 0}
    return ops.get(operation, 0)

server.register_tool(
    name="calculate",
    description="Perform basic math operations",
    func=calculate,
    schema={
        "type": "object",
        "properties": {
            "operation": {"type": "string", "enum": ["+", "-", "*", "/"]},
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "required": ["operation", "a", "b"]
    }
)

# Run server
if __name__ == "__main__":
    server.run_stdio()
