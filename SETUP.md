# Workshop Environment Setup

This guide walks you through setting up your Python environment for the **Generative AI for Developers** workshop. One environment covers all labs and projects across Days 1-2.

## Prerequisites

- Python 3.10 or higher
- API keys (see below)

## Step 1: Create Virtual Environment

From this directory (`Generative-AI-for-Developers-DocuSign/`):

```bash
python -m venv .venv
```

Activate it:
```bash
# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs everything needed for:
- Day 1 prompt engineering notebooks
- Day 2 RAG and chatbot notebooks
- Day 2 MCP Server project
- Day 2 AI Agent project

## Step 3: Configure API Keys

Create a `.env` file in this directory:

```
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

**Where to get keys:**
- OpenAI: https://platform.openai.com/api-keys
- Groq (free): https://console.groq.com

## Step 4: Verify Installation

```bash
python -c "import openai; print('OpenAI OK')"
python -c "import faiss; print('FAISS OK')"
python -c "from phi.agent import Agent; print('Phidata OK')"
```

## What's Covered

| Day | Lab/Project | Folder |
|-----|-------------|--------|
| 1 | Zero-Shot, Few-Shot, Chain-of-Thought | `NEW LABS/` |
| 1 | Prompt Engineering | `NEW LABS/` |
| 2 | RAG with OpenAI | `NEW LABS/` |
| 2 | Chatbot with OpenAI | `NEW LABS/` |
| 2 | MCP Server | `PROJECTS/MCP-SERVER/` |
| 2 | AI Agent | `PROJECTS/AI-AGENT/` |

## Troubleshooting

**"No module named 'phi'"**
```bash
pip install phidata
```

**"inspect.getargspec" error**
You have a conflicting `phi` package:
```bash
pip uninstall phi -y && pip install phidata
```

**Jupyter kernel doesn't see packages**
Register the venv as a Jupyter kernel:
```bash
pip install ipykernel
python -m ipykernel install --user --name=genai-workshop
```
Then select "genai-workshop" kernel in Jupyter.

**MCP Server not appearing in Claude Desktop**
1. Ensure you ran `uv run mcp install main.py` from `PROJECTS/MCP-SERVER/`
2. Restart Claude Desktop completely (kill from Task Manager if needed)

## Running Labs

**Jupyter Notebooks (NEW LABS/):**
```bash
jupyter notebook
```
Navigate to `NEW LABS/` and open any notebook.

**AI Agent:**
```bash
cd PROJECTS/AI-AGENT
python 2_finance_agent_llama.py
```

**MCP Server:**
See `PROJECTS/MCP-SERVER/README.md` for Claude Desktop integration steps.
