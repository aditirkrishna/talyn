"""
Talyn decision: Finite Markov Decision Process representation.
"""
from typing import Dict, Tuple, List, Any
import random

State = Any
Action = Any

class MDP:
    """Finite MDP with discrete state and action spaces."""

    def __init__(
        self,
        transitions: Dict[Tuple[State, Action], List[Tuple[State, float]]],
        rewards: Dict[Tuple[State, Action, State], float],
        gamma: float = 0.99,
    ):
        """
        Args:
            transitions: mapping (s,a) -> list of (s', P(s'|s,a))
            rewards: mapping (s,a,s') -> r
            gamma: discount factor, 0<gamma<=1
        """
        if not 0 < gamma <= 1:
            raise ValueError("gamma must be in (0,1]")
        self.P = transitions
        self.R = rewards
        self.gamma = gamma
        self.states = sorted({s for s, _ in transitions.keys()} | {s for lst in transitions.values() for s, _ in lst})
        self.actions = {s: sorted({a for (s0,a) in transitions if s0==s}) for s in self.states}

    def next_state_reward(self, state: State, action: Action) -> Tuple[State, float]:
        """Sample next state and reward given current state and action."""
        probs = self.P[(state, action)]
        r = random.random()
        cumulative = 0.0
        for s_prime, p in probs:
            cumulative += p
            if r <= cumulative:
                reward = self.R.get((state, action, s_prime), 0.0)
                return s_prime, reward
        # fallback last
        s_prime, _ = probs[-1]
        reward = self.R.get((state, action, s_prime), 0.0)
        return s_prime, reward
