"""
Talyn simulation: Brownian bridge implementation.
"""
import random
import math
from typing import List

def brownian_bridge(steps: int = 1000, start: float = 0.0, end: float = 0.0) -> List[float]:
    """
    Simulate a Brownian bridge from start to end.
    Args:
        steps: Number of time steps
        start: Starting value
        end: Ending value
    Returns:
        List of positions at each time step
    """
    if steps < 2:
        return [start, end]
    
    # First generate standard Brownian motion
    W = [0.0]
    for i in range(1, steps):
        W.append(W[-1] + math.sqrt(1/steps) * random.gauss(0, 1))
    
    # Transform to Brownian bridge
    bridge = []
    for i in range(steps):
        t = i / (steps - 1)
        bridge.append(start * (1 - t) + end * t + W[i] - t * W[-1])
    
    return bridge
