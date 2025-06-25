"""
Talyn inference: Bootstrap particle filter implementation.
"""
from typing import Callable, List, Tuple
import random
import math

class ParticleFilter:
    """Simple bootstrap particle filter for state-space models."""

    def __init__(
        self,
        n_particles: int,
        transition: Callable[[float], float],
        observation_likelihood: Callable[[float, float], float],
        prior_sampler: Callable[[], float],
    ):
        self.n = n_particles
        self.transition = transition
        self.observation_likelihood = observation_likelihood
        self.particles = [prior_sampler() for _ in range(n_particles)]
        self.weights = [1.0 / n_particles] * n_particles

    def _systematic_resample(self):
        positions = [(random.random() + i) / self.n for i in range(self.n)]
        cumulative = [0.0]
        for w in self.weights:
            cumulative.append(cumulative[-1] + w)
        indexes = []
        j = 0
        for p in positions:
            while p > cumulative[j+1]:
                j += 1
            indexes.append(j)
        self.particles = [self.particles[i] for i in indexes]
        self.weights = [1.0 / self.n] * self.n

    def update(self, observation: float):
        # Propagate
        self.particles = [self.transition(x) for x in self.particles]
        # Weight
        self.weights = [self.observation_likelihood(observation, x) for x in self.particles]
        total = sum(self.weights)
        if total == 0:
            self.weights = [1.0 / self.n] * self.n
        else:
            self.weights = [w / total for w in self.weights]
        # Resample
        self._systematic_resample()

    def estimate(self) -> float:
        return sum(w * x for w, x in zip(self.weights, self.particles))
