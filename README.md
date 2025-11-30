# Kasparro - Agentic Facebook Performance Analyst

**An autonomous Multi-Agent System designed to diagnose Facebook Ads performance, identify trends, and generate data-backed creative recommendations.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-v0.1-green)
![Status](https://img.shields.io/badge/Status-Submission%20Ready-brightgreen)

---

## 🏗️ Architecture

The system utilizes a **Planner-Executor-Evaluator** architecture where specialized agents collaborate to solve the user's query.

```ascii
User Query 
    │
    ▼
[ 🧠 Planner Agent ] ───> Breaks query into execution steps
    │
    ├── [ 📊 Data Agent ] ──────> Extracts stats (Spend, ROAS, CTR) from CSV
    │
    ├── [ 🧐 Insight Agent ] ───> Analyzes trends & forms hypotheses (e.g., "Creative Fatigue")
    │
    ├── [ ⚖️ Evaluator Agent ] ─> Validates hypotheses against data evidence
    │
    └── [ 🎨 Creative Gen ] ────> Generates new Ad Copy for underperforming assets
    │
    ▼
[ 📄 Final Report ] ───> JSON Insights + Markdown Summary
```

## 🚀 Quick Start

### 1. Prerequisites
   
  Python 3.10 or higher

  A valid OpenAI API Key

### 2. Installation
```
# 1. Clone the repository
git clone <https://github.com/saikarthik333/kasparro-agentic-fb-analyst-Sai-Karthik-Motapothula>
cd kasparro-agentic-fb-analyst-Sai-Karthik-Motapothula

# 2. Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a .env file in the root directory:
```
OPENAI_API_KEY=sk-your-key-here
LANGFUSE_PUBLIC_KEY=pk-lf-... (Optional for tracing)
LANGFUSE_SECRET_KEY=sk-lf-... (Optional for tracing)
```
4. Run the Analysis
Execute the main orchestrator with a query:
```
python -m src.run "Why did ROAS drop last week for the ComfortMax campaign?"
```
## ⚙️ Features & Engineering Decisions
### 1. Robust "Mock/Offline" Mode
To ensure system stability and cost-efficiency during development, the agents are equipped with a Fallback Layer.

Live Mode: If a valid API key with quota is detected, agents use GPT-3.5/4 to reason dynamically.

Mock Mode: If the API returns Rate Limit (429) or Connection errors, the system automatically switches to deterministic mock data. This allows the pipeline to be tested end-to-end without fragility.

### 2. Modularity
Prompts as Code: All LLM prompts are stored in prompts/*.md to separate logic from instruction.

Configurable Thresholds: Sensitivity for "Low CTR" or "ROAS Drop" is managed in config/config.yaml.

## 📂 Project Structure
```

├── config/             # Configuration (Thresholds, LLM settings)
├── data/               # Datasets (synthetic_fb_ads_undergarments.csv)
├── prompts/            # Markdown prompt templates
├── reports/            # Generated outputs
│   ├── report.md       # Final human-readable analysis
│   ├── insights.json   # Machine-readable findings
│   └── creatives.json  # AI-generated ad copy
├── src/
│   ├── agents/         # Individual Agent Logic (Planner, Insight, etc.)
│   └── utils/          # Helper functions (Prompt loaders)
├── tests/              # Unit tests
├── run.py              # Main Entry Point
└── requirements.txt    # Dependencies
```
## 📊 Example Output
After running the script, check the reports/ folder.

Snippet from reports/report.md:

Diagnosis: ROAS dropped by 15% due to a decline in CTR. Hypothesis: Creative Fatigue: The current ad visuals are no longer engaging the audience. Recommended 

Action: Launch new creatives focused on the "Comfort & Durability" angle.

## 🧪 Testing
Run the test suite to verify data loading and agent initialization:
```
pytest tests/
```
---

**Author:** Motapothula Sai Karthik

**LinkedIn:** [saikarthik333](https://www.linkedin.com/in/saikarthik333/) \
**GitHub:** [saikarthik333](https://github.com/saikarthik333) \
**Email:**[saikarthikmotapothula333@gmail.com](mailto:saikarthikmotapothula333@gmail.com)

---
## 📜 License
Internal Assignment for Kasparro AI.
