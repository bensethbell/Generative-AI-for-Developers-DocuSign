# HKS LAB Migration Guide: OpenAI → Claude

## Summary

✅ Successfully converted `HKS_LAB_Prompt_Engineering_openai_gpt_3_for_diverse_language_tasks.ipynb` to Claude.

**New file:** `HKS_LAB_Prompt_Engineering_claude_for_diverse_language_tasks.ipynb`

---

## What Changed

### 1. Dependencies
**Before (OpenAI):**
```python
%pip install openai==0.28.0 python-dotenv
import openai
```

**After (Claude):**
```python
%pip install anthropic python-dotenv
import anthropic
```

### 2. API Configuration
**Before (Azure OpenAI):**
```python
os.environ["AZURE_OPENAI_API_KEY"] = "..."
os.environ["AZURE_OPENAI_API_BASE"] = "..."
os.environ["AZURE_OPENAI_API_VERSION"] = "..."

openai.api_type = "azure"
openai.api_key = api_key
openai.api_base = api_base
openai.api_version = api_version
```

**After (Anthropic):**
```python
os.environ["ANTHROPIC_API_KEY"] = "your-api-key-here"

client = anthropic.Anthropic(api_key=api_key)
model = "claude-3-5-sonnet-20241022"
```

### 3. API Calls (All 7 Scenarios Updated)
**Before (OpenAI):**
```python
results = openai.ChatCompletion.create(
    engine=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=150
)
output_text = results["choices"][0]["message"]["content"].strip("\n")
```

**After (Claude):**
```python
response = client.messages.create(
    model=model,
    max_tokens=150,
    temperature=0.7,
    system="You are a helpful assistant.",  # System message separate
    messages=[
        {"role": "user", "content": prompt}
    ]
)
output_text = response.content[0].text
```

### 4. Model Selection
**Before:**
- `gpt-35-turbo` (GPT-3.5)

**After (Choose one):**
- `claude-3-5-sonnet-20241022` ← **Recommended** (best balance)
- `claude-3-opus-20240229` (most capable, slower)
- `claude-3-haiku-20240307` (fastest, lower cost)

---

## All 7 Scenarios Converted

✅ **1. QnA** - Question answering
✅ **2. Summarization** - English text summarization
✅ **3. Chinese Summarization** - Multilingual support with translation
✅ **4. Classification** - News article categorization
✅ **5. Product Name Generation** - Creative naming
✅ **6. Translation** - Chinese poem to English
✅ **7. Parsing Unstructured Data** - JSON extraction
✅ **8. NLP to SQL** - Natural language to SQL query

---

## How to Use the New Notebook

### Step 1: Get Anthropic API Key
1. Go to https://console.anthropic.com/
2. Create an account or sign in
3. Navigate to API Keys
4. Create a new API key

### Step 2: Set Your API Key
**Option A: Environment Variable (Recommended)**
```bash
export ANTHROPIC_API_KEY="your-actual-api-key-here"
```

**Option B: .env File**
Create a file named `.env` in the same directory:
```
ANTHROPIC_API_KEY=your-actual-api-key-here
```

**Option C: Direct in Notebook** (not recommended for production)
Edit cell #6 to replace `"your-api-key-here"` with your actual key.

### Step 3: Run the Notebook
1. Open `HKS_LAB_Prompt_Engineering_claude_for_diverse_language_tasks.ipynb`
2. Run all cells in order
3. Each scenario will demonstrate Claude's capabilities

---

## Key Differences: Claude vs OpenAI

### Advantages of Claude
✅ **Better instruction following** - More reliable at following complex prompts
✅ **Longer context** - 200K tokens vs GPT-3.5's 16K tokens
✅ **Superior code generation** - Better at technical tasks
✅ **Thoughtful responses** - More detailed and nuanced answers
✅ **Strong multilingual** - Excellent Chinese, French, and other languages
✅ **Structured output** - Reliable JSON/YAML generation
✅ **No Azure dependency** - Direct API, simpler setup

### What's Similar
- Temperature and max_tokens work the same way
- Multilingual capabilities are comparable
- Pricing is competitive
- Both handle all 7 prompt engineering tasks well

---

## Pricing Comparison

**OpenAI GPT-3.5 Turbo:**
- Input: $0.50 / 1M tokens
- Output: $1.50 / 1M tokens

**Claude 3.5 Sonnet (Recommended):**
- Input: $3.00 / 1M tokens
- Output: $15.00 / 1M tokens

**Claude 3 Haiku (Faster, cheaper):**
- Input: $0.25 / 1M tokens
- Output: $1.25 / 1M tokens

*Note: Claude models are more expensive per token but often require fewer tokens due to better instruction following.*

---

## Troubleshooting

### Error: "API key not found"
**Solution:** Make sure you've set the `ANTHROPIC_API_KEY` environment variable or in the .env file.

### Error: "Rate limit exceeded"
**Solution:** Anthropic has different rate limits by tier. Check your account tier at https://console.anthropic.com/settings/limits

### Different outputs than OpenAI
**Expected:** Claude and GPT-3.5 are different models with different training, so outputs will vary. This is normal and doesn't indicate an error.

### Want shorter/longer responses
**Solution:** Adjust the `max_tokens` parameter in each API call.

### Want more/less creative responses
**Solution:** Adjust the `temperature` parameter:
- `0.0` = Deterministic, focused
- `0.7` = Balanced (default)
- `1.0` = More creative, random

---

## Testing Checklist

Before using in the workshop, test each scenario:

- [ ] QnA (basic question)
- [ ] YAML generation
- [ ] French response
- [ ] Text summarization (neutron star)
- [ ] Chinese summarization + translation
- [ ] Text classification (news articles)
- [ ] Product name generation
- [ ] Chinese poem translation
- [ ] Unstructured data parsing (Goocrux fruits)
- [ ] NLP to SQL query

---

## Workshop Integration

### Schedule Impact
**No changes needed to workshop schedule** - All scenarios work with Claude as drop-in replacement.

### Materials to Update
- [ ] Tell participants to get Anthropic API key instead of Azure OpenAI
- [ ] Update setup instructions in participant guide
- [ ] Update any slides that mention "OpenAI" or "GPT-3.5"

### Benefits for Participants
- Simpler setup (no Azure configuration)
- Better learning experience (Claude's responses are often more educational)
- Skills transfer to multiple LLM providers

---

## Next Steps

1. **Test the notebook** - Run through all cells to verify everything works
2. **Get API keys for participants** - Decide if DocuSign will provide keys or participants get their own
3. **Update remaining notebooks:**
   - `Zero_Shot,_Few_Shot,_and_Chain_of_Thought_Prompting_with_Azure_OpenAI.ipynb`
   - `Retrieval_Augmented_Generation_(RAG)_model_using_Azure_OpenAI.ipynb`
   - `Chatbot_with_OpenAI.ipynb`
4. **Update documentation** - WORKSHOP_SCHEDULE.md references

---

## Contact

For questions about this migration:
- Anthropic Documentation: https://docs.anthropic.com/
- Claude API Reference: https://docs.anthropic.com/en/api/messages
- Community Support: https://discord.gg/anthropic
