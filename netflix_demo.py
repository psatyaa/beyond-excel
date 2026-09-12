"""Classroom reveal: one financial objective, first 20 titles, then 5,000.

Run: python netflix_demo.py [--dataset small|large|both]
"""
import argparse
import json
from pathlib import Path
from portfolio_optimizer import load_catalog, optimize_portfolio, select_by_viewing_hours

SAMPLE = Path(__file__).resolve().parent / 'Sample'


def reveal(size):
    budget = 30_000_000 if size == 'small' else 500_000_000
    catalog = load_catalog(SAMPLE / f'netflix_titles_{size}.csv')
    baseline = select_by_viewing_hours(catalog, budget)
    result = optimize_portfolio(catalog, budget)
    selected = result['selected']
    baseline_value = int(baseline.net_financial_value.sum())
    value = int(selected.net_financial_value.sum())
    spend = int(selected.licensing_cost.sum())

    print('\n' + '=' * 78)
    print('REVEAL 1: THE BETTER COMBINATION' if size == 'small'
          else 'REVEAL 2: THE SAME METHOD AT SCALE')
    print(f'{len(catalog):,} candidate titles | Budget: ${budget:,.0f}')
    print('Synthetic teaching data | Maximize projected revenue minus cost')
    print('=' * 78)
    print(f"{'Method':<29} {'Titles':>7} {'Spend':>17} {'Projected value':>19}")
    for label, portfolio in [('Viewing-hours sort (baseline)', baseline),
                             ('Financial optimizer', selected)]:
        print(f'{label:<29} {len(portfolio):>7} '
              f'${int(portfolio.licensing_cost.sum()):>16,} '
              f'${int(portfolio.net_financial_value.sum()):>18,}')
    print(f'\nVALUE GAIN: ${value - baseline_value:,.0f}'
          + (f' ({(value - baseline_value) / baseline_value:.1%})' if baseline_value > 0 else ''))
    print(f'UNSPENT BUDGET: ${budget - spend:,.0f}')
    print(f"Solver: {result['status']} | Gap: {result['gap']:.2%} | "
          f"Solve time: {result['seconds']:.3f}s (varies by machine)")

    visible = selected if size == 'small' else selected.head(5)
    print('\nFUNDED TITLES' + (' (first 5 by projected net value)' if size == 'large' else ''))
    for row in visible.itertuples():
        print(f'  {row.title_name:<28} Cost ${row.licensing_cost:>11,} | '
              f'Value ${row.net_financial_value:>11,}')
    if size == 'small':
        print('\nDISCUSS: Would you accept this portfolio, or pay for a strategic override?')
    else:
        print('\nSame objective and budget rule; more candidates. Retention and strategy')
        print('are not optimized here: managers must make those requirements explicit.')

    summary = {
        'dataset': size, 'synthetic_data': True,
        'objective': 'maximize projected revenue minus licensing cost',
        'constraints': 'each title selected at most once; total cost within budget',
        'candidate_titles': len(catalog), 'budget_limit': budget,
        'baseline': {'method': 'viewing-hours descending, skip unaffordable titles',
                     'titles_funded': len(baseline),
                     'budget_allocated': int(baseline.licensing_cost.sum()),
                     'projected_net_value': baseline_value},
        'optimizer': {'status': result['status'], 'relative_gap': result['gap'],
                      'titles_funded': len(selected), 'budget_allocated': spend,
                      'projected_net_value': value},
        'incremental_projected_value': value - baseline_value,
        'limitations': ['Revenue forecasts are treated as certain and additive.',
                        'Retention, brand benefits, and audience overlap are not modeled.',
                        'Projected contribution is not realized profit.'],
    }
    output = Path(__file__).resolve().parent / 'output'
    output.mkdir(exist_ok=True)
    selected.to_csv(output / f'{size}_selected_titles.csv', index=False)
    (output / f'{size}_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(f"\nAI evidence saved to: {output / f'{size}_summary.json'}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', choices=['small', 'large', 'both'], default='both')
    args = parser.parse_args()
    for size in (['small', 'large'] if args.dataset == 'both' else [args.dataset]):
        reveal(size)


if __name__ == '__main__':
    main()
