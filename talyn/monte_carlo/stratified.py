"""
Talyn Monte Carlo: stratified sampling variance reduction.
"""
import random
from typing import Callable

def stratified_sampling(
    f: Callable[[float], float], 
    strata: int = 10,
    samples_per_stratum: int = 100
) -> float:
    """
    Estimate E[f(X)] using stratified sampling.
    Args:
        f: Function to estimate expectation of
        strata: Number of strata (0,1] is divided into
        samples_per_stratum: Samples per stratum
    Returns:
        Estimated expectation
    """
    total = 0.0
    for i in range(strata):
        a = i / strata
        b = (i + 1) / strata
        for _ in range(samples_per_stratum):
            x = random.uniform(a, b)
            total += f(x)
    return total / (strata * samples_per_stratum)
