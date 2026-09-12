import itertools
import unittest
from pathlib import Path
import pandas as pd
from portfolio_optimizer import load_catalog, optimize_portfolio, select_by_viewing_hours

ROOT = Path(__file__).resolve().parents[1]


class PortfolioTests(unittest.TestCase):
    def test_classroom_reveal(self):
        data = load_catalog(ROOT / 'Sample/netflix_titles_small.csv')
        baseline = select_by_viewing_hours(data, 30_000_000)
        self.assertEqual(baseline.net_financial_value.sum(), 11_600_000)
        result = optimize_portfolio(data, 30_000_000)
        self.assertEqual(result['status'], 'proven optimal')
        self.assertEqual(result['selected'].net_financial_value.sum(), 12_400_000)
        self.assertEqual(result['selected'].licensing_cost.sum(), 29_500_000)
        self.assertEqual(len(result['selected']), 5)

    def test_against_exhaustive_portfolios(self):
        # Independent enumeration checks selection, zero budget, and negative values.
        costs = [8, 6, 5, 3, 2, 1]
        values = [9, 8, 7, 4, -2, 0]
        data = pd.DataFrame({'licensing_cost': [x * 1_000_000 for x in costs],
                             'net_financial_value': [x * 1_000_000 for x in values]})
        for budget in [0, 1, 5, 10, 15, 25]:
            expected = max(sum(v * flag for v, flag in zip(values, flags))
                           for flags in itertools.product([0, 1], repeat=len(costs))
                           if sum(c * flag for c, flag in zip(costs, flags)) <= budget)
            chosen = optimize_portfolio(data, budget * 1_000_000)['selected']
            self.assertEqual(chosen.net_financial_value.sum(), expected * 1_000_000)
            self.assertLessEqual(chosen.licensing_cost.sum(), budget * 1_000_000)

    def test_baseline_skips_unaffordable_title(self):
        data = pd.DataFrame({'licensing_cost': [40, 28, 5, 2],
                             'viewing_hours': [100, 90, 80, 70]})
        self.assertEqual(select_by_viewing_hours(data, 30).index.tolist(), [1, 3])


if __name__ == '__main__':
    unittest.main()
