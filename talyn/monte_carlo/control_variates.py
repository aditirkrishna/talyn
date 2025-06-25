"""
Talyn Monte Carlo: control variates variance reduction.
"""
import random
from typing import Callable, Tuple

def control_variates(
    f: Callable[[float], float], 
    g: Callable[[float], float],
    g_expectation: float,
    n_samples: int = 1000
) -> Tuple[float, float]:
    """
    Estimate E[f(X)] using control variate g with known E[g].
    Args:
        f: Target function
        g: Control variate function with known expectation
        g_expectation: Known E[g(X)]
        n_samples: Number of samples
    Returns:
        (estimate, variance_reduction_factor)
    """
    # First pass: estimate covariance
    cov_sum = 0.0
    var_g_sum = 0.0
    f_samples = []
    g_samples = []
    
    for _ in range(n_samples):
        x = random.random()
        fx = f(x)
        gx = g(x)
        f_samples.append(fx)
        g_samples.append(gx)
        cov_sum += (fx - sum(f_samples)/len(f_samples)) * (gx - sum(g_samples)/len(g_samples))
        var_g_sum += (gx - g_expectation)**2
    
    # Calculate optimal coefficient
    b = cov_sum / var_g_sum if var_g_sum > 0 else 0
    
    # Second pass: apply control variate
    controlled_sum = 0.0
    for fx, gx in zip(f_samples, g_samples):
        controlled_sum += fx - b * (gx - g_expectation)
    
    estimate = controlled_sum / n_samples
    variance_reduction = 1 - (cov_sum**2) / (sum((fx - sum(f_samples)/n_samples)**2 for fx in f_samples) * var_g_sum) if var_g_sum > 0 else 0
    
    return estimate, variance_reduction
