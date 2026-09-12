"""Run: .venv/bin/python -m streamlit run netflix_advanced_analytics.py"""
from pathlib import Path

import pandas as pd
import streamlit as st

from portfolio_optimizer import load_catalog, optimize_portfolio, select_by_viewing_hours

st.set_page_config(page_title='Netflix | Portfolio decisions', page_icon='🎬', layout='wide')
st.title('Netflix content portfolio')
st.caption('Synthetic classroom case · Same calculations as the terminal demo')
scenario = st.radio('Choose the reveal', ['20 titles · $30M budget', '5,000 titles · $500M budget'],
                    horizontal=True)
size, budget = ('small', 30_000_000) if scenario.startswith('20 ') else ('large', 500_000_000)
path = Path(__file__).resolve().parent / 'Sample' / f'netflix_titles_{size}.csv'


# 1. Reuse the analysis. Cache results so dashboard interactions do not re-solve.
@st.cache_data(show_spinner='Comparing portfolio combinations…', ttl=3600)
def analyze(csv_path, modified_at, budget):
    catalog = load_catalog(csv_path)
    baseline = select_by_viewing_hours(catalog, budget)
    result = optimize_portfolio(catalog, budget)
    return baseline, result


baseline, result = analyze(str(path), path.stat().st_mtime_ns, budget)
selected = result['selected']
value = int(selected.net_financial_value.sum())
baseline_value = int(baseline.net_financial_value.sum())
spend = int(selected.licensing_cost.sum())

# 2. Replace print statements with dashboard components.
st.subheader('What does a better combination buy?')
value_card, gain_card, spend_card, titles_card = st.columns(4)
value_card.metric('Projected net value', f'${value / 1e6:,.2f}M')
gain_card.metric('Gain over viewing-hours sort', f'${(value - baseline_value) / 1e6:,.2f}M',
                 f'{(value / baseline_value - 1):.1%}' if baseline_value > 0 else None)
spend_card.metric('Budget spent', f'${spend / 1e6:,.2f}M',
                  help=f'Exact spend: ${spend:,}. Unspent: ${budget - spend:,}.')
titles_card.metric('Titles funded', len(selected))
st.caption(f"Solver: {result['status']} · Relative gap: {result['gap']:.4%} · "
           f"Solve time: {result['seconds']:.2f}s · Unspent budget: ${budget - spend:,}")

comparison = pd.DataFrame({
    'Method': ['Viewing-hours sort', 'Financial optimizer'],
    'Projected net value ($M)': [baseline_value / 1e6, value / 1e6],
}).set_index('Method')
chart, explanation = st.columns([2, 1])
with chart:
    st.bar_chart(comparison, color='#E50914', height=290, horizontal=True)
with explanation:
    st.markdown('**One objective, one budget rule**')
    st.write('Maximize projected revenue minus licensing cost. Each title can be selected once.')
    st.write('The baseline sorts by viewing hours and skips titles that do not fit. '
             'The optimizer compares combinations under the same budget.')
    st.info('Would you give up projected financial value to secure a strategically important title?')

# 3. The same DataFrames also become interactive tables and allocation charts.
funded_tab, baseline_tab, allocation_tab = st.tabs(['Optimized portfolio', 'Baseline portfolio', 'Allocation'])
columns = ['title_name', 'genre', 'region', 'licensing_cost', 'net_financial_value']
labels = dict(zip(columns, ['Title', 'Genre', 'Region', 'Licensing cost ($)', 'Projected net value ($)']))
for tab, portfolio in [(funded_tab, selected), (baseline_tab, baseline)]:
    with tab:
        st.caption(f'{len(portfolio)} titles · Spend USD {int(portfolio.licensing_cost.sum()):,} · '
                   f'Projected net value USD {int(portfolio.net_financial_value.sum()):,}')
        st.dataframe(portfolio[columns].rename(columns=labels), hide_index=True,
                     column_config={name: st.column_config.NumberColumn(format='localized')
                                    for name in ['Licensing cost ($)', 'Projected net value ($)']})
with allocation_tab:
    genre, region = st.columns(2)
    for panel, field in [(genre, 'genre'), (region, 'region')]:
        with panel:
            st.markdown(f'**Optimized spending by {field} ($M)**')
            st.bar_chart(selected.groupby(field).licensing_cost.sum().div(1e6), color='#E50914')

st.caption('Projected contribution is not realized profit. Forecasts are treated as certain and additive. '
           'Retention, brand benefits, and audience overlap are not modeled.')
