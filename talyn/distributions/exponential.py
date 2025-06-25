"""
Exponential distribution for Talyn.
"""
import random
import math

class Exponential:
    """
    Exponential(lam): waiting time between Poisson events, lam > 0.
    """
    def __init__(self, lam: float):
        self.lam = lam

    def pdf(self, x: float) -> float:
        if x < 0:
            return 0.0
        return self.lam * math.exp(-self.lam * x)

    def sample(self) -> float:
        u = random.random()
        return -math.log(1-u) / self.lam

