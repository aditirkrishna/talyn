"""
Talyn sample space and set operations.
"""
from typing import Any, Set, Iterable

class SampleSpace:
    """
    Represents a finite sample space Ω = {ω1, ω2, ..., ωn}.
    """
    def __init__(self, outcomes: Iterable[Any]):
        self.omega = set(outcomes)

    def validate_element(self, element: Any) -> None:
        """
        Ensure element ∈ Ω.
        """
        if element not in self.omega:
            raise ValueError(f"Element {element!r} not in sample space")

def union(A: Set[Any], B: Set[Any]) -> Set[Any]:
    """
    Set-theoretic union: A ∪ B = {ω: ω∈A or ω∈B}.
    """
    return A | B

def intersection(A: Set[Any], B: Set[Any]) -> Set[Any]:
    """
    Set-theoretic intersection: A ∩ B = {ω: ω∈A and ω∈B}.
    """
    return A & B

def complement(A: Set[Any], space: SampleSpace) -> Set[Any]:
    """
    Set-theoretic complement: Aᶜ = Ω \ A.
    """
    if not A <= space.omega:
        raise ValueError("Event contains elements outside the sample space")
    return space.omega - A
