"""
Talyn decision: epsilon-greedy multi-armed bandit implementation.
"""
from typing import List
import random

class EpsilonGreedyBandit:
    """Simple stationary K-armed bandit with ε-greedy action selection."""

    def __init__(self, true_means: List[float], epsilon: float = 0.1):
        self.true_means = true_means
        self.k = len(true_means)
        self.epsilon = epsilon
        self.counts = [0] * self.k
        self.estimates = [0.0] * self.k
        self.rewards_history: List[float] = []

    def _pull_arm(self, arm: int) -> float:
        """Return reward sampled from arm's Bernoulli/Normal with given mean (assume Normal(µ,1))."""
        return random.gauss(self.true_means[arm], 1.0)

    def select_arm(self) -> int:
        if random.random() < self.epsilon:
            return random.randrange(self.k)
        return max(range(self.k), key=lambda i: self.estimates[i])

    def step(self) -> float:
        arm = self.select_arm()
        reward = self._pull_arm(arm)
        self.counts[arm] += 1
        # incremental mean update
        n = self.counts[arm]
        self.estimates[arm] += (reward - self.estimates[arm]) / n
        self.rewards_history.append(reward)
        return reward

    def run(self, steps: int = 1000) -> List[float]:
        for _ in range(steps):
            self.step()
        return self.rewards_history
