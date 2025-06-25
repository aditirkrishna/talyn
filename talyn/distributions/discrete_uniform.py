"""
DiscreteUniform distribution for Talyn.
"""
import random

class DiscreteUniform:
    """
    DiscreteUniform(a, b): Uniform integer in [a, b] inclusive.
    """
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def pmf(self, x: int) -> float:
        if self.a <= x <= self.b:
            return 1 / (self.b - self.a + 1)
        return 0.0

    def sample(self) -> int:
        return random.randint(self.a, self.b)

