"""
Talyn bootstrap: Percentile bootstrap implementation.
"""
import random
from typing import List, Callable, TypeVar, Tuple

T = TypeVar('T')

def percentile_bootstrap(
    data: List[T], 
    statistic: Callable[[List[T]], float],
    n_resamples: int = 1000,
    confidence: float = 0.95
) -> Tuple[float, float, float]:
    """
    Calculate percentile bootstrap confidence interval.
    Args:
        data: Original sample data
        statistic: Function to compute statistic of interest
        n_resamples: Number of bootstrap samples
        confidence: Confidence level (0-1)
    Returns:
        (estimate, lower_bound, upper_bound)
    """
    if not 0 < confidence < 1:
        raise ValueError("Confidence must be between 0 and 1")
    
    n = len(data)
    estimates = []
    
    for _ in range(n_resamples):
        resample = [random.choice(data) for _ in range(n)]
        estimates.append(statistic(resample))
    
    estimates.sort()
    lower_idx = int((1 - confidence)/2 * n_resamples)
    upper_idx = int((1 + confidence)/2 * n_resamples)
    
    return statistic(data), estimates[lower_idx], estimates[upper_idx]
