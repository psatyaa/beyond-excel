# Python reveal for the 10-minute classroom demo

Use synthetic data throughout. The objective is projected revenue minus licensing cost under a hard budget. Retention and strategic scores are descriptive, not part of this objective.

## Setup

From the project directory:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Live commands

After the Excel viewing-hours selection, reveal the result on the same 20 titles:

```bash
.venv/bin/python netflix_demo.py --dataset small
```

Expected: baseline $11.6M projected value at $30M spend; optimal portfolio $12.4M at $29.5M spend. Show the five funded titles and ask whether $800K of additional projected value justifies the portfolio change.

Then show the same method at scale:

```bash
.venv/bin/python netflix_demo.py --dataset large
```

For the supplied 5,000-title dataset: the viewing-hours baseline yields $113,997,672; the financial optimum yields $301,397,319 at $499,999,116 spend across 24 titles. Explain that this compares selection methods on synthetic forecasts; it does not measure a real business gain or Excel's computational limits.

Run both reveals consecutively with `.venv/bin/python netflix_demo.py`.

The solver reports whether optimality is proven and its relative gap. Runs have a 20-second solver limit; a time-limited feasible result is labeled accordingly. Runtime varies by machine. The optimizer chooses combinations, rather than taking a prefix of a ranking.

## AI handoff

Each run writes `Sample/results/small_summary.json` or `large_summary.json`, plus a CSV of funded titles. Paste the small summary into AI with:

> Write three bullets: financial result, strategic tradeoff, and one assumption to validate. Use only this evidence. Do not invent retention benefits or explanations for individual exclusions. Respect the solver's reported optimality status.

## Ten-minute timing

- 0–1: $30M decision challenge and show of hands.
- 1–3: Excel formula and audience-led portfolio.
- 3–4: Python small-dataset reveal.
- 4–5: Python large-dataset reveal.
- 5–6: Discuss the opportunity cost of insisting on Wednesday.
- 6–8: AI briefing and evidence check.
- 8–10: Student recommendation and managerial accountability.

## Optional advanced visuals

Run the live dashboard:

```bash
.venv/bin/python -m streamlit run netflix_advanced_analytics.py
```

Switch between 20 titles / $30M and 5,000 titles / $500M. Both scenarios use the exact same loading, baseline selection, and optimizer functions as the terminal demo. The dashboard shows projected value, improvement, spend, funded titles, the baseline comparison, and allocation by genre and region. Results are cached to make switching fast after the first solve.

For the classroom code walkthrough, show the three numbered sections in `netflix_advanced_analytics.py`: reuse the analysis, replace print statements with `st.metric` and `st.bar_chart`, then display the existing DataFrames with `st.dataframe`. Streamlit supplies the browser layout and interactions. This command replaces the previous static HTML/chart export; the dashboard needs its local server running.

Before class, run both reveals and keep the output available as a fallback. The existing Excel files contain static calculated values and summary sheets; add a live formula manually if demonstrating formula editing.
