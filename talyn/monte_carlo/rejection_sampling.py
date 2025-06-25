"""
Talyn Monte Carlo: rejection sampling implementation.
"""
import random
from typing import Callable, List

def rejection_sampling(
    target_pdf: Callable[[float], float], 
    proposal_pdf: Callable[[float], float],
    proposal_sampler: Callable[[], float],
    M: float,
    n_samples: int = 1000
) -> List[float]:
    """
    Generate samples from target distribution using rejection sampling.
    Args:
        target_pdf: Target probability density function
        proposal_pdf: Proposal probability density function
        proposal_sampler: Function to sample from proposal distribution
        M: Upper bound on target_pdf(x)/(proposal_pdf(x))
        n_samples: Number of desired samples
    Returns:
        List of accepted samples
    """
    samples = []
    while len(samples) < n_samples:
        x = proposal_sampler()
        u = random.random()
        if u * M * proposal_pdf(x) <= target_pdf(x):
            samples.append(x)
    return samples
