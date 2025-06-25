"""
Kolmogorov axioms validators for ProbabilityMeasure.
"""
from typing import Any, Set
from talyn.probability.measure import ProbabilityMeasure
import itertools


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


def validate_monotonicity(measure: ProbabilityMeasure, tol: float = 1e-8) -> None:
    """
    Check monotonicity: if A ⊆ B, then P(A) ≤ P(B).
    """
    omega = measure.space.omega
    elements = list(omega)
    subsets = [set(c) for r in range(len(elements)+1) for c in itertools.combinations(elements, r)]
    for A in subsets:
        for B in subsets:
            if A <= B:
                if measure.prob(A) > measure.prob(B) + tol:
                    raise ValueError(f"Monotonicity failed: P({A}) > P({B})")


def validate_additivity(measure: ProbabilityMeasure, A: Set[Any], B: Set[Any], tol: float = 1e-8) -> None:
    """
    Check that for disjoint A and B: P(A ∪ B) = P(A) + P(B).
    """
    if A & B:
        raise ValueError("Events A and B are not disjoint")
    p_union = measure.prob(A | B)
    p_sum = measure.prob(A) + measure.prob(B)
    if abs(p_union - p_sum) > tol:
        raise ValueError(f"Additivity failed: P(A ∪ B)={p_union} != P(A)+P(B)={p_sum}")
