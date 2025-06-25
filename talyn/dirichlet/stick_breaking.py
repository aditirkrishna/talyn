"""
Talyn dirichlet: stick-breaking representation for Dirichlet Process.
"""
import random
from typing import List

def stick_breaking(alpha: float, num_weights: int) -> List[float]:
    """
    Generate weights via stick-breaking process for DP with concentration alpha.
    Args:
        alpha: concentration parameter
        num_weights: number of weights to generate
    Returns:
        List of mixture weights summing to <=1
    """
    betas = [random.betavariate(1, alpha) for _ in range(num_weights)]
    weights: List[float] = []
    remaining = 1.0
    for beta in betas:
        w = beta * remaining
        weights.append(w)
        remaining *= (1 - beta)
    return weights
