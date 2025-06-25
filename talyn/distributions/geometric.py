"""
Geometric distribution for Talyn.
"""
import random
import math

class Geometric:
    """
    Geometric(p): number of failures before first success (support: 0,1,2,...)
    """
    def __init__(self, p: float):
        self.p = p

    def pmf(self, k: int) -> float:
        if k < 0:
            return 0.0
        return (1 - self.p) ** k * self.p

    def sample(self) -> int:
        """Draw a sample from Geometric(p)."""
        u = random.random()
        return int(math.log(1 - u) / math.log(1 - self.p))

