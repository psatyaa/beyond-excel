# From Excel to Python to AI: Scaling Business Decisions

An MBA classroom demonstration case study showing how managerial decision-making evolves across three technology tiers using a **Netflix Global Content Acquisition & Licensing Optimization** scenario.

---

## 💡 Core Philosophical Thesis

```text
[ EXCEL ]                 [ PYTHON ]                 [ GENERATIVE AI ]
Understanding the Business  -->  Scaling the Analysis  -->  Communicating & Accelerating Decisions
(Intuition & Pivots)             (Automation & Scale Math)    (Executive Synthesis & NL Q&A)
                                                                    │
                                                                    ▼
                                                    [ HUMAN MANAGER ACCOUNTABILITY ]
                                                      (Final Strategic Governance)
```

1. **Excel = Understanding the Business**: Managers visually manipulate a small catalog (20 titles), build intuition around licensing costs, viewing hours, ad revenue, and priority scoring, and learn how business rules are built cell-by-cell.
2. **Python = Scaling the Analysis**: Code takes the exact same business logic and applies it across 5,000 titles in under **0.02 seconds**, solving multi-constrained budget optimization problems that manual spreadsheet sorting cannot solve.
3. **Generative AI = Communicating & Accelerating Decisions**: LLMs translate numerical optimization outputs into 1-page executive memos, explain trade-offs, and answer natural language scenario questions in plain English.
4. **Managerial Ownership**: Software provides decision support; ultimate financial, strategic, and creative accountability rests with the human business manager.

---

## 📁 Repository Structure

```text
.
├── README.md                      # Project overview and pedagogical vision (this file)
├── instructions.md                # Step-by-step beginner guide to install and run
├── requirements.txt               # Python package dependencies
├── netflix_demo.py                # Live terminal demonstration script (Python optimization reveal)
├── netflix_advanced_analytics.py  # Interactive Streamlit dashboard web application
├── portfolio_optimizer.py         # Underlying portfolio optimization logic module
│
├── Sample/                        # Classroom synthetic datasets & generator code
│   ├── netflix_titles_small.csv   # 20 titles dataset (CSV format)
│   ├── netflix_titles_small.xlsx  # 20 titles Excel workbook (with Pivots & Data Dictionary)
│   ├── netflix_titles_large.csv   # 5,000 titles dataset (CSV format)
│   └── netflix_titles_large.xlsx  # 5,000 titles Excel workbook
│
├── Docs/                          # Documentation & Case Materials
│   ├── PRD/requirements.md        # Product Requirements Document (PRD)
│   └── classroom_demo_guide.md    # Minute-by-minute facilitator walkthrough guide
│
└── output/                        # [IGNORED BY GIT] Generated run outputs & JSON summaries
```

> **Note on Outputs**: All generated runtime outputs (such as CSV summaries, JSON results, and temporary reports) are automatically saved into the `output/` directory, which is excluded from Git version control via `.gitignore`.

---

## 🚀 Getting Started

For step-by-step setup and execution instructions tailored for students and beginners, please read **[instructions.md](instructions.md)**.

### Quick Commands

```bash
# 1. Setup Environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Run Terminal Demo
python netflix_demo.py

# 3. Launch Interactive Streamlit Dashboard
streamlit run netflix_advanced_analytics.py
```

---

## 🎓  Key Takeaways

- **The Excel Limit**: Sorting in Excel leads to a "greedy pick" (e.g., spending 93% of budget on a single mega-title like *Wednesday S2*).
- **The Optimization Advantage**: Algorithmic optimization selects a portfolio of **5 titles instead of 2**, generating **+$800,000 more net value** while saving **$500,000 in unspent cash**.
- **Scale Matters**: If manual sorting leaves $800,000 on the table for 20 titles, millions of dollars are lost when sorting 5,000 titles manually.
