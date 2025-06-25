"""
Talyn simulation: Brownian motion implementation.
"""
import random
import math
from typing import List

def brownian_motion(steps: int = 1000, delta: float = 0.1) -> List[float]:
    """
    Simulate 1D Brownian motion (Wiener process).
    Args:
        steps: Number of time steps
        delta: Time increment between steps
    Returns:
        List of positions at each time step
    """
    path = [0.0]
    for _ in range(1, steps):
        path.append(path[-1] + math.sqrt(delta) * random.gauss(0, 1))
    return path
