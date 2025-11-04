#!/usr/bin/env python3
"""Minimal MCP Server - Model Context Protocol implementation in <100 lines."""
import json, sys
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List

class MCPServer:
    """Minimal MCP server implementing core protocol features."""

    def __init__(self, name: str = "minimal-mcp", version: str = "1.0.0"):
        self.name, self.version = name, version
        self.resources: Dict[str, Any] = {}
        self.tools: Dict[str, callable] = {}

    def register_resource(self, uri: str, content: str, mime_type: str = "text/plain"):
        """Register a resource that can be accessed by AI."""
        self.resources[uri] = {"uri": uri, "mimeType": mime_type, "text": content}

    def register_tool(self, name: str, description: str, func: callable, schema: Dict = None):
        """Register a tool that can be called by AI."""
        self.tools[name] = {"name": name, "description": description, "func": func,
                            "inputSchema": schema or {"type": "object", "properties": {}}}

    def handle_request(self, request: Dict) -> Dict:
        """Handle incoming MCP request."""
        method = request.get("method", "")

        if method == "initialize":
            return {"protocolVersion": "2024-11-05", "serverInfo": {"name": self.name, "version": self.version},
                    "capabilities": {"resources": {"listChanged": True}, "tools": {"listChanged": True}}}

        elif method == "resources/list":
            return {"resources": [{"uri": r["uri"], "mimeType": r["mimeType"], "name": r["uri"].split("/")[-1]}
                                  for r in self.resources.values()]}

        elif method == "resources/read":
            uri = request.get("params", {}).get("uri")
            return {"contents": [self.resources[uri]]} if uri in self.resources else {"error": "Resource not found"}

        elif method == "tools/list":
            return {"tools": [{k: v for k, v in t.items() if k != "func"} for t in self.tools.values()]}

        elif method == "tools/call":
            name = request.get("params", {}).get("name")
            args = request.get("params", {}).get("arguments", {})
            if name in self.tools:
                try: result = self.tools[name]["func"](**args)
                except Exception as e: return {"error": str(e), "isError": True}
                return {"content": [{"type": "text", "text": str(result)}]}
            return {"error": f"Tool '{name}' not found", "isError": True}

        elif method == "ping":
            return {}

        return {"error": f"Unknown method: {method}"}

    def run_stdio(self):
        """Run server using stdio transport (standard for MCP)."""
        for line in sys.stdin:
            try:
                request = json.loads(line.strip())
                response = {"jsonrpc": "2.0", "id": request.get("id")}
                response["result"] = self.handle_request(request)
                print(json.dumps(response), flush=True)
            except Exception as e:
                error_resp = {"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}
                print(json.dumps(error_resp), flush=True)

# Example: File System MCP Server
def create_filesystem_server(root_path: str = "."):
    """Create an MCP server that exposes filesystem as resources."""
    server = MCPServer(name="filesystem-mcp", version="1.0.0")
    root = Path(root_path)

    # Register all text files as resources
    for file_path in root.rglob("*.txt"):
        try: server.register_resource(f"file://{file_path}", file_path.read_text(), "text/plain")
        except: pass

    for file_path in root.rglob("*.md"):
        try: server.register_resource(f"file://{file_path}", file_path.read_text(), "text/markdown")
        except: pass

    # Register tools
    server.register_tool("get_file_info", "Get file metadata", lambda path: {
        "size": Path(path).stat().st_size, "modified": datetime.fromtimestamp(Path(path).stat().st_mtime).isoformat()
    }, {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]})

    server.register_tool("list_directory", "List files in directory", lambda path=".": [
        str(p) for p in Path(path).iterdir()
    ], {"type": "object", "properties": {"path": {"type": "string", "default": "."}}})

    server.register_tool("search_content", "Search for text in files", lambda query, pattern="*.txt": [
        str(p) for p in Path(".").rglob(pattern) if query.lower() in p.read_text().lower()
    ], {"type": "object", "properties": {"query": {"type": "string"}, "pattern": {"type": "string"}}, "required": ["query"]})

    return server

if __name__ == "__main__":
    server = create_filesystem_server()
    server.run_stdio()
