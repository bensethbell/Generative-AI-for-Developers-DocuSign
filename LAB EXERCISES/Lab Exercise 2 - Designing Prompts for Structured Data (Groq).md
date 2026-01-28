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

## 15. Extra Credit

### Part 1: Build an Interactive Chatbot

Turn your Groq API call into an interactive chatbot that keeps prompting the user for input in a loop.

**Requirements:**
- Use a `while` loop to continuously prompt the user for questions
- The chatbot should respond to each question using the Groq API
- The loop should exit when the user types `quit` or `exit`

**Starter Code:**
```python
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
model = "llama-3.3-70b-versatile"

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=300
    )
    print(f"\nAssistant: {response.choices[0].message.content.strip()}\n")
```

**Try it out:** Ask it a few questions in a row. Notice anything missing?

---

### Part 2: Add Conversation History

You'll notice that the chatbot from Part 1 doesn't remember previous messages. Each question is treated independently. Fix this by maintaining a list of messages and passing the full conversation history to the API on each call.

**Requirements:**
- Maintain a `messages` list that starts with the system message
- Append each user message and assistant response to the list
- Pass the full `messages` list to the API each time

**Hints:**
- Initialize your list with `[{"role": "system", "content": "You are a helpful assistant."}]`
- After the user types something, append `{"role": "user", "content": user_input}` to the list
- After getting a response, append `{"role": "assistant", "content": assistant_reply}` to the list
- Pass the entire list as the `messages` parameter in your API call

**Test it:** Ask "My name is Alex", then ask "What is my name?" — the chatbot should now remember.

---

### Part 3: Add Content Moderation

Now make your chatbot its own content moderator using a **meta-prompting** technique. Before processing a user's message (and optionally after generating a response), send the content to the model with a separate moderation prompt to check whether it should be allowed.

**Requirements:**
1. Write a moderation prompt that asks the model to evaluate whether a piece of text contains harmful content. Be specific about the kind of content you want to flag (pick one or more):
   - Racist or discriminatory language
   - Content not appropriate for children
   - Requests for illegal activity
   - Copyright infringement attempts
2. Create a `moderate(text)` function that:
   - Sends the text to Groq with your moderation prompt
   - Instructs the model to respond with ONLY `yes` or `no` (yes = harmful)
   - Parses the response into a boolean
3. Before sending the user's input to the chatbot:
   - Run `moderate(user_input)` — if flagged, print a rejection message and skip the API call
4. **(Bonus)** After generating the assistant's response:
   - Run `moderate(assistant_reply)` — if flagged, replace the response with a safe fallback message

**Hints:**
```python
def moderate(text):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a content moderator. Respond with ONLY 'yes' or 'no'."},
            {"role": "user", "content": f"Does the following text contain [YOUR CATEGORY HERE]?\n\n{text}"}
        ],
        temperature=0.0,
        max_tokens=3
    )
    result = response.choices[0].message.content.strip().lower()
    return result == "yes"
```

**Test it:** Try sending a message that should be flagged and verify the chatbot rejects it.
