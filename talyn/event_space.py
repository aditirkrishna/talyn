"""
Talyn event space: sigma-algebra, EventSpace class with foundational methods.
"""
from typing import Any, Dict, Set, Iterable, List, Optional
import itertools
import random
from .sample_space import SampleSpace
from .probability import ProbabilityMeasure


def powerset(s: Set[Any]) -> List[Set[Any]]:
    """
    Return the powerset of set s as a list of subsets.
    """
    lst = list(s)
    return [set(comb) for r in range(len(lst) + 1) for comb in itertools.combinations(lst, r)]


class EventSpace:
    """
    EventSpace encapsulates a sample space, its sigma-algebra, and a probability measure.
    """
    def __init__(
        self,
        outcomes: Iterable[Any],
        prob_map: Optional[Dict[Any, float]] = None,
        rng_func=None
    ):
        # Sample space and sigma-algebra (powerset)
        self.space = SampleSpace(outcomes)
        self.sigma = powerset(self.space.omega)
        # Default uniform probabilities if none provided
        if prob_map is None:
            prob_map = {o: 1.0 for o in self.space.omega}
        self.measure = ProbabilityMeasure(self.space, prob_map)
        self.rng = rng_func if rng_func is not None else random.random

    def validate_sigma_algebra(self) -> None:
        """
        Ensure closure under complement and union.
        """
        for A in self.sigma:
            comp = self.space.omega - A
            if comp not in self.sigma:
                raise ValueError(f"Sigma-algebra not closed under complement for {A}")
            for B in self.sigma:
                if A.union(B) not in self.sigma:
                    raise ValueError(f"Sigma-algebra not closed under union for {A}, {B}")

    def prob(self, event: Set[Any]) -> float:
        return self.measure.prob(event)

    def complement(self, A: Set[Any]) -> Set[Any]:
        return self.space.omega - A

    def union(self, A: Set[Any], B: Set[Any]) -> Set[Any]:
        return A.union(B)

    def intersection(self, A: Set[Any], B: Set[Any]) -> Set[Any]:
        return A.intersection(B)

    def draw(self) -> Any:
        """
        Sample a random outcome according to the probability measure.
        """
        u = self.rng()
        cumulative = 0.0
        for outcome, p in self.measure.probabilities.items():
            cumulative += p
            if u < cumulative:
                return outcome
        # fallback
        return outcome

    def conditional_probability(self, A: Set[Any], B: Set[Any]) -> float:
        """
        Compute P(A|B) = P(A ∩ B) / P(B).
        """
        pB = self.measure.prob(B)
        if pB == 0:
            raise ValueError("P(B) is zero; conditional probability undefined")
        pAB = self.measure.prob(A.intersection(B))
        return pAB / pB

    def total_probability(self, A: Set[Any], partition: Iterable[Set[Any]]) -> float:
        """
        Compute total probability rule: sum P(A|Bi)*P(Bi) over partition.
        """
        total = 0.0
        for Bi in partition:
            pBi = self.measure.prob(Bi)
            if pBi == 0:
                continue
            pA_Bi = self.measure.prob(A.intersection(Bi)) / pBi
            total += pA_Bi * pBi
        return total

    def bayes(self, A: Set[Any], B: Set[Any]) -> float:
        """
        Compute Bayes: P(B|A) = P(A|B)*P(B)/P(A).
        """
        pA = self.measure.prob(A)
        if pA == 0:
            raise ValueError("P(A) is zero; Bayes undefined")
        pB = self.measure.prob(B)
        if pB == 0:
            return 0.0
        pA_B = self.measure.prob(A.intersection(B)) / pB
        return pA_B * pB / pA
