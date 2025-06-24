"""
Talyn RNG module.

Provides pseudorandom number generators for simulations.
"""

class LCG:
    """
    Linear Congruential Generator (LCG) producing floats in [0,1).

    Formula: X_{n+1} = (a * X_n + c) mod m
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


class XORShift32:
    """
    XORShift RNG producing floats in [0,1).

    Algorithm: x ^= x << 13; x ^= x >> 17; x ^= x << 5
    """
    def __init__(self, seed: int):
        self.state = seed & 0xFFFFFFFF

    def random(self) -> float:
        """
        Generate next pseudorandom number as float in [0,1).
        """
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17)
        x ^= (x << 5) & 0xFFFFFFFF
        self.state = x & 0xFFFFFFFF
        return self.state / 2**32
