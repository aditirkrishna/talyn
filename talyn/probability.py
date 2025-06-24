"""
Probability measure and Kolmogorov axioms validators for finite sample spaces.
"""
from typing import Any, Dict, Set
from .sample_space import SampleSpace

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


def validate_nonnegativity(measure: ProbabilityMeasure) -> None:
    """
    Check that P({omega}) >= 0 for all outcomes in Omega.
    """
    for outcome, p in measure.probabilities.items():
        if p < 0:
            raise ValueError(f"Probability of {outcome!r} is negative: {p}")


def validate_unit_total(measure: ProbabilityMeasure, tol: float = 1e-8) -> None:
    """
    Check that P(Omega) = 1.
    """
    total = sum(measure.probabilities.values())
    if abs(total - 1.0) > tol:
        raise ValueError(f"Total probability is not 1 (got {total})")


def validate_additivity(
    measure: ProbabilityMeasure,
    A: Set[Any],
    B: Set[Any],
    tol: float = 1e-8
) -> None:
    """
    Check that for disjoint A and B: P(A ∪ B) = P(A) + P(B).
    """
    if A & B:
        raise ValueError("Events A and B are not disjoint")
    p_union = measure.prob(A | B)
    p_sum = measure.prob(A) + measure.prob(B)
    if abs(p_union - p_sum) > tol:
        raise ValueError(
            f"Additivity failed: P(A ∪ B)={p_union} != P(A)+P(B)={p_sum}"
        )
