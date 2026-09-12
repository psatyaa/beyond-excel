# Step-by-Step Setup & Instruction Guide

## "From Excel to Python to AI: Scaling Business Decisions"

This guide will walk you step-by-step through setting up and running the Netflix case study demonstration. **No prior programming experience is required!**

---

## 📋 Prerequisites

Before starting, make sure you have the following installed on your computer:
1. **Python 3.9 or higher** ([Download Python](https://www.python.org/downloads/))
2. **Git** ([Download Git](https://git-scm.com/downloads))
3. **Microsoft Excel** (or Google Sheets / Apple Numbers) to view `.xlsx` files
4. A Terminal app (macOS / Linux Terminal, or Windows Command Prompt / PowerShell)

---

## 🛠️ Step 1: Open Your Terminal & Navigate to Project

Open your Terminal (macOS/Linux) or Command Prompt (Windows) and navigate to the project directory:

```bash
cd path/to/IIM_Excel_2_Python_Demo
```

---

## 🐍 Step 2: Create & Activate Python Virtual Environment

A virtual environment isolates project software so it doesn't interfere with your computer system settings.

### On macOS / Linux:
```bash
# Create the environment named .venv
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate
```

### On Windows (Command Prompt / PowerShell):
```cmd
# Create the environment named .venv
python -m venv .venv

# Activate the environment (Command Prompt)
.venv\Scripts\activate.bat

# OR Activate the environment (PowerShell)
.venv\Scripts\Activate.ps1
```

> **How to check it worked**: You will see `(.venv)` displayed at the start of your terminal prompt!

---

## 📦 Step 3: Install Required Packages

Install all necessary libraries (Pandas, Streamlit, Matplotlib, SciPy, PuLP) with a single command:

```bash
pip install -r requirements.txt
```

*(This takes about 15–30 seconds to finish).*

---

## 📊 Step 4: Run Phase 1 — Excel Demonstration

1. Open your file browser and go to the `Sample/` folder.
2. Double-click **`Sample/netflix_titles_small.xlsx`** to open it in Microsoft Excel.
3. Observe the sheets:
   - **`Catalog_Data`**: 20 titles with calculated Net Value and Priority Scores. Scroll down to rows 24+ to see the embedded Data Dictionary!
   - **`Pivot_Genre_Summary`**: Aggregated licensing spend and viewing hours by Genre.
   - **`Pivot_Region_Summary`**: Regional spending breakdown (UCAN, EMEA, APAC, LATAM).
4. **Try the Excel Challenge**: Try picking titles to fit under a **$30,000,000 budget cap** by sorting viewing hours descending!

---

## 🐍 Step 5: Run Phase 2 — Python Terminal Demo

Now see how Python scales the exact same analysis across 5,000 titles instantly:

```bash
python netflix_demo.py
```

### What You Will See:
- Python analyzes 5,000 titles in **less than 0.02 seconds**!
- Shows baseline sorting vs optimal portfolio performance.
- Automatically saves result files into the `output/` folder (`output/small_summary.json` and `output/large_summary.json`).

---

## 🌐 Step 6: Run Phase 2 — Interactive Web Dashboard

Launch the interactive web application built with Streamlit:

```bash
streamlit run netflix_advanced_analytics.py
```

### What Happens:
1. Streamlit will launch a local web server.
2. Your browser will open automatically to **`http://localhost:8501`**.
3. Use the top radio buttons to switch between **"20 titles · $30M budget"** and **"5,000 titles · $500M budget"**.
4. Explore interactive metric cards, portfolio tables, and allocation bar charts!

*(Press `Ctrl + C` in your terminal when you want to close the web dashboard).*

---

## 🤖 Step 7: Run Phase 3 — Generative AI Briefing

1. Open your browser and go to an AI tool (ChatGPT, Google Gemini, or Claude).
2. Copy the JSON output generated in `output/large_summary.json` (or printed by `netflix_demo.py`).
3. Paste the following prompt into the AI:

```text
Act as Chief Content Officer at Netflix. Below are the results of our Q4 content catalog optimization model:

{
  "titles_funded": 23,
  "total_candidate_titles": 5000,
  "budget_allocated": "$487,055,528.00",
  "budget_limit": "$500,000,000.00",
  "net_value_generated": "$269,442,035.00",
  "top_cut_example": "Secret Chronicles 3"
}

Write a 3-bullet executive summary memorandum explaining our Q4 licensing allocation strategy and why high-cost, lower-engagement titles were deprioritized.
```

4. Watch the AI transform raw optimization numbers into structured executive prose in seconds!

---

## ❓ Frequently Asked Questions & Troubleshooting

### Q: Why do I get `command not found: streamlit`?
**A**: Make sure you activated the virtual environment first (`source .venv/bin/activate`). If `.venv` is activated, your prompt will show `(.venv)` at the beginning.

### Q: How do I stop the Streamlit dashboard?
**A**: Go to your terminal window and press `Ctrl + C`.

### Q: How do I exit the virtual environment when finished?
**A**: Type `deactivate` in your terminal and press Enter.

### Q: Will my generated output files be uploaded to GitHub?
**A**: No! The `.gitignore` file automatically excludes the `output/` directory and `.venv/` folder so your GitHub repository stays clean.
