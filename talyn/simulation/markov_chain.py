"""
Talyn simulation: Markov Chain Monte Carlo implementation.
"""
from typing import Callable, List, Tuple, Any
import random
import math

class MarkovChain:
    """
    Generic Markov Chain for MCMC sampling.
    """
    def __init__(self, initial_state: Any, transition_kernel: Callable[[Any], Any]):
        self.state = initial_state
        self.transition = transition_kernel
        self.history = [initial_state]

    def step(self) -> Any:
        """Perform one MCMC transition."""
        self.state = self.transition(self.state)
        self.history.append(self.state)
        return self.state

    def sample(self, n: int) -> List[Any]:
        """Run chain for n steps and return samples."""
        for _ in range(n):
            self.step()
        return self.history[-n:]  # Return only the new samples

def metropolis_hastings(
    target_pdf: Callable[[Any], float], 
    proposal: Callable[[Any], Any],
    proposal_pdf: Callable[[Any, Any], float],
    initial_state: Any,
    n_samples: int = 1000,
    burn_in: int = 100
) -> List[Any]:
    """
    Metropolis-Hastings MCMC sampler.
    Args:
        target_pdf: Target probability density function (up to constant)
        proposal: Function proposing new state given current state
        proposal_pdf: q(x'|x) - proposal density
        initial_state: Starting point for the chain
        n_samples: Number of samples to collect
        burn_in: Number of burn-in samples to discard
    Returns:
        List of samples from target distribution
    """
    current = initial_state
    samples = []
    
    # Burn-in phase
    for _ in range(burn_in):
        candidate = proposal(current)
        acceptance_ratio = (target_pdf(candidate) * proposal_pdf(current, candidate)) / \
                          (target_pdf(current) * proposal_pdf(candidate, current))
        if random.random() < min(1, acceptance_ratio):
            current = candidate
    
    # Sampling phase
    for _ in range(n_samples):
        candidate = proposal(current)
        acceptance_ratio = (target_pdf(candidate) * proposal_pdf(current, candidate)) / \
                          (target_pdf(current) * proposal_pdf(candidate, current))
        if random.random() < min(1, acceptance_ratio):
            current = candidate
        samples.append(current)
    
    return samples
