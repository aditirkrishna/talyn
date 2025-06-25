"""
Talyn simulation: MCMC convergence diagnostics (Gelman-Rubin R̂ statistic).
"""
from typing import List

def mean(xs):
    return sum(xs) / len(xs)

def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1) if len(xs) > 1 else 0.0

def gelman_rubin(chains: List[List[float]]) -> float:
    """
    Compute Gelman-Rubin R̂ statistic for multiple chains using pure Python.
    Args:
        chains: List of chains (each a list of samples)
    Returns:
        R_hat value (float)
    """
    m = len(chains)
    n = min(len(chain) for chain in chains)
    if m < 2 or n < 2:
        raise ValueError("Need at least 2 chains with 2 samples each")
    # Truncate all chains to same length
    chains = [chain[:n] for chain in chains]
    means = [mean(chain) for chain in chains]
    variances = [variance(chain) for chain in chains]
    mean_of_means = mean(means)
    B = n * variance(means)
    W = mean(variances)
    var_hat = ((n - 1) / n) * W + (1 / n) * B
    R_hat = (var_hat / W) ** 0.5 if W > 0 else float('inf')
    return float(R_hat)

