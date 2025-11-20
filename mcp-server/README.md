# 🔌 MCP Server

**Minimal MCP implementation** - Connect AI to your data with the new Model Context Protocol.

## What Is MCP?

[Model Context Protocol](https://modelcontextprotocol.io) (late 2024) - open standard for AI to access data. Like USB-C for AI.

## Quick Start

```bash
python server.py

# Test
echo '{"jsonrpc":"2.0","id":1,"method":"initialize"}' | python server.py
```

### Connect to Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

## Build Custom Server

```python
from server import MCPServer

server = MCPServer("my-server")

# Register resource (data AI can read)
server.register_resource(
    uri="doc://welcome",
    content="Welcome!",
    mime_type="text/plain"
)

# Register tool (function AI can call)
def calculate(x: int, y: int) -> int:
    return x + y

server.register_tool("calculate", "Add numbers", calculate, {...})
server.run_stdio()
```

## Use Cases

- **Docs Server**: Expose codebase documentation
- **Tools Server**: Let AI use internal tools
- **Database Server**: Query your databases
- **API Server**: Connect to external APIs

**87 lines. Zero dependencies.**
