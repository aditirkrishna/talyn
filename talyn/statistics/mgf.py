"""
Talyn statistics: moment generating function approximation.
"""
from typing import List
import math

def mgf(samples: List[float], t: float) -> float:
    """
    Compute the moment generating function M(t) = E[e^{tX}] from samples.
    """
    if not samples:
        return 0.0
    return sum(math.exp(t * x) for x in samples) / len(samples)
