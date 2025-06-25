"""
Sampling utilities for Talyn.
"""
import random
from typing import List, Any, Optional, Callable


def sample_without_replacement(population: List[Any], k: int, rng_func: Optional[Callable[[], float]] = None) -> List[Any]:
    """
    Draw k unique elements without replacement using Fisher-Yates shuffle.
    """
    A = list(population)
    n = len(A)
    if k > n:
        raise ValueError("k cannot exceed population size")
    rng = rng_func or random.random
    for i in range(k):
        j = i + int(rng() * (n - i))
        A[i], A[j] = A[j], A[i]
    return A[:k]
