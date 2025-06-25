"""
Talyn statistics: law of large numbers demonstration.
"""
from typing import List

def law_of_large_numbers(samples: List[float]) -> List[float]:
    """
    Return running averages of the provided samples for LLN demonstration.
    """
    means = []
    total = 0.0
    for i, x in enumerate(samples, start=1):
        total += x
        means.append(total / i)
    return means
