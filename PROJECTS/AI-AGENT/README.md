# Build Your First AI Agent: Finance Assistant

This project demonstrates how to build an AI agent that can autonomously use external tools to answer complex questions. The example creates a finance agent that fetches real-time stock data, analyst recommendations, and company fundamentals using the phi framework with Groq/LLaMA.

## Workshop Context

This lab is part of **Day 2: LLM Application Architecture** (1:00-2:00 PM), which covers design patterns including Agents, RAG, and MCP. AI agents represent a key paradigm for building autonomous LLM applications that can reason, plan, and execute actions using external tools.

**Related Materials:**
- `EXTRA NOTES/AI Agents – Concepts, Architecture, Examples, and Use Cases.pdf` - Comprehensive theory reference
- `PROJECTS/MCP-SERVER/` - Alternative approach using Model Context Protocol

## What This Agent Demonstrates

1. **Tool Integration** - Connects to YFinance API for real-time financial data
2. **Custom Functions** - Defines a `get_company_symbol()` helper tool the agent can call
3. **Instructions** - Guides agent behavior (use tables, how to find symbols)
4. **Streaming Output** - Real-time response generation with markdown formatting
5. **Debug Mode** - Shows tool calls as they happen for learning purposes

## Prerequisites

- Workshop environment set up (see `SETUP.md` in workshop root)
- A Groq API key (free tier available at https://console.groq.com)

## Setup Steps

**Use the shared workshop environment.** See `SETUP.md` in the workshop root directory for full instructions.

Quick start if environment is already set up:
```bash
# From workshop root
source .venv/bin/activate
cd PROJECTS/AI-AGENT
```

**Next**: Create a `.env` file in this directory (or use the one in workshop root):
```
GROQ_API_KEY=your_groq_api_key_here
```

Then run the agent:
```bash
python 2_finance_agent_llama.py
```

## Expected Output

The agent will:
1. Receive the prompt asking to compare TSLA and MSFT
2. Call the YFinance tools to fetch stock prices, analyst recommendations, and fundamentals
3. Display the data in formatted tables
4. Stream the response in real-time

You'll see tool calls displayed (thanks to `show_tool_calls=True`) showing the agent's reasoning process.

## Key Code Concepts

```python
# Define a custom tool the agent can use
def get_company_symbol(company: str) -> str:
    """Agent calls this to look up stock symbols by company name."""
    symbols = {"Tesla": "TSLA", "Apple": "AAPL", ...}
    return symbols.get(company, "Unknown")

# Create the agent with model, tools, and instructions
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(...), get_company_symbol],
    instructions=["Use tables to display data.", ...],
)

# Run the agent with a user prompt
agent.print_response("Your question here", stream=True)
```

## Exercises to Try

1. **Add a new tool**: Create a function that calculates percentage change between two prices
2. **Modify instructions**: Add an instruction to always include a risk disclaimer
3. **Change the model**: Try `llama-3.1-8b-instant` for faster (but less capable) responses
4. **New query**: Ask the agent to compare different stocks or sectors

## How This Differs from MCP

| Approach | AI Agent (phi) | MCP Server |
|----------|----------------|------------|
| Runtime | Agent calls tools directly | Client requests tools from server |
| Integration | Framework-specific | Protocol-based, tool-agnostic |
| Use Case | Standalone applications | Connecting LLMs to enterprise systems |
| Complexity | Simpler setup | More infrastructure |

Both approaches enable LLMs to use external tools - agents embed tool calling directly, while MCP provides a standardized protocol for tool discovery and execution.

## Troubleshooting

- **API Key Error**: Ensure your `.env` file exists and contains a valid `GROQ_API_KEY`
- **Import Error**: Run `pip install phidata` (the package name differs from the import)
- **Rate Limits**: Groq free tier has rate limits; wait a moment and retry
- **No Output**: Check that `debug_mode=True` is set to see what's happening

## Next Steps

After completing this lab:
1. Explore the **MCP Server** project (`PROJECTS/MCP-SERVER/`) for a protocol-based approach
2. Review the AI Agents PDF in `EXTRA NOTES/` for deeper architectural understanding
3. Try building a DocuSign-specific agent (Day 3 covers this in detail)

@All rights reserved. Codebasics Inc. LearnerX Pvt Ltd.
