"""
Talyn information: Jensen-Shannon divergence implementation.
"""
import math
from typing import List
from .entropy import entropy

def jensen_shannon(p: List[float], q: List[float], base: float = 2) -> float:
    """
    Calculate Jensen-Shannon divergence between distributions p and q.
    Args:
        p: First probability distribution
        q: Second probability distribution
        base: Logarithm base
    Returns:
        JSD(p||q) - symmetric measure of distribution similarity
    """
    if len(p) != len(q):
        raise ValueError("Distributions must have same length")
    if not math.isclose(sum(p), 1.0, rel_tol=1e-9) or not math.isclose(sum(q), 1.0, rel_tol=1e-9):
        raise ValueError("Both distributions must sum to 1")
    
    m = [0.5 * (p_i + q_i) for p_i, q_i in zip(p, q)]
    return 0.5 * entropy(p, base) + 0.5 * entropy(q, base) - entropy(m, base)
