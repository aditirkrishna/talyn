"""
Sampling utilities for Talyn: mathematically pure, dependency-free.
"""
from typing import List, Any, Optional
import random

# No magic numbers: all constants defined at top if needed


def sample_without_replacement(population: List[Any], k: int) -> List[Any]:
    """
    Sample k unique elements from population without replacement.
    Args:
        population: List[Any], population to sample from
        k: int, number of unique samples (0 < k <= len(population))
    Returns:
        List[Any]: k unique elements
    Raises:
        ValueError: if k > len(population)
    """
    if k > len(population):
        raise ValueError("Sample size exceeds population size")
    return random.sample(population, k)


def weighted_sample(
    population: List[Any],
    weights: List[float],
    k: int = 1,
    seed: Optional[int] = None
) -> Any:
    """
    Weighted random sampling with replacement.
    Args:
        population: List[Any], population to sample from
        weights: List[float], non-negative weights (not necessarily normalized)
        k: int, number of samples (default 1)
        seed: Optional[int], RNG seed for reproducibility
    Returns:
        Any or List[Any]: single sample if k==1, else list of samples
    Raises:
        ValueError: if population and weights lengths mismatch or weights sum to zero
    """
    if len(population) != len(weights):
        raise ValueError("Population and weights must be same length")
    total = sum(weights)
    if total == 0:
        raise ValueError("Sum of weights must be positive")
    norm_weights = [w / total for w in weights]
    rng = random.Random(seed)
    # Mathematical note: uses Python's built-in weighted sampling (replacement)
    if k == 1:
        return rng.choices(population, weights=norm_weights, k=1)[0]
    return rng.choices(population, weights=norm_weights, k=k)
