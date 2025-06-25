"""
Poisson distribution for Talyn.
"""
import random
import math

class Poisson:
    """
    Poisson(lam): counts of events in fixed interval with rate lam.
    """
    def __init__(self, lam: float):
        self.lam = lam

    def pmf(self, k: int) -> float:
        if k < 0:
            return 0.0
        return math.exp(-self.lam) * (self.lam ** k) / math.factorial(k)

    def sample(self) -> int:
        # Knuth's algorithm
        L = math.exp(-self.lam)
        k = 0
        p = 1.0
        while p > L:
            k += 1
            p *= random.random()
        return k - 1

