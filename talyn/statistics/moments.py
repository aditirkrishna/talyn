"""
Talyn statistics: moment calculations.
"""
from typing import List
import math

def mean(samples: List[float]) -> float:
    """Compute the sample mean."""
    return sum(samples) / len(samples) if samples else 0.0

def variance(samples: List[float]) -> float:
    """Compute the sample variance."""
    m = mean(samples)
    return sum((x - m) ** 2 for x in samples) / len(samples) if samples else 0.0

def skewness(samples: List[float]) -> float:
    """Compute the sample skewness."""
    m = mean(samples)
    var = variance(samples)
    s = math.sqrt(var)
    if s == 0:
        return 0.0
    return sum(((x - m) / s) ** 3 for x in samples) / len(samples)

def kurtosis(samples: List[float]) -> float:
    """Compute the sample excess kurtosis (kurtosis - 3)."""
    m = mean(samples)
    var = variance(samples)
    s = math.sqrt(var)
    if s == 0:
        return -3.0
    return sum(((x - m) / s) ** 4 for x in samples) / len(samples) - 3.0
