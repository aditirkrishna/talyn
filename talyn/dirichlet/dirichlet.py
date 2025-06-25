"""
Talyn dirichlet: Dirichlet distribution sampling and PDF.
"""
import random
import math
from math import gamma
from typing import List, Tuple

def sample_dirichlet(alpha: List[float]) -> List[float]:
    """
    Sample from a Dirichlet distribution with parameters alpha.
    """
    thetas = [random.gammavariate(a, 1.0) for a in alpha]
    total = sum(thetas)
    return [t / total for t in thetas]

def dirichlet_pdf(x: List[float], alpha: List[float]) -> float:
    """
    Compute Dirichlet PDF at point x given parameters alpha.
    """
    if len(x) != len(alpha):
        raise ValueError("Dimension mismatch")
    coef = gamma(sum(alpha)) / math.prod([gamma(a) for a in alpha])
    return coef * math.prod([x_i**(a_i - 1) for x_i, a_i in zip(x, alpha)])

