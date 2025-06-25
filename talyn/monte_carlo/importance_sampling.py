"""
Talyn Monte Carlo: importance sampling implementation.
"""
import random
from typing import Callable, List

def importance_sampling(
    target_pdf: Callable[[float], float],
    proposal_pdf: Callable[[float], float],
    proposal_sampler: Callable[[], float],
    f: Callable[[float], float],
    n_samples: int = 1000
) -> float:
    """
    Estimate E[f(X)] where X ~ target_pdf using importance sampling.
    Args:
        target_pdf: Target probability density function
        proposal_pdf: Proposal probability density function
        proposal_sampler: Function to sample from proposal distribution
        f: Function whose expectation we want to estimate
        n_samples: Number of samples
    Returns:
        Estimated expectation
    """
    total = 0.0
    for _ in range(n_samples):
        x = proposal_sampler()
        weight = target_pdf(x) / proposal_pdf(x)
        total += f(x) * weight
    return total / n_samples
