"""
Empirical Cumulative Distribution Function (ECDF) utilities.
"""
from typing import List, Any, Tuple

def ecdf(samples: List[float]) -> Tuple[List[float], List[float]]:
    """
    Compute empirical CDF points for a list of samples.
    Returns two lists: sorted samples (x) and corresponding CDF values (y).
    """
    if not samples:
        return [], []
    sorted_samples = sorted(samples)
    n = len(samples)
    x = []
    y = []
    for i, v in enumerate(sorted_samples, start=1):
        x.append(v)
        y.append(i / n)
    return x, y
