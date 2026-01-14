# Build Your First MCP Server: Leave Management
This AI tool helps an HR with leave management related tasks. The codebase here 
is for MCP server that interacts with mock leave database and responds to MCP client queries

# Setup Steps

**Prerequisites**: Complete the shared workshop environment setup first. See `SETUP.md` in the workshop root directory.

1. Install Claude Desktop
2. Install uv: `pip install uv`
3. Create project directory: `uv init my-first-mcp-server`
4. Add MCP dependency: `uv add "mcp[cli]"`
5. If you get type errors: `pip install --upgrade typer`
6. Write code in main.py for leave management server
7. Install server in Claude Desktop: `uv run mcp install main.py`
8. Kill any running Claude instance from Task Manager, then restart Claude Desktop
9. In Claude Desktop, you will now see tools from this server

@All rights reserved. Codebasics Inc. LearnerX Pvt Ltd. 
