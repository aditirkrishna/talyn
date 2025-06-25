"""
Talyn PPL: Tiny probabilistic programming language core.
"""
import random
from typing import Callable, Any, List

def sample(dist: Callable[..., Any], *args, **kwargs) -> Any:
    """
    Sample from a distribution function.
    """
    return dist(*args, **kwargs)

def observe(weight: float) -> float:
    """
    Weight an execution trace (placeholder).
    """
    return weight

def run_model(model: Callable[[], Any], num_samples: int) -> List[Any]:
    """
    Run the model to generate samples.
    """
    return [model() for _ in range(num_samples)]
