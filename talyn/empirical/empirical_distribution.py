"""
Talyn empirical: Empirical distribution implementation.
"""
from typing import List, Optional
import bisect
import random

class EmpiricalDistribution:
    """
    Empirical distribution from samples with CDF and inverse CDF.
    """
    def __init__(self, samples: List[float]):
        """
        Initialize with observed samples.
        Args:
            samples: List of observed values
        """
        if not samples:
            raise ValueError("Must provide at least one sample")
        self.samples = sorted(samples)
        self.n = len(self.samples)
    
    def cdf(self, x: float) -> float:
        """Empirical CDF estimate at x."""
        return bisect.bisect_right(self.samples, x) / self.n
    
    def ppf(self, p: float) -> float:
        """
        Empirical percent point function (inverse CDF).
        Args:
            p: Probability in [0,1]
        Returns:
            The p-th quantile
        """
        if not 0 <= p <= 1:
            raise ValueError("p must be between 0 and 1")
        idx = min(int(p * self.n), self.n - 1)
        return self.samples[idx]
    
    def sample(self, size: Optional[int] = None) -> float:
        """Sample from the empirical distribution."""
        if size is None:
            return random.choice(self.samples)
        return [random.choice(self.samples) for _ in range(size)]
