# Classroom Demonstration Facilitator Guide

> **Updated Python demo:** Use [the 10-minute run guide](python_reveal_10min.md) for the current small- and large-dataset reveals and AI handoff. The scripts now use financial portfolio optimization, replacing the priority-ranking method and its historical figures below. The longer agenda below is retained as reference.

## "From Excel to Python to AI: Scaling Business Decisions"
### Case Study: Netflix Content Acquisition & Catalog Optimization

---

| Guide Metadata | Details |
| :--- | :--- |
| **Session Length** | 60 Minutes (Modular for 45 to 90 min sessions) |
| **Target Audience** | MBA Students & Business Executives (Non-Technical / Low-Code background) |
| **Core Software Required**| Microsoft Excel, Terminal / Python Environment, Web Browser (LLM Interface) |
| **Sample Data Files** | `Sample/netflix_titles_small.xlsx`, `Sample/netflix_titles_large.xlsx` / `.csv` |
| **Python Demo Script** | `netflix_demo.py` (Simple 50-Line Walkthrough) |
| **Python Advanced Script**| `netflix_advanced_analytics.py` (Visual Charts & HTML Dashboard Export) |

---

## Pre-Class Room Setup (5 Minutes Before Class)

1. **Laptop Display / Projector Setup**:
   - Open **Microsoft Excel** with `Sample/netflix_titles_small.xlsx`.
   - Open **Terminal** or VS Code navigated to the workspace directory.
   - Open a browser tab with your preferred AI interface (Google Gemini, ChatGPT, or Claude).
2. **Pedagogical Positioning**:
   - Write the 4-tier thesis on the board:
     - **Excel** = *Understanding the Business*
     - **Python** = *Scaling the Analysis*
     - **AI** = *Communicating & Accelerating Decisions*
     - **Manager** = *Accountable Decision-Maker*

---

## STEP 1: Excel Phase (00:00 - 00:15) — Understanding the Business

### 1.1 What to Open
- File: `Sample/netflix_titles_small.xlsx` (in Microsoft Excel).

### 1.2 What to Say to Students
> *"Welcome everyone. Imagine you are a Content Acquisition Manager at Netflix deciding which titles to license under a budget. Before deploying advanced software, managers use Excel to inspect data and build foundational business logic."*

### 1.3 What to Click & Point Out on Screen
1. **Show the 20 Titles** on the `Catalog_Data` tab (*Stranger Things S5*, *Squid Game S2*, *Wednesday S2*, etc.).
2. **Scroll to Rows 24+** (Bottom of table):
   - Highlight the **DATA DICTIONARY & COLUMN DEFINITIONS** block.
   - Explain key fields: `licensing_cost`, `viewing_hours`, `ad_revenue`, `churn_risk_score` (1-10 retention weight), `strategic_score` (1-10 award weight).
3. **Inspect the Calculated Formulas**:
   - Click Cell `J2` (`net_financial_value`): Point out `= G2 - E2` (`ad_revenue - licensing_cost`).
   - Click Cell `K2` (`priority_score`): Point out `= ((J2/E2)*10) + (H2*0.5) + (I2*0.5)`. Show how formulas build business rules cell-by-cell.

### 1.4 Explore Pre-Built Pivot Tables
1. **Click Tab 2 (`Pivot_Genre_Summary`)**: Show aggregated licensing spend and viewing hours by Genre (Drama, Sci-Fi, Comedy, Action). Ask class: *"Which genre commands the most spend versus viewing hours?"*
2. **Click Tab 3 (`Pivot_Region_Summary`)**: Show spending split across UCAN, EMEA, APAC, and LATAM.

---

### 1.5 The Excel Budget Challenge — Exact Answer & Demonstration

#### The Challenge Scenario
Give students a **$30,000,000 Content Budget Cap** and ask: *"Which titles should we license to maximize our net financial value?"*

#### What Happens in Excel (The Naïve Sorting Flaw)
When students sort `Catalog_Data` by `viewing_hours` descending and try to select titles:
1. **Rank 1**: *Squid Game S2* (Cost: **$35,000,000**) $\rightarrow$ **Too Expensive!** Exceeds \$30M budget cap. Skipped!
2. **Rank 2**: *Stranger Things S5* (Cost: **$45,000,000**) $\rightarrow$ **Too Expensive!** Exceeds \$30M budget cap. Skipped!
3. **Rank 3**: *Wednesday S2* (Cost: **$28,000,000**) $\rightarrow$ **Fits in Budget!** Selected! (Cost: \$28M | Net Value: \$11,000,000). Remaining Budget = **$2,000,000**.
4. **Rank 4-16**: All mega titles (*Bridgerton S3*, *The Witcher S4*, *The Crown S6*) exceed the remaining \$2M budget.
5. **Rank 17**: *Baking Championship* (Cost: **$2,000,000**) $\rightarrow$ **Fits Remaining Budget!** Selected! (Cost: \$2M | Net Value: \$600,000).

```
===================================================================================
NAÏVE EXCEL SORTING RESULT ($30M BUDGET CAP)
===================================================================================
1. Wednesday S2             | Cost: $28,000,000 | Net Value: $11,000,000
2. Baking Championship      | Cost:  $2,000,000 | Net Value:   $600,000
-----------------------------------------------------------------------------------
TOTAL SPENT: $30,000,000 (100%) | TITLES: 2 | TOTAL NET VALUE: $11,600,000
===================================================================================
```

#### The Optimal Answer (Why Python / Optimization Wins)
Show students the optimal combination calculated by Python / Optimization logic:

```
===================================================================================
OPTIMAL PORTFOLIO ALLOCATION ($30M BUDGET CAP)
===================================================================================
1. Drive to Survive S6      | Cost: $8,000,000 | Net Value: $3,000,000 (Docuseries)
2. Anime Legend Revival     | Cost: $7,500,000 | Net Value: $2,300,000 (Action)
3. Love is Blind S6         | Cost: $6,000,000 | Net Value: $3,500,000 (Unscripted)
4. Tokyo Heist Thriller     | Cost: $5,000,000 | Net Value: $1,800,000 (Crime)
5. Seoul Reality Dating     | Cost: $3,000,000 | Net Value: $1,800,000 (Unscripted)
-----------------------------------------------------------------------------------
TOTAL SPENT: $29,500,000 (98.3%) | TITLES: 5 | TOTAL NET VALUE: $12,400,000
===================================================================================
```

#### Key Takeaways for Students
1. **+ $800,000 More Net Profit**: The optimal portfolio generates **$12,400,000** vs Excel's **$11,600,000**.
2. **Saved $500,000 Cash**: Optimal allocation leaves \$500k unspent in liquidity.
3. **5 Titles vs 2 Titles**: Diversifies subscriber engagement across 5 genres instead of putting 93% of capital into 1 show (*Wednesday S2*).

---

## STEP 2: Python Phase (00:15 - 00:35) — Scaling & Advanced Visual Analytics

### 2.1 Simple Demo Run
Run the simple walkthrough script in Terminal:
```bash
python netflix_demo.py
```
- **Highlight**: 5,000 titles analyzed and optimized in **0.014 seconds**!

### 2.2 Advanced Visual Analytics Run
Run the separate advanced analytics script to generate executive charts & interactive dashboard:
```bash
python netflix_advanced_analytics.py
```

#### What It Generates:
1. **Genre & Regional Breakdown Tables** printed in terminal.
2. **Visual Charts Saved to `Sample/charts/`**:
   - `1_genre_spend_vs_value.png`: Bar chart comparing Licensing Spend vs Net Value by Genre.
   - `2_priority_vs_cost_cutoff.png`: Scatter plot showing Priority Index vs Licensing Cost cutoff line.
   - `3_regional_spend_donut.png`: Donut chart showing Regional Capital Allocation.
3. **Interactive HTML Dashboard**:
   - `Sample/netflix_executive_dashboard.html`: Open in any web browser for interactive filtering and drill-down!

---

## STEP 3: The AI Phase (00:35 - 00:50) — Communicating & Accelerating Decisions

### 3.1 What to Open
- Web browser with AI Interface (Gemini, ChatGPT, or Claude).

### 3.2 What to Say to Students
> *"Python gives us numbers and charts, but executives make decisions based on clear strategic communication. Generative AI converts computational outputs into C-suite briefings and lets managers test scenarios in plain English."*

### 3.3 Live Prompting Demo 1: Executive Memorandum
Copy and paste the JSON output printed by `netflix_demo.py` into the LLM prompt:

```text
Act as Chief Content Officer at Netflix. Our Python catalog optimization model analyzed 5,000 titles under a $500M budget cap and produced the following results:

{
  "titles_funded": 23,
  "total_candidate_titles": 5000,
  "budget_allocated": "$487,055,528.00",
  "budget_limit": "$500,000,000.00",
  "net_value_generated": "$269,442,035.00",
  "top_cut_example": "Secret Chronicles 3"
}

Write a concise 3-bullet executive summary memo explaining our Q4 licensing allocation strategy and why high-cost, lower-engagement titles were deprioritized.
```

---

## STEP 4: Managerial Governance & Wrap-Up (00:50 - 01:00)

### 4.1 Cold-Call Discussion Questions
1. **The Human Override**: *"If the Python model deprioritizes an Oscar-nominated documentary because of lower immediate viewing hours, should the CCO override the algorithm? What are the brand equity implications?"*
2. **Technology Selection**: *"When should a business team transition from Excel to Python? What are the warning signs of spreadsheet maturity failure?"*
3. **AI Accountability**: *"If an LLM assistant drafts a memo with a wrong viewership metric, who is accountable—the AI vendor, the data team, or the manager?"*

### 4.2 Closing Philosophy Statement
> **"Excel teaches you how the business logic works. Python scales the analysis to enterprise volume. AI synthesizes insights and accelerates executive communication. But the human business manager retains final decision accountability."**
