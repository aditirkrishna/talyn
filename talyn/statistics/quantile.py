"""
Talyn statistics: quantile function (inverse CDF).
"""
from typing import List


def quantile(samples: List[float], p: float) -> float:
    """
    Compute the p-th quantile of samples (0 <= p <= 1).
    Uses nearest-rank method.
    """
    if not samples:
        raise ValueError("No samples provided")
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be between 0 and 1")
    sorted_samples = sorted(samples)
    n = len(sorted_samples)
    # nearest-rank
    rank = int(p * (n - 1))
    return sorted_samples[rank]
