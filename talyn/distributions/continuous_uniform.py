"""
Continuous Uniform distribution for Talyn.
"""
import random

class ContinuousUniform:
    """
    ContinuousUniform(a, b): Uniform distribution on [a, b]
    """
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def pdf(self, x: float) -> float:
        if self.a <= x <= self.b:
            return 1.0 / (self.b - self.a)
        return 0.0

    def sample(self) -> float:
        return random.uniform(self.a, self.b)

