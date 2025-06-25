"""
Talyn utils: Data analysis helper functions.
"""
from typing import List, Dict
from collections import Counter
import math

def summary_stats(data: List[float]) -> Dict[str, float]:
    """
    Compute count, mean, and variance of a numeric dataset.
    """
    n = len(data)
    mean = sum(data) / n if n else 0.0
    var = sum((x - mean) ** 2 for x in data) / n if n else 0.0
    return {"count": n, "mean": mean, "variance": var}

def correlation(x: List[float], y: List[float]) -> float:
    """
    Compute Pearson correlation between two lists.
    """
    n = len(x)
    if n != len(y) or n < 2:
        raise ValueError("Lists must be same length and have at least 2 elements")
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (n - 1)
    std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) / (n - 1))
    std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y) / (n - 1))
    return cov / (std_x * std_y) if std_x and std_y else 0.0
