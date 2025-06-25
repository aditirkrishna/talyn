"""
Talyn empirical: Empirical probability density function estimation.
"""
from typing import List, Optional
import math

class EmpiricalPDF:
    """
    Kernel density estimation for empirical PDF.
    """
    def __init__(self, samples: List[float], bandwidth: Optional[float] = None):
        """
        Initialize with observed samples and optional bandwidth.
        Args:
            samples: List of observed values
            bandwidth: Smoothing parameter (if None, uses Silverman's rule)
        """
        if not samples:
            raise ValueError("Must provide at least one sample")
        self.samples = samples
        self.n = len(samples)
        self.bandwidth = bandwidth if bandwidth is not None else self._silverman_bandwidth()
    
    def _silverman_bandwidth(self) -> float:
        """Calculate bandwidth using Silverman's rule of thumb."""
        std = math.sqrt(sum((x - sum(self.samples)/self.n)**2 for x in self.samples) / self.n)
        iqr = sorted(self.samples)[self.n*3//4] - sorted(self.samples)[self.n//4]
        return 0.9 * min(std, iqr/1.34) * self.n**(-1/5)
    
    def pdf(self, x: float) -> float:
        """
        Estimate PDF at x using Gaussian kernel density estimation.
        Args:
            x: Point to evaluate PDF at
        Returns:
            Estimated probability density
        """
        return sum(
            math.exp(-0.5 * ((x - xi)/self.bandwidth)**2) 
            for xi in self.samples
        ) / (self.n * self.bandwidth * math.sqrt(2 * math.pi))
