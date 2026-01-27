# Lab Exercise 2 - Designing Prompts for Structured Data (Groq)

---

## 1. Objective

This lab focuses on **prompt design techniques** to make Groq (Llama models) return **structured outputs**, specifically:

- Valid **JSON responses**
- **Schema-controlled outputs**
- **Function-call-style responses** suitable for API integration

By the end of this lab, learners will be able to design prompts that reliably produce machine-readable data instead of free-form text.

---

## 2. Prerequisites

- Basic understanding of JSON
- Familiarity with APIs or backend systems (helpful but not mandatory)
- Access to Groq API (get your free API key at https://console.groq.com)

---

## 3. Why Structured Prompts Are Important

Structured prompting is required when:

- Integrating LLMs with applications
- Automating workflows
- Passing outputs to other systems
- Avoiding ambiguity in responses

**Examples:**
- Returning JSON for APIs
- Extracting entities from text
- Triggering backend functions

---

## 4. Part A: Prompting for JSON Output

### Task
Generate customer data strictly in JSON format.

### Prompt
```
You are an API.
Return ONLY valid JSON.
Do not add explanations.

Generate customer details with fields:
- customerId (string)
- name (string)
- email (string)
- totalPurchase (number)
```

### Expected Output
```json
{
  "customerId": "C001",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "totalPurchase": 1250.75
}
```

### Learning
- Explicitly instructing *"Return ONLY JSON"* avoids extra text
- Field names and data types must be specified

---

## 5. Part B: Enforcing a JSON Schema

### Task
Ensure Groq follows a fixed schema.

### Prompt
```
Return output in the following JSON schema only:

{
  "orderId": string,
  "customerId": string,
  "items": [
    {
      "product": string,
      "quantity": number,
      "price": number
    }
  ],
  "totalAmount": number
}

Generate sample order data.
```

### Expected Output
```json
{
  "orderId": "O1001",
  "customerId": "C001",
  "items": [
    {
      "product": "Laptop",
      "quantity": 1,
      "price": 1200
    }
  ],
  "totalAmount": 1200
}
```

### Learning
- Providing a schema strongly guides output structure
- Reduces parsing errors in applications

---

## 6. Part C: Prompting for Arrays of JSON Objects

### Task
Generate multiple records in JSON array format.

### Prompt
```
Return ONLY a JSON array.
Each object must contain:
- id
- name
- country

Generate 3 customer records.
```

### Expected Output
```json
[
  {"id": "C001", "name": "Amit", "country": "India"},
  {"id": "C002", "name": "Sarah", "country": "USA"},
  {"id": "C003", "name": "Luis", "country": "Spain"}
]
```

---

## 7. Part D: Prompting for Function-Call-Style Output

### Concept
Function calling allows LLMs to return **arguments** needed to invoke backend logic.

### Task
Extract intent and parameters for a function call.

### Function Definition (Conceptual)
```
function createOrder(customerId, product, quantity)
```

### Prompt
```
You are a system that prepares function calls.
Return ONLY JSON arguments for the function below.

Function: createOrder(customerId, product, quantity)

User input:
"Create an order for customer C001 for 2 laptops"
```

### Expected Output
```json
{
  "customerId": "C001",
  "product": "laptop",
  "quantity": 2
}
```

### Learning
- No natural language explanation
- Output maps directly to function parameters

---

## 8. Part E: Validating and Restricting Output

### Task
Prevent invalid values.

### Prompt
```
Return JSON only.
Ensure quantity is a positive integer.
If input is invalid, return:
{ "error": "Invalid input" }

User input:
"Order minus 3 phones for customer C005"
```

### Expected Output
```json
{ "error": "Invalid input" }
```

---

## 9. Part F: Combining Explanation + Structured Output (Controlled)

### Task
Return JSON and a short explanation in separate fields.

### Prompt
```
Return output as JSON with two fields:
- data (object)
- explanation (string)

Generate sample login event data.
```

### Expected Output
```json
{
  "data": {
    "userId": "U123",
    "loginTime": "2024-06-01T10:30:00Z",
    "ipAddress": "192.168.1.10"
  },
  "explanation": "This record represents a user login event."
}
```

---

## 10. Common Prompting Best Practices

- Clearly say **"Return ONLY JSON"**
- Define field names and data types
- Provide sample schema when possible
- Avoid ambiguous instructions
- Use capitalized constraints (ONLY, MUST)
- Validate output before using in production

---

## 11. Common Mistakes to Avoid

- Forgetting to restrict extra text
- Not specifying array vs object
- Leaving data types undefined
- Mixing explanation with data unintentionally

---

## 12. Python Code Example (Using Groq API)

Here's how to implement these prompts programmatically with Groq:

```python
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_structured_response(prompt, model="llama-3.3-70b-versatile"):
    """
    Send a prompt to Groq and get a structured JSON response.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an API that returns ONLY valid JSON. No explanations."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,  # Low temperature for consistent structured output
        max_tokens=500
    )
    return response.choices[0].message.content

# Example: Part A - JSON Output
prompt_a = """
Generate customer details with fields:
- customerId (string)
- name (string)
- email (string)
- totalPurchase (number)
"""

result = get_structured_response(prompt_a)
print(result)
```

---

## 13. Groq-Specific Tips

### Recommended Models for Structured Output
| Model | Speed | Best For |
|-------|-------|----------|
| `llama-3.3-70b-versatile` | Fast | Complex JSON schemas |
| `llama-3.1-8b-instant` | Very Fast | Simple JSON, high volume |
| `mixtral-8x7b-32768` | Fast | Long context JSON tasks |

### Temperature Settings
- Use `temperature=0.1` or lower for consistent JSON output
- Higher temperatures may introduce formatting variations

### JSON Mode (if available)
Some Groq models support explicit JSON mode:
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[...],
    response_format={"type": "json_object"}  # Forces JSON output
)
```

---

## 14. Conclusion

Designing prompts for structured data is essential for real-world LLM integrations. By explicitly defining schemas, constraints, and output rules, developers can reliably use Groq's Llama models for JSON generation, API workflows, and function calling without manual cleanup.

**Key Takeaways:**
- Groq's speed makes it ideal for high-volume structured data generation
- The same prompt engineering principles apply across LLM providers
- Always validate JSON output before using in production systems

Extras to add
* Add in interative loop for continuous chat
* Add in memory to your chatbot
## Integrate Meta Prompting

Ask your model to become it's own content moderator!

1. Design a prompt that asks your model to identify whether or not a prompt or a response contains some sort of harmful content.
    * We suggest defining a fairly specific kind of "harmful content."
        * e.g. "copyright infringement"
        * e.g. "racist language"
        * e.g. "mature themes not appropriate for children"
2. Before making any prompts and after generating any responses:
    * Inject the prompt or content to your meta prompt
    * Send that to the model
    * Parse the "yes" or "no" into a boolean
    * Reject the prompt or response if the model said you should.


