"""
Talyn information: Entropy and information measures.
"""
import math
from typing import List

def entropy(probabilities: List[float], base: float = 2) -> float:
    """
    Calculate Shannon entropy of a probability distribution.
    Args:
        probabilities: List of probabilities (must sum to 1)
        base: Logarithm base (default 2 for bits)
    Returns:
        Entropy in specified units
    """
    if not math.isclose(sum(probabilities), 1.0, rel_tol=1e-9):
        raise ValueError("Probabilities must sum to 1")
    return -sum(p * math.log(p, base) for p in probabilities if p > 0)

def kl_divergence(p: List[float], q: List[float], base: float = 2) -> float:
    """
    Calculate Kullback-Leibler divergence between distributions p and q.
    Args:
        p: True probability distribution
        q: Approximating distribution
        base: Logarithm base
    Returns:
        D_KL(p||q)
    """
    if len(p) != len(q):
        raise ValueError("Distributions must have same length")
    if not math.isclose(sum(p), 1.0, rel_tol=1e-9) or not math.isclose(sum(q), 1.0, rel_tol=1e-9):
        raise ValueError("Both distributions must sum to 1")
    return sum(p_i * math.log(p_i/q_i, base) for p_i, q_i in zip(p, q) if p_i > 0)
