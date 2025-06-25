"""
Talyn information: Mutual information calculation.
"""
import math
from typing import List, Tuple

def mutual_information(
    joint_dist: List[List[float]], 
    base: float = 2
) -> float:
    """
    Calculate mutual information I(X;Y) between two random variables.
    Args:
        joint_dist: 2D array representing joint distribution p(x,y)
        base: Logarithm base
    Returns:
        Mutual information in specified units
    """
    # Calculate marginal distributions
    p_x = [sum(row) for row in joint_dist]
    p_y = [sum(col) for col in zip(*joint_dist)]
    
    # Verify valid joint distribution
    if not math.isclose(sum(p_x), 1.0, rel_tol=1e-9):
        raise ValueError("Joint distribution must sum to 1")
    
    mi = 0.0
    for i in range(len(joint_dist)):
        for j in range(len(joint_dist[0])):
            p_xy = joint_dist[i][j]
            if p_xy > 0:
                mi += p_xy * math.log(p_xy / (p_x[i] * p_y[j]), base)
    return mi
