"""
Talyn sample space and event operations.
"""

from typing import Any, Set, Iterable

class SampleSpace:
    """
    Represents a finite sample space Ω.
    """
    def __init__(self, outcomes: Iterable[Any]):
        self.omega = set(outcomes)

    def validate_element(self, element: Any) -> None:
        """
        Ensure element is in the sample space.
        """
        if element not in self.omega:
            raise ValueError(f"Element {element!r} not in sample space")


def union(A: Set[Any], B: Set[Any]) -> Set[Any]:
    """
    Return the union of events A and B.
    """
    return A | B


def intersection(A: Set[Any], B: Set[Any]) -> Set[Any]:
    """
    Return the intersection of events A and B.
    """
    return A & B


def complement(A: Set[Any], space: SampleSpace) -> Set[Any]:
    """
    Return the complement of event A in the sample space.
    """
    if not A <= space.omega:
        raise ValueError("Event A contains elements outside the sample space")
    return space.omega - A
