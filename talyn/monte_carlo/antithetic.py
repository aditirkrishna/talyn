"""
Talyn Monte Carlo: antithetic variates variance reduction.
"""
import random
from typing import Callable

def antithetic_variates(
    f: Callable[[float], float], 
    n_samples: int = 1000
) -> float:
    """
    Estimate E[f(X)] using antithetic variates.
    Args:
        f: Function to estimate expectation of
        n_samples: Number of sample pairs
    Returns:
        Estimated expectation
    """
    total = 0.0
    for _ in range(n_samples):
        u = random.random()
        total += (f(u) + f(1 - u)) / 2
    return total / n_samples
