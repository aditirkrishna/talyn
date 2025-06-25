"""
Talyn dirichlet: Chinese Restaurant Process sampling.
"""
import random
from typing import List

def crp(alpha: float, n_customers: int) -> List[int]:
    """
    Chinese Restaurant Process seating for n_customers.
    Returns list of table assignments (0-indexed).
    """
    assignments: List[int] = []
    tables: List[int] = []  # counts per table
    for i in range(n_customers):
        if i == 0:
            assignments.append(0)
            tables.append(1)
        else:
            total = alpha + i
            probs = [count / total for count in tables] + [alpha / total]
            r = random.random()
            cum = 0.0
            for idx, p in enumerate(probs):
                cum += p
                if r < cum:
                    if idx < len(tables):
                        assignments.append(idx)
                        tables[idx] += 1
                    else:
                        assignments.append(idx)
                        tables.append(1)
                    break
    return assignments
