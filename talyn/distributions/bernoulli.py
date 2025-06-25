"""
Bernoulli distribution module.
"""
import random

class Bernoulli:
    """
    Bernoulli(p) distribution on {0,1}.
    """
    def __init__(self, p: float, rng_func=None):
        if not 0.0 <= p <= 1.0:
            raise ValueError("p must be in [0,1]")
        self.p = p
        self.rng = rng_func or random.random

    def sample(self) -> int:
        return 1 if self.rng() < self.p else 0

    def pmf(self, k: int) -> float:
        if k == 1:
            return self.p
        if k == 0:
            return 1 - self.p
        return 0.0

    prob = pmf

    def cdf(self, k: int) -> float:
        if k < 0:
            return 0.0
        if k < 1:
            return 1 - self.p
        return 1.0
