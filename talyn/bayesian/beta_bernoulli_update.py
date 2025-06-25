"""
Talyn bayesian: Beta-Bernoulli conjugate prior update.
"""
import math
from typing import Tuple, List

def beta_bernoulli_update(
    prior: Tuple[float, float], 
    data: List[int]
) -> Tuple[float, float]:
    """
    Update Beta prior with Bernoulli/Binomial observations.
    Args:
        prior: (alpha, beta) parameters of Beta prior
        data: List of binary observations (0 or 1)
    Returns:
        (alpha_post, beta_post) parameters of Beta posterior
    """
    alpha_prior, beta_prior = prior
    successes = sum(data)
    failures = len(data) - successes
    
    return (alpha_prior + successes, beta_prior + failures)
