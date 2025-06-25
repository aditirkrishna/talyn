"""
Probability measure module for finite sample spaces.
"""
from typing import Any, Dict, Set
from talyn.sample_space import SampleSpace
import itertools

class ProbabilityMeasure:
    """
    Probability measure over a finite sample space Omega.
    """
    def __init__(self, space: SampleSpace, prob_map: Dict[Any, float]):
        # Validate domain
        if not set(prob_map.keys()) <= space.omega:
            invalid = set(prob_map.keys()) - space.omega
            raise ValueError(f"Probabilities provided for outcomes not in sample space: {invalid}")
        total = sum(prob_map.values())
        if total <= 0:
            raise ValueError("Sum of probabilities must be positive")
        # Normalize
        self.probabilities: Dict[Any, float] = {
            outcome: p / total for outcome, p in prob_map.items()
        }
        self.space = space

    def prob(self, event: Set[Any]) -> float:
        """
        Compute probability of event (subset of Omega).
        """
        if not event <= self.space.omega:
            raise ValueError("Event contains outcomes outside the sample space")
        return sum(self.probabilities.get(outcome, 0.0) for outcome in event)
