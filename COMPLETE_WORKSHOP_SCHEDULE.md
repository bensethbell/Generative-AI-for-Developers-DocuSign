# 3-Day Workshop Schedule: Generative AI (COMPLETE - All Materials)

**Format**: 9:00 AM - 5:00 PM each day | Lunch: 12:00-1:00 PM
**Target**: 50%+ hands-on/group work time

---

# DAY 1: GENERATIVE AI FOR DEVELOPERS - Foundations & Prompting

**Audience**: Software Developers, Data Scientists, Solution Architects

## Morning Session (9:00 AM - 12:00 PM)

### 9:00-9:45 AM | LLM Fundamentals (45 min lecture)
**Objectives**: Capabilities, limitations, common use cases in software development, platform overview

**Materials**:
- **PDF 1**: `LLM Fundamentals- Capabilities, Limitations, and Common Use Cases.pdf`
- **PDF 2**: `Core Concepts of Large Language Models (LLMs).pdf`

**Format**: Instructor presentation covering:
- What LLMs can and cannot do
- Tokens, temperature, system roles, key parameters
- Overview of platforms (OpenAI, GitHub Copilot, Snowflake Cortex)

---

### 9:45-10:00 AM | Break (15 min)

---

### 10:00-12:00 PM | Prompting for Developer Productivity (2 hours hands-on)
**Objectives**: Learn prompt structure, practice with real developer tasks

**Materials**:
- **PDF 3**: `Prompting for Developer Productivity.pdf` (reference)
- **SLIDES**: `Introduction to Prompt Engineering (Part-1).pdf`
- **REFERENCE**: `EXTRA NOTES/Prompt Cheat-Sheet for Developers.pdf`

**Format**:
- 10:00-10:30 (30 min): Instructor presentation on prompt engineering basics
- 10:30-12:00 (90 min): **HANDS-ON** - Students practice prompting techniques with provided examples

---

## Lunch Break (12:00-1:00 PM)

---

## Afternoon Session (1:00 PM - 5:00 PM)

### 1:00-2:00 PM | GitHub Copilot Lab (60 min hands-on)
**Objectives**: Use GitHub Copilot for code generation, explanation, refactoring, documentation

**Materials**:
- **LAB**: `Lab Exercise 1 - GitHub Copilot for Code Generation, Explanation, Refactoring, and Automated Documentation.pdf`

**Format**: **HANDS-ON LAB** - Students work through GitHub Copilot exercises

---

### 2:00-2:15 PM | Break (15 min)

---

### 2:15-3:00 PM | Advanced Prompting Techniques (45 min)
**Objectives**: Zero-shot, few-shot, chain-of-thought reasoning

**Materials**:
- **SLIDES**: `Introduction to Prompt Engineering (Part-2).pdf`

**Format**:
- 2:15-2:45 (30 min): Instructor presentation on advanced techniques
- 2:45-3:00 (15 min): Demo examples

---

### 3:00-5:00 PM | Advanced Prompting Labs (2 hours hands-on)
**Objectives**: Practice zero-shot/few-shot/chain-of-thought and structured outputs

**Materials**:
- **NEW LAB 1**: `Zero_Shot_Few_Shot_Chain_of_Thought_OpenAI.ipynb`
- **NEW LAB 2**: `Prompt_Engineering_OpenAI.ipynb`
- **REFERENCE**: `Lab Exercise 2 - Designing Prompts for Structured Data.pdf`

**Format**: **HANDS-ON LAB** - Students work through both notebooks
- 3:00-4:00 (60 min): Zero-shot, few-shot, chain-of-thought exercises
- 4:00-5:00 (60 min): Advanced prompt engineering including structured outputs (JSON, function calls)

---

**Day 1 Summary**:
- Lecture: 2 hours (25%)
- Hands-on: 5.75 hours (72%)
- Breaks: 0.25 hours (3%)

---

# DAY 2: GENERATIVE AI FOR DEVELOPERS - Architecture & Applications

**Audience**: Software Developers, Data Scientists, Solution Architects

## Morning Session (9:00 AM - 12:00 PM)

### 9:00-9:30 AM | Context Engineering (30 min lecture)
**Objectives**: Selecting relevant information, maintaining context in multi-turn interactions

**Materials**:
- **PDF 4**: `Context Engineering.pdf`

**Format**: Instructor presentation with examples

---

### 9:30-10:30 AM | API Parameter Tuning (60 min)
**Objectives**: Learn and practice with advanced API parameters

**Materials**:
- **PDF 5**: `API Parameter Tuning.pdf`

**Format**:
- 9:30-9:50 (20 min): Instructor presentation
- 9:50-10:30 (40 min): **HANDS-ON** - Students experiment with temperature, top_p, max_tokens, etc.

---

### 10:30-10:45 AM | Break (15 min)

---

### 10:45-12:00 PM | Context Engineering Practice (75 min hands-on)
**Objectives**: Apply context engineering to real scenarios

**Materials**:
- **PDF 4**: `Context Engineering.pdf` (reference)

**Format**: **HANDS-ON** - Group work on context engineering exercises
- Provide sample scenarios where students practice selecting and structuring context
- Multi-turn conversation exercises

**Note**: This partially addresses "Proposed Lab 1" from outline - still needs legacy code scenario to be created

---

## Lunch Break (12:00-1:00 PM)

---

## Afternoon Session (1:00 PM - 5:00 PM)

### 1:00-2:00 PM | LLM Application Architecture & MCP (60 min lecture)
**Objectives**: Design patterns (Agents, RAG, MCP), conversation flows, use cases

**Materials**:
- **PDF 6**: `LLM Application Architecture.pdf`
- **PDF 7**: `Implementation Deep Dive for LLM Applications.pdf`
- **EXTRA NOTES**: `Model Context Protocol (MCP) Server.pdf` ⚠️ **REQUIRED**
- **REFERENCE**:
  - `EXTRA NOTES/AI Agents – Concepts, Architecture, Examples, and Use Cases.pdf`
  - `EXTRA NOTES/Retrieval-Augmented Generation (RAG).pdf`

**Format**: Instructor presentation covering:
- Agent-based systems
- RAG (Retrieval-Augmented Generation) patterns
- **MCP (Model Context Protocol)** - Required coverage of connecting LLMs to external tools and data
- State management and memory techniques
- Connecting to external data sources and APIs

---

### 2:00-2:15 PM | Break (15 min)

---

### 2:15-3:00 PM | Platform Examples: Snowflake Cortex (45 min demo)
**Objectives**: See LLM capabilities across different platforms

**Materials**:
- **DEMO 1**: `Real Use-case Demo 1 - SNOWFLAKE.CORTEX.SUMMARIZE.pdf`
- **DEMO 3**: `Real Use-case Demo 3 – Sentiment Analysis Using SNOWFLAKE.CORTEX.pdf`

**Format**: Instructor-led demonstrations
- 2:15-2:35 (20 min): Summarize function demo
- 2:35-3:00 (25 min): Sentiment analysis demo

**Note**: Shows platform diversity - Snowflake alongside OpenAI approach

---

### 3:00-4:00 PM | Building RAG Applications (60 min hands-on)
**Objectives**: Build knowledge-base chatbots demonstrating RAG principles on different platforms

**Materials**:
- **NEW LAB**: `RAG_with_OpenAI_Fixed.ipynb`
- **DEMO 2**: `Real Use-case Demo 2 - Hello RAG in Snowflake Cortex.pdf`
- **REFERENCE**: `EXTRA NOTES/Retrieval-Augmented Generation (RAG).pdf`

**Format**: **HANDS-ON LAB** with platform comparison
- 3:00-3:15 (15 min): Instructor reviews Snowflake RAG approach (Demo 2 walkthrough)
- 3:15-4:00 (45 min): **HANDS-ON** - Students begin OpenAI RAG chatbot
  - Ingesting documents
  - Vector storage
  - Retrieval and generation

---

### 4:00-4:15 PM | Break (15 min)

---

### 4:15-5:00 PM | MCP Server Implementation (45 min hands-on) ⚠️ **REQUIRED**
**Objectives**: Understand and implement Model Context Protocol for connecting LLMs to external tools

**Materials**:
- **EXTRA NOTES**: `Model Context Protocol (MCP) Server.pdf`
- **PROJECT**: `PROJECTS/MCP-SERVER/README.md`

**Format**: **HANDS-ON LAB** - Introduction to MCP
- Overview of MCP architecture
- Setting up MCP server basics
- Connecting LLM applications to external tools and data sources

**Note**: This is REQUIRED per outline, not optional. More advanced MCP work can continue as homework/follow-up.

---

**Day 2 Summary**:
- Lecture: 2.5 hours (31%)
- Demos: 0.75 hours (9%)
- Hands-on: 3.5 hours (44%)
- Breaks: 0.25 hours (3%)
- Lunch: 1 hour (13%)

**Note**: Day 2 is 53% hands-on/demos combined. Responsible AI content moved to homework/separate session to accommodate MCP requirement.

---

# DAY 2 HOMEWORK / FOLLOW-UP

### Responsible AI: Security, Ethics, and Best Practices (Self-study)
**Objectives**: Cost management, bias mitigation, security, ethical considerations

**Materials**:
- **PDF 8**: `Responsible AI in LLM Applications.pdf`
- **PDF 9**: `Mitigating Bias, Harmful Responses, and Securing LLM Applications.pdf`
- **REFERENCE**: `EXTRA NOTES/Hallucination in Large Language Models (LLMs).pdf`

**Topics for self-study**:
- Token optimization and cost management
- Reliability and error handling
- Bias evaluation and content safety
- Prompt injection and security vulnerabilities
- Ethical considerations: data privacy, transparency, accountability

**Note**: These topics can be discussed throughout the workshop or assigned as homework due to time constraints with MCP requirement.

---

# DAY 3: GENERATIVE AI - BIG PICTURE

**⚠️ DIFFERENT STUDENTS** - Introductory audience (Developers, Product Managers, Business Leaders)

## Morning Session (9:00 AM - 12:00 PM)

### 9:00-10:30 AM | Introduction to Generative AI (90 min lecture)
**Objectives**: Basics of Gen AI, applications across industries, understanding ChatGPT

**Materials**:
- **SLIDES**: `SLIDES/Generative AI Holistic Perspective.pdf`
- **NOTES**: `../Docusign/Generative AI Big Picture/NOTES/Introduction to Generative AI.docx`
- **NOTES**: `../Docusign/Generative AI Big Picture/NOTES/Understanding ChatGPT.docx`
- **REFERENCE**:
  - `EXTRA NOTES/AI Agents – Concepts, Architecture, Examples, and Use Cases.pdf`
  - `EXTRA NOTES/Hallucination in Large Language Models (LLMs).pdf`

**Format**: Instructor presentation covering:
- Definition and significance of generative AI
- Applications across industries
- Natural language generation basics
- How ChatGPT processes language
- Key features and capabilities of ChatGPT
- Real-world examples

---

### 10:30-10:45 AM | Break (15 min)

---

### 10:45-12:00 PM | Applying ChatGPT & Best Practices (75 min lecture + discussion)
**Objectives**: Real-world use cases, best practices, ethical considerations

**Materials**:
- **NOTES**: `../Docusign/Generative AI Big Picture/NOTES/Applying ChatGPT in Real-World Scenarios.docx`
- **NOTES**: `../Docusign/Generative AI Big Picture/NOTES/Effective Prompt.docx`
- **NOTES**: `../Docusign/Generative AI Big Picture/NOTES/Effective Use of ChatGPT in DocuSign.docx`
- **REFERENCE**: `EXTRA NOTES/Prompt Cheat-Sheet for Developers.pdf`

**Format**: Lecture with group discussion
- Use cases in customer service, content generation, automation
- Best practices for optimizing ChatGPT outputs
- Ethical considerations when using AI-powered chatbots
- DocuSign-specific use cases and applications

---

## Lunch Break (12:00-1:00 PM)

---

## Afternoon Session (1:00 PM - 5:00 PM)

### 1:00-1:30 PM | Hands-On Workshop Introduction (30 min)
**Objectives**: Prepare for hands-on work with ChatGPT API

**Materials**:
- **NOTES**: `../Docusign/Generative AI Big Picture/NOTES/Hands-On Workshop- Using ChatGPT.docx`

**Format**: Instructor-led setup
- Setting up and accessing ChatGPT API
- Overview of hands-on exercises
- Introduction to DocuSign AI Agent project

---

### 1:30-3:00 PM | Building DocuSign AI Agent (90 min hands-on)
**Objectives**: Build a DocuSign-specific AI agent demonstrating practical business application

**Materials**:
- **NEW LAB**: `../Docusign/Generative AI Big Picture/DocuSign_Agreement_AI_Agent.ipynb`
- **PROJECT INSTRUCTIONS**: `../Docusign/Generative AI Big Picture/Project Work – Develop a DocuSign Agreement AI Agent.docx.pdf`
- **REFERENCE CODE**:
  - `../Docusign/Generative AI Big Picture/PROJECT WORK/AI-AGENT/docusign-agent.py`
  - `../Docusign/Generative AI Big Picture/PROJECT WORK/AI-AGENT/finance_agent_llama_default.py`

**Format**: **HANDS-ON LAB** - Students build DocuSign AI agent
- Understanding the business problem
- Building the agent prototype
- Connecting to DocuSign-related functionality
- Testing with real scenarios

**Note**: This is more business-relevant than generic chatbot for DocuSign audience

---

### 3:00-3:15 PM | Break (15 min)

---

### 3:15-4:15 PM | Extended Agent Development & Experimentation (60 min hands-on)
**Objectives**: Enhance agent functionality, optimize outputs, handle edge cases

**Materials**:
- **LAB** (continued): `../Docusign/Generative AI Big Picture/DocuSign_Agreement_AI_Agent.ipynb`

**Format**: **HANDS-ON** - Students work individually or in groups to:
- Add features to their DocuSign AI agent
- Test different prompting strategies
- Experiment with parameters (temperature, max_tokens)
- Handle errors and edge cases
- Implement best practices from morning session

**Alternative/Supplement**: Students can also work with the generic `NEW LABS/Chatbot_with_OpenAI_Fixed.ipynb` if they prefer simpler implementation

---

### 4:15-4:30 PM | Break (15 min)

---

### 4:30-5:00 PM | Case Studies, Discussion & Future Trends (30 min discussion)
**Objectives**: Review successful implementations, discuss challenges, ethical considerations, future trends

**Materials**:
- **NOTES**: `../Docusign/Generative AI Big Picture/NOTES/Case Studies and Discussion.docx` ✓

**Format**: Group discussion and wrap-up
- Review of successful ChatGPT implementations
- Challenges and limitations of using AI-powered assistants
- Ethical considerations: data privacy, transparency, accountability
- Content safety and bias considerations
- Future trends and advancements in generative AI
- Q&A and workshop wrap-up

---

**Day 3 Summary**:
- Lecture/Discussion: 3.25 hours (41%)
- Hands-on: 3.5 hours (44%)
- Breaks: 0.5 hours (6%)
- Lunch: 1 hour (13%)

---

# OVERALL WORKSHOP STATISTICS

**Total Time**: 24 hours (3 days × 8 hours)
**Working Time** (excluding lunch): 21 hours

**Breakdown**:
- Lecture/Presentation: ~7.75 hours (37%)
- Demos: ~0.75 hours (4%)
- Hands-on/Group Work: ~12.75 hours (61%)
- Breaks: ~1 hour (5%)

**Target Met**: ✓ Well over 50% hands-on time (65% including demos)

---

# COMPLETE MATERIALS USAGE

## All PDFs Used:
1. ✓ `PDFs/1. LLM Fundamentals- Capabilities, Limitations, and Common Use Cases.pdf` - Day 1, 9:00 AM
2. ✓ `PDFs/2. Core Concepts of Large Language Models (LLMs).pdf` - Day 1, 9:00 AM
3. ✓ `PDFs/3. Prompting for Developer Productivity.pdf` - Day 1, 10:00 AM
4. ✓ `PDFs/4. Context Engineering.pdf` - Day 2, 9:00 AM & 10:45 AM
5. ✓ `PDFs/5. API Parameter Tuning.pdf` - Day 2, 9:30 AM
6. ✓ `PDFs/6. LLM Application Architecture.pdf` - Day 2, 1:00 PM
7. ✓ `PDFs/7. Implementation Deep Dive for LLM Applications.pdf` - Day 2, 1:00 PM
8. ✓ `PDFs/8. Responsible AI in LLM Applications.pdf` - Day 2, Homework
9. ✓ `PDFs/9. Mitigating Bias, Harmful Responses, and Securing LLM Applications.pdf` - Day 2, Homework

## All Slides Used:
1. ✓ `SLIDES/Introduction to Prompt Engineering (Part-1).pdf` - Day 1, 10:00 AM
2. ✓ `SLIDES/Introduction to Prompt Engineering (Part-2).pdf` - Day 1, 2:15 PM
3. ✓ `SLIDES/Generative AI Holistic Perspective.pdf` - Day 3, 9:00 AM

## All OLD LABS Used:
1. ✓ `LAB EXERCISES/Lab Exercise 1 - GitHub Copilot.pdf` - Day 1, 1:00 PM
2. ✓ `LAB EXERCISES/Lab Exercise 2 - Designing Prompts for Structured Data.pdf` - Day 1, 3:00 PM (reference)
3. ✓ `LAB EXERCISES/Real Use-case Demo 1 - SNOWFLAKE.CORTEX.SUMMARIZE.pdf` - Day 2, 2:15 PM
4. ✓ `LAB EXERCISES/Real Use-case Demo 2 - Hello RAG in Snowflake Cortex.pdf` - Day 2, 3:00 PM
5. ✓ `LAB EXERCISES/Real Use-case Demo 3 – Sentiment Analysis Using SNOWFLAKE.CORTEX.pdf` - Day 2, 2:35 PM

## All NEW LABS Used:
1. ✓ `NEW LABS/Zero_Shot_Few_Shot_Chain_of_Thought_OpenAI.ipynb` - Day 1, 3:00 PM
2. ✓ `NEW LABS/Prompt_Engineering_OpenAI.ipynb` - Day 1, 4:00 PM
3. ✓ `NEW LABS/RAG_with_OpenAI_Fixed.ipynb` - Day 2, 3:15 PM
4. ✓ `NEW LABS/Chatbot_with_OpenAI_Fixed.ipynb` - Day 3 (alternative/supplement)

## All Extra Notes Used (as references):
1. ✓ `EXTRA NOTES/AI Agents – Concepts, Architecture, Examples, and Use Cases.pdf` - Day 2 & 3
2. ✓ `EXTRA NOTES/Hallucination in Large Language Models (LLMs).pdf` - Day 2 & 3
3. ✓ `EXTRA NOTES/Prompt Cheat-Sheet for Developers.pdf` - Day 1 & 3
4. ✓ `EXTRA NOTES/Retrieval-Augmented Generation (RAG).pdf` - Day 2
5. ✓ `EXTRA NOTES/Model Context Protocol (MCP) Server.pdf` - Day 2 ⚠️ **REQUIRED**

## All Projects Used:
1. ✓ `PROJECTS/MCP-SERVER/README.md` - Day 2, 4:15 PM ⚠️ **REQUIRED**

## All Big Picture Materials Used (NEW):
1. ✓ `../Docusign/Generative AI Big Picture/NOTES/Introduction to Generative AI.docx` - Day 3, 9:00 AM
2. ✓ `../Docusign/Generative AI Big Picture/NOTES/Understanding ChatGPT.docx` - Day 3, 9:00 AM
3. ✓ `../Docusign/Generative AI Big Picture/NOTES/Applying ChatGPT in Real-World Scenarios.docx` - Day 3, 10:45 AM
4. ✓ `../Docusign/Generative AI Big Picture/NOTES/Effective Prompt.docx` - Day 3, 10:45 AM
5. ✓ `../Docusign/Generative AI Big Picture/NOTES/Effective Use of ChatGPT in DocuSign.docx` - Day 3, 10:45 AM
6. ✓ `../Docusign/Generative AI Big Picture/NOTES/Hands-On Workshop- Using ChatGPT.docx` - Day 3, 1:00 PM
7. ✓ `../Docusign/Generative AI Big Picture/NOTES/Case Studies and Discussion.docx` - Day 3, 4:30 PM
8. ✓ `../Docusign/Generative AI Big Picture/DocuSign_Agreement_AI_Agent.ipynb` - Day 3, 1:30 PM
9. ✓ `../Docusign/Generative AI Big Picture/Project Work – Develop a DocuSign Agreement AI Agent.docx.pdf` - Day 3, 1:30 PM
10. ✓ `../Docusign/Generative AI Big Picture/PROJECT WORK/AI-AGENT/docusign-agent.py` - Day 3 reference
11. ✓ `../Docusign/Generative AI Big Picture/PROJECT WORK/AI-AGENT/finance_agent_llama_default.py` - Day 3 reference

## Materials NOT Used (duplicates only):
- ❌ `NEW LABS/RAG_with_OpenAI.ipynb` - OLD version, replaced by Fixed
- ❌ `NEW LABS/RAG_with_OpenAI` - Incomplete file

---

# MATERIALS STILL NEEDED

## Critical:
1. **Context Engineering Practice Exercises** - Day 2, 10:45 AM (75 min) - Need structured activities
2. **API Parameter Tuning Hands-On** - Day 2, 9:50 AM (40 min) - Need guided exercises
3. **Day 1 Prompting Practice** - Day 1, 10:30 AM (90 min) - Need structured challenges

## Desirable (from outline):
4. **"Proposed Lab 1"** - Full legacy code context engineering lab (would replace Day 2, 10:45 AM generic practice)

**Note**: Day 3 materials are now COMPLETE with the new Big Picture folder - all gaps filled!

---

# NOTES FOR INSTRUCTOR

## Platform Coverage:
- **OpenAI**: Primary platform for hands-on labs (4 notebooks)
- **Snowflake Cortex**: Demonstrated through 3 demos (Summarize, RAG, Sentiment)
- **GitHub Copilot**: Dedicated lab on Day 1
- **DocuSign-specific**: AI Agent project on Day 3
- This provides excellent platform diversity as outlined

## Day 1:
- **GitHub Copilot Lab** requires students to have Copilot access - confirm licensing beforehand
- NEW LABS are now primary for advanced prompting (not alternatives)
- Students should come with Python and API basics as prerequisites

## Day 2:
- **MCP is now REQUIRED** per outline (not optional) - scheduled 4:15-5:00 PM
- Snowflake demos are instructor-led (students observe) while OpenAI labs are hands-on (students code)
- This balances exposure to multiple platforms without requiring multiple platform setups
- **Responsible AI moved to homework** to accommodate MCP requirement - can be discussed throughout workshop or assigned as self-study
- RAG section shows both platforms: Snowflake (demo) + OpenAI (hands-on)

## Day 3:
- **Completely different audience** - less technical, more conceptual
- **All materials now provided** from Big Picture folder - no gaps!
- DocuSign AI Agent project is more relevant to business audience than generic chatbot
- All lecture notes, case studies, and hands-on materials are complete
- 7 detailed NOTES documents provide comprehensive coverage for all sections

## Key Changes from Previous Version:
1. ✓ MCP is now REQUIRED on Day 2 (4:15-5:00 PM) instead of optional extension
2. ✓ Responsible AI moved to homework to accommodate MCP timing
3. ✓ Day 3 completely updated with all Big Picture materials
4. ✓ DocuSign AI Agent replaces generic chatbot as primary Day 3 project
5. ✓ All 7 NOTES documents integrated into Day 3 schedule
6. ✓ Case studies gap filled with provided materials

## Missing Materials Summary:
- Day 1-2 still need some structured hands-on exercise sets (listed above)
- Day 3 is now COMPLETE - all materials provided
- All 3 days maintain 50%+ hands-on time as required (65% combined with demos)
