# Projects

Day 2 hands-on projects demonstrating two approaches to connecting LLMs with external tools.

## Projects

### AI-AGENT/
Build a finance assistant agent using the `phi` framework and Groq. The agent autonomously calls YFinance tools to fetch stock data, analyst recommendations, and company fundamentals.

**Run it:**
```bash
cd AI-AGENT
python 2_finance_agent_llama.py
```

### MCP-SERVER/
Build a Model Context Protocol (MCP) server for leave management that integrates with Claude Desktop. Demonstrates the MCP standard for connecting LLMs to enterprise tools.

**Run it:**
```bash
cd MCP-SERVER
uv run mcp install main.py
# Then restart Claude Desktop
```

## Comparison

| Aspect | AI Agent (phi) | MCP Server |
|--------|----------------|------------|
| Runtime | Agent calls tools directly | Client requests tools from server |
| Integration | Framework-specific | Protocol-based, tool-agnostic |
| Use Case | Standalone applications | Connecting LLMs to enterprise systems |
| Complexity | Simpler setup | More infrastructure |

See each project's README for detailed setup and instructions.
