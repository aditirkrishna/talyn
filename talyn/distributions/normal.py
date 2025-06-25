"""
Normal distribution for Talyn.
"""
import random
import math

class Normal:
    """
    Normal(mu, sigma): Gaussian distribution with mean mu and std sigma.
    """
    def __init__(self, mu: float, sigma: float):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x: float) -> float:
        z = (x - self.mu) / self.sigma
        return math.exp(-0.5 * z * z) / (self.sigma * math.sqrt(2 * math.pi))

    def sample(self) -> float:
        # Box-Muller transform
        u1 = random.random()
        u2 = random.random()
        z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2 * math.pi * u2)
        return self.mu + self.sigma * z0

