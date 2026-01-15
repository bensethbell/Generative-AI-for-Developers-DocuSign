# Handoff: GitHub Repository Setup

## Current State

### Repo 1: Generative-AI-for-Developers-DocuSign
**Location:** `/Users/mannasethsotsky/Dropbox/Ben Bell/Documents/DataScienceTeaching/JobHuntPersonal/Pluralsight/Generative-AI-for-Developers-DocuSign`

**Git Status:** Initialized with 3 branches:
- `main` - Original Google Drive content (clean baseline)
- `dev` - Modified version with all improvements (SETUP.md, requirements.txt, NEW LABS, etc.)
- `student` - Clean version for distribution (no ARCHIVE, PREP, schedule)

**Pending Changes on `dev` branch:**
```
modified:   NEW LABS/Chatbot_with_OpenAI_Fixed.ipynb
modified:   NEW LABS/Prompt_Engineering_OpenAI.ipynb

Untracked:
  ARCHIVE/SQL_LAB_PDFS/
  LAB EXERCISES/Real Use-case Demo 1 - SQLite Summarization LLM function.pdf
  LAB EXERCISES/Real Use-case Demo 2- Hello RAG with SQLite + OpenAI.pdf
  LAB EXERCISES/Real Use-case Demo 3 – Sentiment Analysis Using SQLite + OpenAI.pdf
  NEW LABS/SQL_RAG_SQLite.ipynb
  NEW LABS/SQL_Sentiment_SQLite.ipynb
  NEW LABS/SQL_Summarization_SQLite.ipynb
  NEW LABS/support_tickets.db
  PREP/SQL_AI_LABS_HANDOFF.md
  PREP/GITHUB_SETUP_HANDOFF.md (this file)
```

**No remote configured yet.**

### Repo 2: Docusign (other workshop)
**Location:** `/Users/mannasethsotsky/Dropbox/Ben Bell/Documents/DataScienceTeaching/JobHuntPersonal/Pluralsight/Docusign`

**Status:** Unknown - needs exploration. Previous LLM instance had path access issues.

---

## Tasks To Complete

### 1. Explore the Other Docusign Folder
```bash
cd "/Users/mannasethsotsky/Dropbox/Ben Bell/Documents/DataScienceTeaching/JobHuntPersonal/Pluralsight/Docusign"
ls -la
```

Determine:
- What is this workshop about?
- Is it related to the Generative AI workshop?
- Does it have its own git repo?
- Should it be combined or kept separate?

### 2. Decision: One Repo vs Two Repos

**Recommendation: Separate repos** (unless workshops are tightly coupled)

| Factor | One Repo | Separate Repos |
|--------|----------|----------------|
| Student cloning | Clone everything | Clone only what needed |
| Branch strategy | Complex | Clean per-workshop |
| Sharing | All or nothing | Selective |

### 3. Commit Pending Changes (Generative AI Workshop)

```bash
cd "/Users/mannasethsotsky/Dropbox/Ben Bell/Documents/DataScienceTeaching/JobHuntPersonal/Pluralsight/Generative-AI-for-Developers-DocuSign"

# Stage all new files
git add -A

# Commit
git commit -m "Add SQLite-based AI labs as Snowflake alternatives

- SQL_Summarization_SQLite.ipynb: Text summarization with SQLite + OpenAI
- SQL_RAG_SQLite.ipynb: RAG pipeline with SQLite vector storage
- SQL_Sentiment_SQLite.ipynb: Sentiment analysis with SQL aggregations
- Corresponding PDF lab guides
- SQL_AI_LABS_HANDOFF.md: Instructions for creating these labs
- Minor fixes to existing notebooks"
```

### 4. GitHub CLI Authentication

The `gh` CLI was installed via `brew install gh` but may not be authenticated yet.

Check:
```bash
gh auth status
```

If not authenticated:
```bash
gh auth login
# Select: GitHub.com → HTTPS → Login with web browser
# Follow prompts
```

### 5. Create GitHub Repository

**Option A: Using gh CLI (if authenticated)**
```bash
cd "/Users/mannasethsotsky/Dropbox/Ben Bell/Documents/DataScienceTeaching/JobHuntPersonal/Pluralsight/Generative-AI-for-Developers-DocuSign"

# Create private repo
gh repo create Generative-AI-for-Developers-Workshop --private --source=. --push

# Or create and push all branches
gh repo create Generative-AI-for-Developers-Workshop --private
git remote add origin https://github.com/USERNAME/Generative-AI-for-Developers-Workshop.git
git push -u origin main dev student
```

**Option B: Manual (if gh not working)**
1. Go to github.com → New Repository
2. Name: `Generative-AI-for-Developers-Workshop`
3. Private (recommended for workshop materials)
4. Do NOT initialize with README
5. Copy the HTTPS URL
6. Run:
```bash
git remote add origin <URL>
git push -u origin main dev student
```

### 6. Repeat for Second Workshop (if separate)

If the Docusign folder is a separate workshop and doesn't have git:
```bash
cd "/Users/mannasethsotsky/Dropbox/Ben Bell/Documents/DataScienceTeaching/JobHuntPersonal/Pluralsight/Docusign"

git init
# Create .gitignore (copy from other repo or create new)
git add -A
git commit -m "Initial commit: [Workshop Name]"

gh repo create [repo-name] --private --source=. --push
```

---

## Branch Strategy Explanation

For each workshop repo:

```
main (original/baseline content)
  │
  └── dev (instructor version with all materials)
        │
        └── student (clean version for distribution)
```

- **main**: Original source materials, clean baseline
- **dev**: All modifications, instructor notes, archives, prep materials
- **student**: What students clone - no ARCHIVE, PREP, or instructor-only files

Students should clone and work from `student` branch:
```bash
git clone -b student https://github.com/USER/repo.git
```

---

## File Locations Summary

| File | Purpose |
|------|---------|
| `PREP/SQL_AI_LABS_HANDOFF.md` | Instructions for creating SQLite AI labs |
| `PREP/GITHUB_SETUP_HANDOFF.md` | This file - GitHub setup instructions |
| `SETUP.md` | Student environment setup guide |
| `requirements.txt` | Python dependencies |

---

## Questions for User

1. What is the content of the other Docusign folder? (Need to explore it)
2. Should workshops be combined or separate repos?
3. What GitHub username/org should repos be created under?
4. Public or private repositories?
