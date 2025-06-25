"""
Talyn simulation: Autocorrelation function computation.
"""
from typing import List

def autocorrelation(data: List[float], lag_max: int = None) -> List[float]:
    """
    Compute autocorrelation for lags up to lag_max (default n-1).
    """
    n = len(data)
    if n == 0:
        return []
    if lag_max is None or lag_max >= n:
        lag_max = n - 1
    mean = sum(data) / n
    # variance
    var = sum((x - mean)**2 for x in data) / n
    result: List[float] = []
    for lag in range(lag_max + 1):
        cov = sum((data[i] - mean) * (data[i + lag] - mean) for i in range(n - lag)) / (n - lag)
        result.append(cov / var if var > 0 else 0.0)
    return result
