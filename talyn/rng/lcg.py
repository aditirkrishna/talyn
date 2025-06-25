"""
LCG pseudorandom number generator.
"""

class LCG:
    """
    Linear Congruential Generator (LCG) producing floats in [0,1).
    X_{n+1} = (a * X_n + c) mod m
    """
    def __init__(self, seed: int, a: int = 1664525, c: int = 1013904223, m: int = 2**32):
        self.a = a
        self.c = c
        self.m = m
        self.state = seed

    def random(self) -> float:
        """
        Generate next pseudorandom number as float in [0,1).
        """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m
