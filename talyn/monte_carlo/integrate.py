"""
Talyn Monte Carlo: numerical integration.
"""
import random
from typing import Callable

def integrate(f: Callable[[float], float], a: float, b: float, n: int = 10000) -> float:
    """
    Compute ∫ₐᵇ f(x)dx using Monte Carlo integration.
    Args:
        f: Function to integrate
        a: Lower bound
        b: Upper bound
        n: Number of samples
    """
    if b <= a:
        raise ValueError("b must be greater than a")
    
    total = 0.0
    for _ in range(n):
        x = random.uniform(a, b)
        total += f(x)
    
    return (b - a) * total / n
