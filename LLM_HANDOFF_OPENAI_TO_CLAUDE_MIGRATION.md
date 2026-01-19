# LLM Handoff Document: OpenAI to Claude Migration

## Project Context

**Client:** DocuSign
**Workshop:** Generative AI for Developers (2-day training)
**Reason for Migration:** Client's security team blocked ChatGPT/OpenAI access during SF session
**Target:** Switch all OpenAI-dependent materials to Anthropic Claude

---

## Migration Status Summary

| Component | Status | Notes |
|-----------|--------|-------|
| HKS_LAB Notebook (7 scenarios) | ✅ COMPLETE | New file created |
| Zero-Shot/Few-Shot Notebook | ❌ PENDING | Similar pattern to HKS_LAB |
| RAG Notebook | ❌ PENDING | Uses HTTP requests, straightforward |
| Chatbot Notebook | ❌ PENDING | LangChain has Claude support |
| Snowflake Cortex Demos | ✅ NO CHANGES NEEDED | Claude fully supported in Snowflake |
| AI Agent Projects | ✅ NO CHANGES NEEDED | Already uses Groq/Llama |
| MCP Server | ✅ NO CHANGES NEEDED | No LLM dependency |
| Documentation | ❌ PENDING | Find/replace "ChatGPT" → "Claude" |

---

## Completed Work

### 1. HKS_LAB_Prompt_Engineering Notebook

**Original File:**
`LAB EXERCISES/HKS_LAB_Prompt_Engineering_openai_gpt_3_for_diverse_language_tasks.ipynb`

**New File (Claude version):**
`LAB EXERCISES/HKS_LAB_Prompt_Engineering_claude_for_diverse_language_tasks.ipynb`

**Migration Guide:**
`LAB EXERCISES/MIGRATION_GUIDE_HKS_LAB.md`

**What was converted:**
- Dependencies: `openai==0.28.0` → `anthropic`
- API config: Azure OpenAI → Anthropic direct API
- All 7 prompt engineering scenarios updated
- Response handling: `results["choices"][0]["message"]["content"]` → `response.content[0].text`
- System messages moved to separate `system` parameter

---

## Remaining Work

### High Priority: 3 Notebooks to Convert

#### 1. Zero_Shot,_Few_Shot,_and_Chain_of_Thought_Prompting_with_Azure_OpenAI.ipynb

**Location:** `LAB EXERCISES/Zero_Shot,_Few_Shot,_and_Chain_of_Thought_Prompting_with_Azure_OpenAI.ipynb`

**Current Implementation:**
```python
import openai
openai.api_type = "azure"
openai.api_key = "..."
openai.api_base = "https://hks-demo-new.cognitiveservices.azure.com/"

response = openai.ChatCompletion.create(
    engine="kedardeploy",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=150
)
result = response.choices[0].message["content"]
```

**Required Changes:**
```python
import anthropic
client = anthropic.Anthropic(api_key="...")

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=150
)
result = response.content[0].text
```

**Effort:** ~1-2 hours

---

#### 2. Retrieval_Augmented_Generation_(RAG)_model_using_Azure_OpenAI.ipynb

**Location:** `LAB EXERCISES/Retrieval_Augmented_Generation_(RAG)_model_using_Azure_OpenAI.ipynb`

**Current Implementation:**
- Uses `requests` library for HTTP calls to Azure OpenAI
- Uses FAISS + TF-IDF for vector search (NO CHANGES NEEDED for this part)
- RAG pipeline calls Azure OpenAI for generation

**Required Changes:**
```python
# OLD - Azure OpenAI HTTP
url = f"{endpoint}openai/deployments/{deployment_name}/chat/completions?api-version=2024-10-01-preview"
headers = {"Content-Type": "application/json", "api-key": api_key}
payload = {
    "messages": [...],
    "max_tokens": 100
}
response = requests.post(url, headers=headers, json=payload)
result = response.json()['choices'][0]['message']['content']

# NEW - Anthropic HTTP (or use SDK)
url = "https://api.anthropic.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01"
}
payload = {
    "model": "claude-3-5-sonnet-20241022",
    "messages": [...],
    "max_tokens": 100
}
response = requests.post(url, headers=headers, json=payload)
result = response.json()['content'][0]['text']
```

**Effort:** ~2 hours

---

#### 3. Chatbot_with_OpenAI.ipynb

**Location:** `LAB EXERCISES/Chatbot_with_OpenAI.ipynb`

**Current Implementation:**
- Uses `langchain` + `openai==0.28`
- Azure OpenAI for chat completions
- Simple chatbot for sourdough baking assistant

**Required Changes:**
```python
# OLD
from langchain import OpenAI
openai.api_type = "azure"
response = openai.ChatCompletion.create(engine=deployment, messages=[...])

# NEW - Option A: Direct Anthropic SDK
import anthropic
client = anthropic.Anthropic(api_key=api_key)
response = client.messages.create(model="claude-3-5-sonnet-20241022", messages=[...])

# NEW - Option B: LangChain with Claude
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", anthropic_api_key=api_key)
```

**Effort:** ~1-2 hours

---

### Low Priority: Documentation Updates

**Files to update:**
- `WORKSHOP_SCHEDULE.md` - Replace "ChatGPT" with "Claude"
- `WORKSHOP_SCHEDULE_V2.md` - Replace "ChatGPT" with "Claude"

**Changes needed:**
- Find/replace: "ChatGPT" → "Claude"
- Find/replace: "OpenAI" → "Anthropic" (where appropriate)
- Update notebook references in schedule
- Update setup instructions (Anthropic API key instead of Azure)

**Effort:** ~30 minutes

---

## Key Technical Reference

### Claude API Pattern

```python
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",  # or claude-3-opus, claude-3-haiku
    max_tokens=1024,
    temperature=0.7,
    system="You are a helpful assistant.",  # System message is SEPARATE
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ]
)

# Extract response
output = response.content[0].text
```

### Claude Models Available
- `claude-3-5-sonnet-20241022` - **Recommended** (best balance of speed/capability)
- `claude-3-opus-20240229` - Most capable, slower
- `claude-3-haiku-20240307` - Fastest, lowest cost

### Key Differences from OpenAI
1. **System message** is a separate parameter, not in messages array
2. **Response structure:** `response.content[0].text` not `response.choices[0].message.content`
3. **No `engine` parameter** - use `model` directly
4. **No Azure config** - direct API with single API key

---

## Snowflake Cortex (NO CODE CHANGES NEEDED)

Snowflake has a [$200M partnership with Anthropic](https://www.snowflake.com/en/news/press-releases/snowflake-and-anthropic-announce-200-million-partnership-to-bring-agentic-ai-to-global-enterprises/). Claude is fully supported.

**Only change needed in Snowflake demos:**
```sql
-- OLD
SELECT SNOWFLAKE.CORTEX.COMPLETE('gpt-35-turbo', 'Your prompt');

-- NEW
SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', 'Your prompt');
```

Supported Claude models in Snowflake Cortex:
- `claude-4-opus`
- `claude-4-sonnet`
- `claude-3-7-sonnet`
- `claude-3-5-sonnet`

---

## Files NOT Requiring Changes

These files are already provider-agnostic or use non-OpenAI providers:

| File | Reason |
|------|--------|
| `PROJECTS/MCP-SERVER/main.py` | No LLM dependency |
| `PROJECTS/MCP-SERVER/pyproject.toml` | Only MCP dependency |
| `PROJECTS/AI-AGENT/2_finance_agent_llama.py` | Uses Groq (Llama) |
| `PROJECT WORK/AI-AGENT/docusign-agent.py` | Uses Groq (Llama) |
| `PROJECT WORK/AI-AGENT/finance_agent_llama_default.py` | Uses Groq (Llama) |
| `DocuSign_Agreement_AI_Agent.ipynb` | Uses Groq (Llama) |

---

## Testing Checklist

Before deploying to workshop:

### HKS_LAB Notebook (DONE)
- [ ] QnA scenario works
- [ ] YAML generation works
- [ ] French response works
- [ ] Text summarization works
- [ ] Chinese summarization works
- [ ] Text classification works
- [ ] Product naming works
- [ ] Translation works
- [ ] JSON parsing works
- [ ] NLP to SQL works

### Zero-Shot Notebook (TODO)
- [ ] Zero-shot prompting works
- [ ] Few-shot prompting works
- [ ] Chain-of-thought prompting works

### RAG Notebook (TODO)
- [ ] FAISS vector search works (should be unchanged)
- [ ] Claude generation works
- [ ] End-to-end RAG pipeline works

### Chatbot Notebook (TODO)
- [ ] Chat completion works
- [ ] Multi-turn conversation works
- [ ] Sourdough assistant responds correctly

### Snowflake Demos (TEST ONLY)
- [ ] SUMMARIZE function works with Claude model
- [ ] SENTIMENT function works with Claude model
- [ ] RAG in Snowflake Cortex works with Claude

---

## Environment Setup for Next LLM

### Required API Key
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

Get key from: https://console.anthropic.com/

### Dependencies
```bash
pip install anthropic python-dotenv
```

### Repository Structure
```
Generative-AI-for-Developers-DocuSign/
├── LAB EXERCISES/
│   ├── HKS_LAB_Prompt_Engineering_claude_for_diverse_language_tasks.ipynb  # ✅ NEW
│   ├── HKS_LAB_Prompt_Engineering_openai_gpt_3_for_diverse_language_tasks.ipynb  # OLD
│   ├── MIGRATION_GUIDE_HKS_LAB.md  # ✅ NEW
│   ├── Zero_Shot,_Few_Shot,_and_Chain_of_Thought_Prompting_with_Azure_OpenAI.ipynb  # TODO
│   ├── Retrieval_Augmented_Generation_(RAG)_model_using_Azure_OpenAI.ipynb  # TODO
│   └── Chatbot_with_OpenAI.ipynb  # TODO
├── PROJECTS/
│   ├── AI-AGENT/  # ✅ No changes needed (uses Groq)
│   └── MCP-SERVER/  # ✅ No changes needed (no LLM)
├── WORKSHOP_SCHEDULE.md  # TODO: Update references
├── WORKSHOP_SCHEDULE_V2.md  # TODO: Update references
└── LLM_HANDOFF_OPENAI_TO_CLAUDE_MIGRATION.md  # ✅ THIS FILE
```

---

## Estimated Remaining Effort

| Task | Time Estimate |
|------|---------------|
| Zero-Shot Notebook | 1-2 hours |
| RAG Notebook | 2 hours |
| Chatbot Notebook | 1-2 hours |
| Documentation updates | 30 minutes |
| Testing all notebooks | 1-2 hours |
| **Total** | **6-9 hours** |

---

## Contact & Resources

- **Anthropic Documentation:** https://docs.anthropic.com/
- **Claude API Reference:** https://docs.anthropic.com/en/api/messages
- **Snowflake + Claude:** https://www.snowflake.com/en/developers/guides/getting-started-with-anthropic-on-snowflake-cortex/

---

*Document created: January 2026*
*Last updated: January 2026*
*Migration initiated due to: DocuSign security team blocking ChatGPT access*
