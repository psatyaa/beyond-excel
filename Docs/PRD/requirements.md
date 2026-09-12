# Product Requirements Document (PRD)

## MBA Classroom Demonstration: "From Excel to Python to AI: Scaling Business Decisions"
### Case Study: Netflix Content Acquisition & Catalog Optimization

---

| Document Attribute | Details |
| :--- | :--- |
| **Document Title** | PRD: From Excel to Python to AI — Scaling Business Decisions |
| **Target Course** | MBA Core / Elective (Digital Transformation, Technology for Managers, Media Strategy) |
| **Target Audience** | MBA Students & Business Executives (Non-Technical / Low-Code background) |
| **Case Domain** | Streaming Media Content Licensing & Budget Optimization (Netflix Case) |
| **Author** | Senior Product Manager, Business Consultant & MBA Lead Instructor |
| **Sample Data Location**| `Sample/netflix_titles_small.xlsx` (20 Titles) & `Sample/netflix_titles_large.xlsx` (5,000 Titles) |
| **Status** | Approved / Ready for Live Classroom Demonstration |
| **Version** | 5.0.0 (Data Dictionary Embedded at Bottom of Small Excel Workbook) |
| **Repository Path** | `Docs/PRD/requirements.md` |

---

## 1. Executive Summary & Core Philosophical Thesis

Modern business managers operate at the intersection of strategic decision-making and scale. While traditional business education relies on Microsoft Excel for building foundational business intuition, modern enterprises generate data volume and complexity that exceed spreadsheet capabilities.

This PRD defines a streamlined interactive MBA classroom demonstration designed to illustrate how managerial decision-making evolves across three technology tiers using a simple Netflix content acquisition scenario:

```
+-------------------------------------------------------------------------------------------------------+
| THE 3-TIER DECISION PROGRESSION MATRIX                                                                |
+--------------------+----------------------------+---------------------------------+-------------------+
| Tier               | Core Function              | Dataset File                    | Student Role      |
+--------------------+----------------------------+---------------------------------+-------------------+
| 1. Excel           | Understanding the Business | `Sample/`                       | Hands-on Formulas,|
|                    | (Intuition & Pivots)       | `netflix_titles_small.xlsx`     | Sorting, Pivots & |
|                    |                            | (20 Titles, Embedded Dict)      | Column Definitions|
+--------------------+----------------------------+---------------------------------+-------------------+
| 2. Python          | Scaling the Analysis       | `Sample/`                       | Code Automation   |
|                    | (Automated Logic & Scale)  | `netflix_titles_large.xlsx`     | & Optimization    |
|                    |                            | / `.csv` (5,000 Titles)         |                   |
+--------------------+----------------------------+---------------------------------+-------------------+
| 3. Generative AI   | Communicating Decisions    | Python Output Data              | Executive Prompting|
|                    | (Executive Briefs & NL QA) | (Summary Tables / JSON)         | & Strategic Review|
+--------------------+----------------------------+---------------------------------+-------------------+
```

### Core Final Takeaway
> **"Excel teaches you how the business logic works on a single file with formulas, pivot tables, and column definitions. Python scales that logic across thousands of rows in milliseconds. AI synthesizes insights and accelerates executive communication. But the human business manager retains final decision accountability."**

---

## 2. Business Background & Case Scenario

**Netflix** licenses movies, series, and documentaries from global creators and studios. Regional content managers are assigned a quarterly content licensing budget (e.g., **\$30 Million** for a small regional pilot, or **\$500 Million** for a global region) and must select which titles to license or renew.

### The Manager's Strategic Question
When presented with candidate titles, managers must decide:
1. **Which titles generate the highest net financial value?** ($\text{Ad Revenue} - \text{Licensing Cost}$)
2. **Which titles protect against subscriber churn?** (High Churn Risk Score)
3. **Which titles to select under a hard financial budget cap?**

---

## 3. Problem Statement & The Excel Scale Bottleneck

1. **Small Scale (20 Titles - `Sample/netflix_titles_small.xlsx`)**:
   - In Excel, managers open the file, inspect the 20 titles, read the **embedded Data Dictionary at the bottom of the table** (rows 24+), review calculated `net_financial_value` formulas, explore the `Pivot_Genre_Summary` and `Pivot_Region_Summary` tabs, sort by `viewing_hours`, and manually pick top titles to fit a \$30M budget.
2. **Large Scale (5,000 Titles - `Sample/netflix_titles_large.xlsx`)**:
   - When opened in Excel at 5,000 titles, pivot tables become cumbersome to refresh, formula recalculations lag, manual sorting is prone to copy-paste errors, and managers **cannot manually optimize the best combination of titles under a \$500M budget constraint**. Greedy sorting in Excel leaves millions of dollars in net value on the table.

---

## 4. Master Data Dictionary & Multi-Tab Excel Structure

The synthetic datasets in `Sample/` include multi-tab formatted Excel workbooks (`netflix_titles_small.xlsx` and `netflix_titles_large.xlsx`).

### Workbook Sheet Layout
1. **`Catalog_Data`**: Primary dataset containing 9 core fields plus calculated metrics (`net_financial_value`, `priority_score`), followed by a formatted **Data Dictionary Block at the bottom (Rows 24+)**.
2. **`Pivot_Genre_Summary`**: Pivot summary table aggregating metrics by Genre (`total_titles`, `total_licensing_cost`, `total_viewing_hours`, `total_ad_revenue`, `total_net_value`, `avg_churn_risk`).
3. **`Pivot_Region_Summary`**: Pivot summary table aggregating metrics by Region (`total_titles`, `total_licensing_cost`, `total_viewing_hours`, `total_ad_revenue`, `total_net_value`).
4. **`Data_Dictionary`**: Dedicated reference tab containing full column specifications.

### Column Definitions (Embedded at Bottom of Small Excel File)

| Column Name | Data Type | Example Value | Description & Business Meaning | Excel Formula / Rule |
| :--- | :--- | :--- | :--- | :--- |
| `title_id` | String | `NFLX-001` | Unique content identification code (Primary Key) | e.g., `NFLX-001` |
| `title_name` | String | `Stranger Things S5` | Title of movie, series, or documentary | Non-null text string |
| `genre` | String | `Sci-Fi` | Content category (`Drama`, `Sci-Fi`, `Comedy`, `Action`, `Unscripted`) | Primary filter dimension |
| `region` | String | `UCAN` | Primary target streaming region (`UCAN`, `LATAM`, `EMEA`, `APAC`) | Regional distribution scope |
| `licensing_cost` | Currency (\$) | `\$45,000,000` | Annual licensing fee or production cost paid by Netflix | Input cost basis ($) |
| `viewing_hours` | Integer | `12,500,000` | Annual historical viewing hours across subscribers | Viewership engagement metric |
| `ad_revenue` | Currency (\$) | `\$62,000,000` | Projected annual revenue from ad tier & subscriptions | Revenue contribution ($) |
| `churn_risk_score` | Integer (1-10)| `10` | Rating of title's ability to retain subscribers (10 = Critical anchor)| Retention priority rating |
| `strategic_score` | Integer (1-10)| `10` | Executive strategic importance rating (Awards, Brand equity) | Executive importance weight |
| `net_financial_value` | Currency (\$) | `\$17,000,000` | Net dollar profit contribution generated by title | `= ad_revenue - licensing_cost` |
| `priority_score` | Float Score | `18.78` | Weighted priority index combining Net Return %, Churn & Strategic weights | `= ((net_financial_value / licensing_cost) * 10) + (churn_risk_score * 0.5) + (strategic_score * 0.5)` |

---

## 5. Phase 1: Excel Demonstration (Understanding the Business & Pivots)

### 5.1 Dataset File
- **`Sample/netflix_titles_small.xlsx`** (20 rows, 4 worksheets, embedded column definitions)

### 5.2 Simple Excel Calculations & Pivot Table Steps
1. **Inspect Data & Embedded Definitions**:
   - Open `Catalog_Data` tab. Review row data (rows 1-21).
   - Scroll to bottom (rows 24+) to read the formatted **Data Dictionary & Column Definitions** block explaining each metric.
2. **Explore Pre-Built Pivot Tables**:
   - Open `Pivot_Genre_Summary` tab to see aggregated licensing spend and viewing hours by Genre.
   - Open `Pivot_Region_Summary` tab to compare UCAN vs EMEA vs APAC vs LATAM spending.
3. **Manual Budget Allocation Exercise**:
   - Give students a **\$30,000,000** budget cap.
   - Students attempt to sort by `viewing_hours` or `net_financial_value` and select titles until spend reaches \$30M.

### 5.3 Clear Breakdown of Excel Limits
- **Attempting Scale with `netflix_titles_large.xlsx`**: Students open the 5,000-row Excel file.
- **Why Excel Fails at Scale**: Pivot tables take noticeable time to update, manual formula drag-and-drop introduces range errors, and simple column sorting produces **suboptimal budget allocation** compared to code.

---

## 6. Phase 2: Python Demonstration (Scaling the Analysis)

### 6.1 Dataset File
- **`Sample/netflix_titles_large.csv` / `.xlsx`** (5,000 rows)

### 6.2 Simple & Clean Python Script (`netflix_demo.py`)

```python
import pandas as pd

# 1. Load the 5,000 title dataset from Sample folder
df = pd.read_csv("Sample/netflix_titles_large.csv")

# 2. Simple Business Calculations
df['net_value'] = df['ad_revenue'] - df['licensing_cost']
df['priority_score'] = ((df['net_value'] / df['licensing_cost']) * 10) + (df['churn_risk_score'] * 0.5) + (df['strategic_score'] * 0.5)

# 3. Sort by Priority Score
df_sorted = df.sort_values(by='priority_score', ascending=False).reset_index(drop=True)

# 4. Apply Budget Constraint ($500M)
budget_limit = 500000000
df_sorted['cumulative_cost'] = df_sorted['licensing_cost'].cumsum()
selected_titles = df_sorted[df_sorted['cumulative_cost'] <= budget_limit]

# 5. Output Key Results
total_spent = selected_titles['licensing_cost'].sum()
total_net_value = selected_titles['net_value'].sum()
titles_count = len(selected_titles)

print(f"--- PYTHON CATALOG OPTIMIZATION RESULTS ---")
print(f"Titles Selected: {titles_count} / 5,000")
print(f"Total Budget Spent: ${total_spent:,.2f} / ${budget_limit:,.2f}")
print(f"Total Net Value Generated: ${total_net_value:,.2f}")
```

---

## 7. Phase 3: AI Enhancement Demonstration (Communicating Decisions)

Generative AI takes the structured output from Python and transforms it into **executive communications, explanatory briefs, and natural language Q&A**.

---

## 8. Live Classroom Demonstration Script (60-Minute Session)

```
+---------------------------------------------------------------------------------------------------+
| 60-MINUTE CLASSROOM AGENDA & DEMO TIMING                                                          |
+-------------------+---------------------------------------------------------+---------------------+
| Time              | Classroom Activity                                      | Tech Focus          |
+-------------------+---------------------------------------------------------+---------------------+
| 00:00 - 00:15     | Act 1: Open `Sample/netflix_titles_small.xlsx`.         | Excel Formulas,     |
| (15 Mins)         | Read column descriptions at bottom, explore Pivots.     | Pivots & Definitions|
+-------------------+---------------------------------------------------------+---------------------+
| 00:15 - 00:35     | Act 2: Open `Sample/netflix_titles_large.xlsx` / CSV.   | Python Execution    |
| (20 Mins)         | Run 5,000-row optimization script in 0.05 seconds.      | & Scalability       |
+-------------------+---------------------------------------------------------+---------------------+
| 00:35 - 00:50     | Act 3: Feed Python summary to LLM.                      | Generative AI       |
| (15 Mins)         | Generate Executive Briefing & test Natural Language QA. | Communication       |
+-------------------+---------------------------------------------------------+---------------------+
| 00:50 - 01:00     | Act 4: Managerial Discussion on AI governance, human    | Managerial          |
| (10 Mins)         | override, and strategic decision accountability.        | Governance          |
+-------------------+---------------------------------------------------------+---------------------+
```

---

## 9. MBA Key Takeaways & Classroom Discussion Questions

### Key Takeaways
1. **Excel is for Business Logic Discovery & Pivot Intuition**: Use Excel to inspect data, read column definitions, build formulas, and explore pivot tables.
2. **Python is for Scale & Automation**: Use Python when data grows beyond single spreadsheets.
3. **AI is for Communication & Decision Acceleration**: Use AI to translate numbers into executive memos.
4. **Managers Retain Final Accountability**: Humans make the final decisions.

---
