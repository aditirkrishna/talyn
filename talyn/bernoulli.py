"""
Bernoulli distribution module for Talyn: mathematically explicit, dependency-free.
"""
import random
from typing import Callable, Optional

class Bernoulli:
    """
    Bernoulli(p) distribution on {0,1}.
    Args:
        p: float, probability of success (0 ≤ p ≤ 1)
        rng_func: Optional[Callable[[], float]], RNG function returning float in [0,1) (default: random.random)
    Scientific contract:
        Models a single Bernoulli trial. All probabilities and outputs are mathematically explicit.
    """
    def __init__(self, p: float, rng_func: Optional[Callable[[], float]] = None):
        if not 0.0 <= p <= 1.0:
            raise ValueError("p must be in [0,1]")
        self.p = p
        self.rng = rng_func or random.random

    def sample(self) -> int:
        """
        Draw a sample from Bernoulli(p).
        Returns:
            int: 1 (success) with probability p, 0 (failure) with probability 1-p
        """
        return 1 if self.rng() < self.p else 0

    def pmf(self, k: int) -> float:
        """
        Probability mass function: P(X = k)
        Args:
            k: int, outcome (0 or 1)
        Returns:
            float: P(X = k)
        """
        if k == 1:
            return self.p
        if k == 0:
            return 1 - self.p
        return 0.0

    prob = pmf  # Alias for mathematical clarity

    def cdf(self, k: int) -> float:
        """
        Cumulative distribution function: P(X ≤ k)
        Args:
            k: int
        Returns:
            float: cumulative probability up to k
        """
        if k < 0:
            return 0.0
        if k < 1:
            return 1 - self.p
        return 1.0
