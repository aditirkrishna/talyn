"""
Talyn bayesian: Maximum Likelihood Estimation implementation.
"""
import math
from typing import List, Callable, Tuple

def mle(
    data: List[float], 
    likelihood: Callable[[List[float], float], float],
    param_range: Tuple[float, float],
    n_points: int = 100
) -> float:
    """
    Find MLE estimate by grid search.
    Args:
        data: Observed data points
        likelihood: Function computing likelihood(data, parameter)
        param_range: (min, max) range to search over
        n_points: Number of grid points to evaluate
    Returns:
        Maximum likelihood estimate
    """
    min_param, max_param = param_range
    best_param = min_param
    best_likelihood = -math.inf
    
    for i in range(n_points):
        param = min_param + i * (max_param - min_param) / (n_points - 1)
        current_likelihood = likelihood(data, param)
        
        if current_likelihood > best_likelihood:
            best_likelihood = current_likelihood
            best_param = param
    
    return best_param
