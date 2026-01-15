# Handoff: Create SQL-Based AI Labs (Snowflake Alternatives)

## Context

This workshop has three Snowflake Cortex demos that require paid Snowflake access:
- Demo 1: Text summarization with `SNOWFLAKE.CORTEX.SUMMARIZE`
- Demo 2: RAG with `EMBED_TEXT_768` + `VECTOR_COSINE_SIMILARITY` + `COMPLETE`
- Demo 3: Sentiment analysis with `SNOWFLAKE.CORTEX.SENTIMENT`

**Goal**: Create equivalent labs using free, locally-runnable alternatives that still demonstrate SQL + AI integration concepts.

## Reference Materials

The original Snowflake PDFs are in:
```
LAB EXERCISES/Real Use-case Demo 1 - SNOWFLAKE.CORTEX.SUMMARIZE LLM function.pdf
LAB EXERCISES/Real Use-case Demo 2-  Hello RAG in Snowflake Cortex.pdf
LAB EXERCISES/Real Use-case Demo 3 – Sentiment Analysis Using SNOWFLAKE.CORTEX.SENTIMENT.pdf
```

## Recommended Approach: SQLite + Python (Simplest)

SQLite is preferred because:
- Zero installation - ships with Python
- No server to run
- Single file database
- Students already have it

### Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Python                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   OpenAI    │  │   NumPy     │  │   SQLite    │ │
│  │ (embeddings │  │  (vector    │  │   (data     │ │
│  │  + LLM)     │  │   math)     │  │   storage)  │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────┘
```

This hybrid approach is actually more realistic than pure-SQL LLM calls - it's how most production systems work.

## Lab 1: SQL Data + LLM Summarization

### Learning Objectives
- Store text data in SQLite
- Query with SQL
- Pass results to OpenAI for summarization
- Store summaries back in database

### Notebook Structure

```python
# 1. Setup
import sqlite3
import openai
from dotenv import load_dotenv

# 2. Create database and sample data
conn = sqlite3.connect('support_tickets.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        ticket_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        category TEXT,
        transcript TEXT,
        summary TEXT
    )
''')

# Insert sample support transcripts (use same data as Snowflake demo)
sample_tickets = [
    (1001, 'Alice Brown', 'Delivery', 'The product was delayed by three days...'),
    (1002, 'Rajesh Kumar', 'Payment', 'Payment failed but money was deducted...'),
    # ... more rows
]

# 3. Query tickets that need summarization
cursor.execute("SELECT ticket_id, transcript FROM tickets WHERE summary IS NULL")
tickets_to_process = cursor.fetchall()

# 4. Summarize with OpenAI
def summarize(text):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize this support ticket in one sentence."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

# 5. Update database with summaries
for ticket_id, transcript in tickets_to_process:
    summary = summarize(transcript)
    cursor.execute("UPDATE tickets SET summary = ? WHERE ticket_id = ?", (summary, ticket_id))

conn.commit()

# 6. Query results with SQL
cursor.execute("SELECT ticket_id, customer_name, category, summary FROM tickets")
# Display results in table format
```

### Key Teaching Points
- SQL for data management (CREATE, INSERT, SELECT, UPDATE)
- Python as the "glue" between database and LLM
- Batch processing pattern (query → process → update)

---

## Lab 2: RAG with SQLite + Vector Search

### Learning Objectives
- Store documents and embeddings in SQLite
- Compute vector similarity with NumPy
- Implement full RAG pipeline with SQL data layer

### Notebook Structure

```python
# 1. Setup
import sqlite3
import numpy as np
import openai
import json

# 2. Create tables
conn = sqlite3.connect('knowledge_base.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        doc_id INTEGER PRIMARY KEY,
        content TEXT,
        embedding TEXT  -- Store as JSON string
    )
''')

# 3. Sample knowledge base (same as Snowflake demo)
documents = [
    "Employees are allowed to work remotely up to two days per week.",
    "Annual leave requests should be submitted at least two weeks in advance.",
    "The company provides full health insurance coverage to all permanent employees.",
    # ... more
]

# 4. Generate embeddings and store
def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

for i, doc in enumerate(documents):
    embedding = get_embedding(doc)
    cursor.execute(
        "INSERT INTO documents (doc_id, content, embedding) VALUES (?, ?, ?)",
        (i+1, doc, json.dumps(embedding))
    )
conn.commit()

# 5. Semantic search function
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_documents(query, top_k=3):
    query_embedding = get_embedding(query)

    cursor.execute("SELECT doc_id, content, embedding FROM documents")
    results = []
    for doc_id, content, emb_json in cursor.fetchall():
        emb = json.loads(emb_json)
        similarity = cosine_similarity(query_embedding, emb)
        results.append((doc_id, content, similarity))

    results.sort(key=lambda x: x[2], reverse=True)
    return results[:top_k]

# 6. RAG query
def rag_query(question):
    # Retrieve relevant documents
    relevant_docs = search_documents(question)
    context = "\n".join([doc[1] for doc in relevant_docs])

    # Generate answer
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Answer based on this context:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content, relevant_docs

# 7. Test it
answer, sources = rag_query("Does the company allow remote work?")
print(f"Answer: {answer}")
print(f"Sources: {[s[1][:50] for s in sources]}")
```

### Key Teaching Points
- Embeddings stored as JSON in SQLite (simple, portable)
- Vector math with NumPy (no extensions needed)
- Full RAG pipeline: embed → store → retrieve → generate
- Compare to Snowflake: same concepts, different syntax

### SQL-Focused Queries to Demonstrate

```python
# Show students these SQL queries work on the data:

# Count documents
cursor.execute("SELECT COUNT(*) FROM documents")

# Search by keyword (traditional SQL)
cursor.execute("SELECT * FROM documents WHERE content LIKE '%remote%'")

# Get all documents for a category (if you add categories)
cursor.execute("SELECT * FROM documents WHERE category = 'HR Policy'")
```

---

## Lab 3: Sentiment Analysis with SQLite

### Learning Objectives
- Store reviews in SQLite
- Analyze sentiment with OpenAI
- Aggregate results with SQL

### Notebook Structure

```python
# 1. Setup and create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        review_text TEXT,
        sentiment_score REAL,
        sentiment_label TEXT
    )
''')

# 2. Insert sample reviews (same as Snowflake demo)
reviews = [
    "The product quality is amazing, I absolutely loved it!",
    "Terrible experience. Nothing worked as expected.",
    "It was okay, not great, not terrible.",
    "The packaging was damaged but customer support helped quickly."
]

# 3. Sentiment analysis function
def analyze_sentiment(text):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Rate the sentiment of this text from -1 (very negative) to 1 (very positive). Return only a number."},
            {"role": "user", "content": text}
        ]
    )
    score = float(response.choices[0].message.content.strip())
    label = "Positive" if score > 0.3 else "Negative" if score < -0.3 else "Neutral"
    return score, label

# 4. Process and store
for i, review in enumerate(reviews):
    score, label = analyze_sentiment(review)
    cursor.execute(
        "INSERT INTO reviews (id, review_text, sentiment_score, sentiment_label) VALUES (?, ?, ?, ?)",
        (i+1, review, score, label)
    )
conn.commit()

# 5. SQL aggregations (key teaching moment!)
# Average sentiment
cursor.execute("SELECT AVG(sentiment_score) as avg_sentiment FROM reviews")

# Group by sentiment
cursor.execute("""
    SELECT sentiment_label, COUNT(*) as count
    FROM reviews
    GROUP BY sentiment_label
""")

# Find most negative reviews
cursor.execute("""
    SELECT review_text, sentiment_score
    FROM reviews
    WHERE sentiment_label = 'Negative'
    ORDER BY sentiment_score ASC
""")
```

### Key Teaching Points
- SQL aggregations (AVG, COUNT, GROUP BY)
- Filtering and sorting results
- Storing ML results for later analysis

---

## Alternative: PostgreSQL + pgvector (Advanced Option)

If you want pure-SQL vector operations, use PostgreSQL with pgvector.

### Setup Options
1. **Local**: Install PostgreSQL + pgvector extension
2. **Cloud (free)**: Supabase, Neon, or Railway

### Example with Supabase (free tier)

```python
import psycopg2
from psycopg2.extras import execute_values

# Connect to Supabase PostgreSQL
conn = psycopg2.connect("postgresql://user:pass@host:5432/postgres")
cursor = conn.cursor()

# Enable pgvector
cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")

# Create table with vector column
cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        content TEXT,
        embedding vector(1536)
    )
""")

# Insert with embedding
cursor.execute(
    "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
    (doc_text, embedding_list)
)

# Vector similarity search IN PURE SQL
cursor.execute("""
    SELECT content, 1 - (embedding <=> %s::vector) as similarity
    FROM documents
    ORDER BY embedding <=> %s::vector
    LIMIT 3
""", (query_embedding, query_embedding))
```

### When to Use PostgreSQL vs SQLite

| Scenario | Recommendation |
|----------|----------------|
| Workshop with easy setup | SQLite |
| Production-realistic demo | PostgreSQL |
| Students have varied environments | SQLite |
| Teaching pure SQL vector ops | PostgreSQL + pgvector |
| Time-constrained | SQLite |

---

## File Naming Convention

Place new notebooks in `NEW LABS/`:
```
NEW LABS/SQL_Summarization_SQLite.ipynb
NEW LABS/SQL_RAG_SQLite.ipynb
NEW LABS/SQL_Sentiment_SQLite.ipynb
```

Or if creating PostgreSQL versions:
```
NEW LABS/SQL_RAG_PostgreSQL_pgvector.ipynb
```

Also make new pdfs that are updated to reflect the changes


## Dependencies to Add to requirements.txt

The SQLite labs need no additional dependencies (sqlite3 ships with Python).

For PostgreSQL version only:
```
psycopg2-binary
```

## Comparison Table for Students

Include this in the notebooks to show equivalence:

| Snowflake Cortex | SQLite + Python Equivalent |
|------------------|---------------------------|
| `SNOWFLAKE.CORTEX.SUMMARIZE(text)` | `openai.chat.completions.create(...)` |
| `SNOWFLAKE.CORTEX.EMBED_TEXT_768(model, text)` | `openai.embeddings.create(...)` |
| `VECTOR_COSINE_SIMILARITY(v1, v2)` | `np.dot(a,b) / (norm(a) * norm(b))` |
| `SNOWFLAKE.CORTEX.COMPLETE(model, prompt)` | `openai.chat.completions.create(...)` |
| `SNOWFLAKE.CORTEX.SENTIMENT(text)` | Custom prompt to OpenAI |

Key insight: Snowflake Cortex wraps these same operations in SQL functions. The underlying mechanics are identical.

---

## Summary

1. **Create 3 Jupyter notebooks** mirroring the Snowflake demos
2. **Use SQLite** for data storage (zero setup)
3. **Use OpenAI** for LLM operations (already have API key)
4. **Use NumPy** for vector math (already installed)
5. **Emphasize SQL queries** for data management
6. **Show the comparison** to Snowflake syntax

The goal is teaching the same concepts (summarization, RAG, sentiment) while demonstrating SQL data management patterns, without requiring Snowflake access.
