# 3-Day Workshop Schedule: Generative AI

## Workshop Structure
- **Days 1-2**: Generative AI for Developers (2-day technical workshop)
- **Day 3**: Generative AI: Big Picture (1-day intro, DIFFERENT STUDENTS)

---

# DAYS 1-2: GENERATIVE AI FOR DEVELOPERS

**Audience**: Software Developers, Data Scientists, Solution Architects
**Prerequisites**: Python experience, API familiarity

---

## DAY 1: Foundations & Prompting

### Morning Session (9:00 AM - 12:00 PM): Foundations of LLMs in Modern Development

#### 1. LLM Fundamentals (60 min)
- Capabilities, limitations, and common use cases in software development
- Platform Overview: Gemini, GitHub Copilot, Azure AI architecture and APIs

**Materials:**
- **SLIDES**: None specifically identified for this section
- **PDFs**:
  - `PDFs/1. LLM Fundamentals- Capabilities, Limitations, and Common Use Cases.pdf`
- **Reference**: `EXTRA NOTES/Hallucination in Large Language Models (LLMs).pdf`

**⚠️ DISCREPANCY**: No slides provided for LLM Fundamentals section

---

#### 2. Core Concepts (45 min)
- Understanding tokens, temperature, system roles, and other key parameters

**Materials:**
- **SLIDES**: None specifically identified
- **PDFs**:
  - `PDFs/2. Core Concepts of Large Language Models (LLMs).pdf`

**⚠️ DISCREPANCY**: No slides provided for Core Concepts section

---

#### 3. Prompting for Developer Productivity - Part 1 (75 min)
- Structuring prompts for clarity, format, and constraints from a developer's perspective

**Materials:**
- **SLIDES**: `SLIDES/Introduction to Prompt Engineering (Part-1).pdf` ✓
- **PDFs**:
  - `PDFs/3. Prompting for Developer Productivity.pdf`
- **Reference**: `EXTRA NOTES/Prompt Cheat-Sheet for Developers.pdf`

---

### Afternoon Session (1:00 PM - 5:00 PM): Hands-On Lab & Advanced Prompting

#### 4. Hands-On Lab: GitHub Copilot (120 min)
- Leveraging tools like Gemini and GitHub Copilot for code generation, explanation, refactoring, and automated documentation

**Materials:**
- **PDFs**:
  - `LAB EXERCISES/Lab Exercise 1 - GitHub Copilot for Code Generation, Explanation, Refactoring, and Automated Documentation.pdf`

**⚠️ DISCREPANCY**:
- This lab requires actual GitHub Copilot access - needs clarification on licensing
- No NEW LAB replacement created (tool-based demo, not code-based)
- Outline mentions "Gemini" but lab only covers GitHub Copilot

---

#### 5. Introduction to Prompt Engineering Part 2 (60 min)
- Advanced prompting techniques

**Materials:**
- **SLIDES**: `SLIDES/Introduction to Prompt Engineering (Part-2).pdf` ✓

---

#### 6. Complex Outputs & Case Study (60 min)
- Designing prompts for structured data like JSON and function calls
- Case Study: Analyzing effective vs. ineffective prompts for a real-world coding problem

**Materials:**
- **PDFs**:
  - `LAB EXERCISES/Lab Exercise 2 - Designing Prompts for Structured Data.pdf`
- **NEW LABS** (partially covers this):
  - `NEW LABS/Prompt_Engineering_OpenAI.ipynb`
  - `NEW LABS/Zero_Shot_Few_Shot_Chain_of_Thought_OpenAI.ipynb`

**⚠️ DISCREPANCY**:
- OLD lab focuses on structured outputs
- NEW labs focus more on prompting techniques (zero-shot, few-shot, CoT)
- Not a perfect match - may need adjustments

---

## DAY 2: Architecture, Implementation & Responsible AI

### Morning Session (9:00 AM - 12:00 PM): Context Engineering & Architecture

#### 1. Context Engineering (60 min)
- Selecting and structuring the most relevant information to guide the model's response
- Maintaining context in multi-turn interactions

**Materials:**
- **SLIDES**: None provided
- **PDFs**:
  - `PDFs/4. Context Engineering.pdf`

**⚠️ DISCREPANCY**: No slides for this critical section

---

#### 2. API Parameter Tuning (45 min)
- Leveraging advanced API parameters for fine-tuning model responses

**Materials:**
- **SLIDES**: None provided
- **PDFs**:
  - `PDFs/5. API Parameter Tuning.pdf`

**⚠️ DISCREPANCY**: No slides provided

---

#### 3. Proposed Lab 1: Developer Productivity Accelerator with Context Engineering (75 min)
**Objective**: Use an LLM and practice context engineering to accelerate a common development task

**Scenario**: Participants will be given a piece of complex, undocumented legacy code. They will practice context engineering by:
1. Generate detailed explanation of code's functionality
2. Write comprehensive suite of unit tests
3. Refactor code for improved readability and efficiency

**Materials:**
- **NONE PROVIDED**

**🚨 CRITICAL GAP**: This lab is described in the outline but DOES NOT EXIST in materials
- Not covered by OLD LABS (Snowflake-specific)
- Not covered by NEW LABS (your OpenAI notebooks)
- **ACTION NEEDED**: Create this lab or clarify if it should be removed

---

### Afternoon Session (1:00 PM - 5:00 PM): Building LLM Applications

#### 4. LLM Application Architecture (60 min)
- Discussing key design patterns (e.g., Agent-based systems, Retrieval-Augmented Generation)
- Defining clear goals and conversation flows for a specific business use case (e.g., internal documentation helper)

**Materials:**
- **SLIDES**: None provided
- **PDFs**:
  - `PDFs/6. LLM Application Architecture.pdf`
- **Reference**:
  - `EXTRA NOTES/AI Agents – Concepts, Architecture, Examples, and Use Cases.pdf`
  - `EXTRA NOTES/Retrieval-Augmented Generation (RAG).pdf`

**⚠️ DISCREPANCY**: No slides for this architecture section

---

#### 5. Implementation Deep Dive (60 min)
- Managing state and context for coherent, multi-turn conversations
- Techniques for creating both short-term memory (in-prompt) and long-term memory (vector stores)
- Connecting LLMs to external data sources and APIs to provide up-to-date, relevant responses

**Materials:**
- **SLIDES**: None provided
- **PDFs**:
  - `PDFs/7. Implementation Deep Dive for LLM Applications.pdf`
- **Reference**:
  - `EXTRA NOTES/Model Context Protocol (MCP) Server.pdf`

**⚠️ DISCREPANCY**: No slides provided

---

#### 6. Proposed Lab 2: Building a Knowledge-Base Chatbot with RAG (90 min)
**Objective**: Build a chatbot that can answer questions based on a private knowledge base

**Overview**: Using Python and a service like Azure AI or the Gemini API, participants will build a simple application that ingests a set of technical documents. The chatbot will then use these documents as its sole source of truth to accurately answer user queries, demonstrating the core principles of Retrieval-Augmented Generation (RAG).

**Materials:**
- **NEW LABS**:
  - ✓ `NEW LABS/RAG_with_OpenAI_Fixed.ipynb` (THIS IS LAB 2!)
- **Reference**:
  - `EXTRA NOTES/Retrieval-Augmented Generation (RAG).pdf`

**⚠️ DISCREPANCY**:
- Outline says "Azure AI or Gemini API"
- NEW lab uses OpenAI API
- OLD LABS use Snowflake Cortex (not relevant anymore)
  - `LAB EXERCISES/Real Use-case Demo 2- Hello RAG in Snowflake Cortex.pdf` (OLD - ignore)

---

#### 7. Responsible AI: Security, Ethics, and Best Practices (60 min)
- Cost Management: Token optimization, intelligent model selection, result caching
- Reliability and Error Handling: Robust error handling for API failures, fallbacks for poor outputs
- Mitigating Bias and Harmful Responses: Evaluating outputs for bias, content safety filters, ethical AI guidelines
- Security for LLM Applications: Key vulnerabilities, preventing prompt injection attacks
- Ethical Considerations: Data privacy, transparency, accountability in production AI systems

**Materials:**
- **SLIDES**: None provided
- **PDFs**:
  - `PDFs/8. Responsible AI in LLM Applications.pdf`
  - `PDFs/9. Mitigating Bias, Harmful Responses, and Securing LLM Applications.pdf`

**⚠️ DISCREPANCY**:
- This is a LOT of content (5 major topics) crammed into 60 minutes at end of Day 2
- No slides provided for this critical section
- May need to be expanded or redistributed

---

# DAY 3: GENERATIVE AI - BIG PICTURE

**⚠️ DIFFERENT STUDENTS** - Introductory audience (Developers, Product Managers, Business Leaders)
**Prerequisites**: Basic understanding of ML/AI concepts

---

## Morning Session (9:00 AM - 12:00 PM): Introduction to Gen AI & ChatGPT

#### 1. Introduction to Generative AI (90 min)
- Definition and significance of generative AI
- Overview of applications across industries
- Basics of natural language generation

**Materials:**
- **SLIDES**: `SLIDES/Generative AI Holistic Perspective.pdf` ✓
- **Reference**:
  - `EXTRA NOTES/AI Agents – Concepts, Architecture, Examples, and Use Cases.pdf`
  - `EXTRA NOTES/Hallucination in Large Language Models (LLMs).pdf`

---

#### 2. Understanding ChatGPT (90 min)
- Introduction to ChatGPT and how it processes language
- Key features and capabilities of ChatGPT
- Examples of ChatGPT applications

**Materials:**
- **SLIDES**: Likely covered in Holistic Perspective deck
- **No separate materials provided**

**⚠️ DISCREPANCY**: Outline suggests detailed ChatGPT coverage but no specific materials beyond the holistic slides

---

## Afternoon Session (1:00 PM - 5:00 PM): Practical Applications

#### 3. Applying ChatGPT in Real-World Scenarios (60 min)
- Use cases of ChatGPT in customer service, content generation, and automation
- Best practices for optimizing ChatGPT outputs
- Ethical considerations when using AI-powered chatbots

**Materials:**
- **No specific materials provided**

**⚠️ DISCREPANCY**: No dedicated materials for this section

---

#### 4. Hands-On Workshop: Using ChatGPT (120 min)
- Setting up and accessing ChatGPT API
- Exploring ChatGPT capabilities through interactive examples
- Building a simple chatbot prototype using ChatGPT

**Materials:**
- **NEW LABS**:
  - ✓ `NEW LABS/Chatbot_with_OpenAI_Fixed.ipynb`
- **Reference**:
  - `EXTRA NOTES/Prompt Cheat-Sheet for Developers.pdf`

**⚠️ NOTE**: This is the right lab for this section!

---

#### 5. Case Studies and Discussion (60 min)
- Review of successful implementations of ChatGPT
- Challenges and limitations of using AI-powered assistants
- Future trends and advancements in generative AI and conversational AI technologies

**Materials:**
- **No specific materials provided**

**⚠️ DISCREPANCY**: No case studies or discussion materials provided

---

# MATERIALS NOT USED IN OUTLINE

## OLD LABS (Snowflake-based - Replaced by NEW LABS):
- ❌ `LAB EXERCISES/Real Use-case Demo 1 - SNOWFLAKE.CORTEX.SUMMARIZE LLM function.pdf`
- ❌ `LAB EXERCISES/Real Use-case Demo 2- Hello RAG in Snowflake Cortex.pdf` (replaced by OpenAI RAG lab)
- ❌ `LAB EXERCISES/Real Use-case Demo 3 – Sentiment Analysis Using SNOWFLAKE.CORTEX.SENTIMENT.pdf`

**⚠️ QUESTION**: Should OpenAI equivalents be created for Summarize and Sentiment Analysis demos?

## PROJECTS Folder:
- `PROJECTS/MCP-SERVER/README.md` - Not referenced in outline

**⚠️ QUESTION**: Is this for advanced/extra content, or should it be integrated?

---

# SUMMARY OF MAJOR DISCREPANCIES

## 1. MISSING MATERIALS

### Critical Gaps:
- **Proposed Lab 1** (Developer Productivity Accelerator with Context Engineering) - **DOES NOT EXIST**
- **Day 1-2 slides** - Only 2 slide decks for prompting, none for: LLM Fundamentals, Core Concepts, Context Engineering, API Tuning, Architecture, Implementation, or Responsible AI
- **Day 3 case studies** - No materials for case studies section

### Missing Demos:
- Summarize demo (OLD: Snowflake, NEW: none)
- Sentiment Analysis demo (OLD: Snowflake, NEW: none)

## 2. PLATFORM INCONSISTENCIES

**Outline mentions**: Google Gemini, GitHub Copilot, Azure AI
**OLD LABS use**: Snowflake Cortex exclusively
**NEW LABS use**: OpenAI API exclusively

**Questions**:
- Is OpenAI the confirmed platform going forward?
- Should Gemini/Azure examples be added?
- Is GitHub Copilot Lab 1 staying as-is (requires licenses)?

## 3. CONTENT COVERAGE ISSUES

### Day 2 Afternoon is Overloaded:
- 60 min: Architecture
- 60 min: Implementation Deep Dive
- 90 min: Lab 2 (RAG Chatbot)
- 60 min: Responsible AI (5 major topics!)
- **Total**: 4.5 hours of content for 4-hour session

### Day 3 Big Picture Lacks Depth:
- Only 1 slide deck provided (Holistic Perspective)
- No case studies materials
- No hands-on materials besides the chatbot lab
- Limited supporting content for 1-day workshop

## 4. MATERIALS ALIGNMENT

### ✅ GOOD ALIGNMENT:
- NEW LABS/RAG_with_OpenAI_Fixed.ipynb → Proposed Lab 2
- NEW LABS/Chatbot_with_OpenAI_Fixed.ipynb → Day 3 Hands-On Workshop
- All 9 core PDFs align with Day 1-2 theory sections

### ⚠️ PARTIAL ALIGNMENT:
- NEW LABS/Prompt_Engineering_OpenAI.ipynb → Partially covers Complex Outputs
- NEW LABS/Zero_Shot_Few_Shot_Chain_of_Thought_OpenAI.ipynb → Relates to prompting techniques but not specifically called out in outline

### ❌ MISSING ALIGNMENT:
- Proposed Lab 1 (Context Engineering with legacy code) - No corresponding lab
- GitHub Copilot Lab 1 - No NEW LAB replacement (tool-based, not code)

## 5. EXTRA NOTES USAGE

The 5 "EXTRA NOTES" PDFs are listed as reference materials but not explicitly integrated into the schedule:
- AI Agents – useful for Architecture section
- Hallucination in LLMs – useful for Fundamentals and Responsible AI
- Prompt Cheat-Sheet – useful for all prompting sections
- MCP Server – advanced topic, not in outline
- RAG – useful for Lab 2

**Question**: Should these be required reading or optional reference?

---

# QUESTIONS FOR CREATOR CALL

## Platform & Tools:
1. Is OpenAI the confirmed platform, or should Gemini/Azure examples be added?
2. Will students have GitHub Copilot licenses for Lab 1?
3. Should the Snowflake demos be recreated in OpenAI (Summarize, Sentiment)?

## Missing Content:
4. **Proposed Lab 1** (Context Engineering with legacy code) - Should this be created, or removed from outline?
5. Where are the slide decks for Days 1-2 content (Fundamentals, Core Concepts, Architecture, etc.)?
6. Where are the Day 3 case study materials?

## Schedule & Pacing:
7. Day 2 afternoon seems overloaded (4.5 hours content in 4 hours) - should anything be moved?
8. Should Responsible AI be its own longer section, or is 60 min sufficient?

## Materials Status:
9. Are the NEW LABS (OpenAI-based) approved replacements for OLD LABS (Snowflake)?
10. Should the EXTRA NOTES PDFs be required or optional reference materials?
11. What's the status of PROJECTS/MCP-SERVER - is this in scope?

## Pedagogical:
12. Lab 2 outline says "Azure AI or Gemini" but NEW lab uses OpenAI - is this OK?
13. Should there be more hands-on time in Day 3 Big Picture, or is it meant to be more conceptual?
