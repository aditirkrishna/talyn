"""
Talyn ABC: Approximate Bayesian Computation via rejection sampling.
"""
from typing import Callable, List, Any
import random

def abc_rejection(
    prior_sampler: Callable[[], Any],
    simulator: Callable[[Any], Any],
    observed: Any,
    distance: Callable[[Any, Any], float],
    epsilon: float,
    n_samples: int
) -> List[Any]:
    """
    Perform ABC rejection sampling.
    """
    accepted: List[Any] = []
    for _ in range(n_samples):
        theta = prior_sampler()
        sim_data = simulator(theta)
        if distance(sim_data, observed) <= epsilon:
            accepted.append(theta)
    return accepted
