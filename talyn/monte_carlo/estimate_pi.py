"""
Monte Carlo π estimation for Talyn: pure Python, no dependencies.
"""
import random
import time

# No magic numbers: all constants defined at top if needed


def estimate_pi(n: int = 1000000) -> (float, float):
    """
    Estimate π using Monte Carlo sampling of the unit circle.
    Args:
        n: int, number of samples
    Returns:
        (float, float): (pi_estimate, elapsed_time_seconds)
    Scientific contract:
        Returns unbiased estimate of π as n→∞ using rejection sampling in [0,1]^2.
    """
    inside = 0
    t0 = time.perf_counter()  # high-precision timing
    for _ in range(n):
        x, y = random.random(), random.random()
        # Accept if inside unit circle (x^2 + y^2 ≤ 1)
        if x*x + y*y <= 1.0:
            inside += 1
    t1 = time.perf_counter()
    return 4 * inside / n, t1 - t0
