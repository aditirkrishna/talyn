"""
Talyn simulation: Random walk implementation.
"""
import random
from typing import List

def random_walk(steps: int = 1000, step_size: float = 1.0) -> List[float]:
    """
    Simulate a 1D symmetric random walk.
    Args:
        steps: Number of steps
        step_size: Size of each step
    Returns:
        List of positions at each time step
    """
    path = [0.0]
    for _ in range(steps):
        path.append(path[-1] + random.choice([-step_size, step_size]))
    return path

def biased_random_walk(steps: int = 1000, step_size: float = 1.0, p: float = 0.5) -> List[float]:
    """
    Simulate a 1D biased random walk.
    Args:
        steps: Number of steps
        step_size: Size of each step
        p: Probability of stepping right (must be between 0 and 1)
    Returns:
        List of positions at each time step
    """
    if not 0 <= p <= 1:
        raise ValueError("Probability p must be between 0 and 1")
        
    path = [0.0]
    for _ in range(steps):
        step = step_size if random.random() < p else -step_size
        path.append(path[-1] + step)
    return path
