"""
Binomial distribution for Talyn.
"""
import random
from math import comb

class Binomial:
    """
    Binomial(n, p): number of successes in n Bernoulli(p) trials.
    """
    def __init__(self, n: int, p: float):
        self.n = n
        self.p = p

    def pmf(self, k: int) -> float:
        """Probability of k successes."""
        if not (0 <= k <= self.n):
            return 0.0
        return comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def sample(self) -> int:
        """Draw a sample from Binomial(n, p)."""
        return sum(1 if random.random() < self.p else 0 for _ in range(self.n))

