## 🚀 Overview
An autonomous Multi-Agent System designed to diagnose Facebook Ads performance.
It uses a **Planner-Executor-Evaluator** architecture to break down high-level queries (e.g., "Why did ROAS drop?") into actionable insights and creative recommendations.

## 🏗️ Architecture
The system consists of 5 specialized agents:
1. **Planner Agent:** Decomposes the user query into a logical execution plan.
2. **Data Agent:** Interfaces with the CSV dataset to extract quantitative metrics.
3. **Insight Agent:** Analyzes trends to form hypotheses (e.g., "Creative Fatigue").
4. **Evaluator Agent:** Validates hypotheses against statistical evidence.
5. **Creative Generator:** Generates new high-performance ad copy based on winning patterns.

## 📂 Project Structure
```text
├── config/             # Configuration (Thresholds, LLM settings)
├── data/               # Datasets
├── prompts/            # Raw prompt files (Markdown)
├── reports/            # Generated Outputs (Markdown Report, JSON)
├── src/
│   ├── agents/         # Individual Agent Logic
│   └── utils/          # Helper functions
├── tests/              # Unit tests
├── run.py              # Main Entry Point
└── requirements.txt    # Dependencies
🛠️ Quick Start
1. Setup Environment
Bash

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
2. Configure Credentials
Create a .env file:

Plaintext

OPENAI_API_KEY=sk-...
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
3. Run Analysis
Bash

python -m src.run "Why did the Men ComfortMax campaign ROAS drop last week?"
📊 Outputs
After execution, check the reports/ folder:

report.md: A human-readable summary of the findings.

insights.json: Structured data for downstream systems.

creatives.json: Generated ad copy variations.

🧪 Testing
Run the test suite:

Bash

pytest tests/

## Status: Submitted