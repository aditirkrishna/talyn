"""
EventSpace and powerset utilities for Talyn probabilistic kernel.
Pure Python, no dependencies.
"""
from typing import List, Set, Dict, Optional
import itertools

class EventSpace:
    def __init__(self, omega: List[str], prob: Optional[Dict[str, float]] = None):
        self.space = type('Space', (), {})()
        self.space.omega = set(omega)
        self.prob_map = prob if prob is not None else {k: 1.0/len(omega) for k in omega}
        if abs(sum(self.prob_map.values()) - 1.0) > 1e-8:
            raise ValueError("Probabilities must sum to 1.")

    def prob(self, event: Set[str]) -> float:
        return sum(self.prob_map[k] for k in event if k in self.prob_map)

    def union(self, A: Set[str], B: Set[str]) -> Set[str]:
        return set(A) | set(B)

    def intersection(self, A: Set[str], B: Set[str]) -> Set[str]:
        return set(A) & set(B)

    def complement(self, A: Set[str]) -> Set[str]:
        return self.space.omega - set(A)

def powerset(s: Set[str]) -> List[Set[str]]:
    """Return the list of all subsets of set s."""
    l = list(s)
    return [set(combo) for r in range(len(l)+1) for combo in itertools.combinations(l, r)]
