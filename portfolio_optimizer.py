"""Shared binary portfolio optimization and classroom comparison baseline."""
from time import perf_counter
import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp


def load_catalog(path):
    catalog = pd.read_csv(path)
    for column in ('licensing_cost', 'ad_revenue', 'viewing_hours'):
        if not np.isfinite(catalog[column]).all() or (catalog[column] < 0).any():
            raise ValueError(f'{column} must contain finite, nonnegative numbers')
    if (catalog.licensing_cost == 0).any() or catalog.title_id.duplicated().any():
        raise ValueError('Titles need unique IDs and positive licensing costs')
    catalog['net_financial_value'] = catalog.ad_revenue - catalog.licensing_cost
    return catalog


def select_by_viewing_hours(catalog, budget):
    """Excel exercise: sort by audience and skip titles that do not fit."""
    remaining, indices = budget, []
    for index, row in catalog.sort_values('viewing_hours', ascending=False,
                                          kind='stable').iterrows():
        if row.licensing_cost <= remaining:
            indices.append(index)
            remaining -= row.licensing_cost
    return catalog.loc[indices].copy()


def optimize_portfolio(catalog, budget, time_limit=20):
    """Maximize projected contribution with a binary choice per title.

    A time-limited feasible result is explicitly distinguished from an optimum.
    """
    if not np.isfinite(budget) or budget < 0:
        raise ValueError('Budget must be finite and nonnegative')
    if catalog.empty:
        return dict(selected=catalog.copy(), status='proven optimal', gap=0.0, seconds=0.0)
    start = perf_counter()
    solution = milp(
        c=-catalog.net_financial_value.to_numpy(dtype=float) / 1_000_000,
        integrality=np.ones(len(catalog)), bounds=Bounds(0, 1),
        constraints=LinearConstraint(
            catalog.licensing_cost.to_numpy(dtype=float).reshape(1, -1), -np.inf, budget),
        options={'time_limit': time_limit, 'mip_rel_gap': 0.0},
    )
    elapsed = perf_counter() - start
    if solution.status not in (0, 1) or solution.x is None:
        raise RuntimeError(f'No feasible portfolio: {solution.message}')
    if not np.allclose(solution.x, np.rint(solution.x), atol=1e-6, rtol=0):
        raise RuntimeError('Optimizer returned a nonintegral portfolio')
    selected = catalog.iloc[np.flatnonzero(solution.x > 0.5)].copy()
    if selected.licensing_cost.sum() > budget:
        raise RuntimeError('Optimizer portfolio exceeds the budget')
    return dict(
        selected=selected.sort_values('net_financial_value', ascending=False),
        status='proven optimal' if solution.status == 0 else 'best feasible (time limit)',
        gap=float(solution.mip_gap), seconds=elapsed,
    )
