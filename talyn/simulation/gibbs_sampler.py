"""
Talyn simulation: Gibbs sampling implementation.
"""
from typing import Callable, Dict, List, Tuple
import random

class GibbsSampler:
    """
    Gibbs sampler for multivariate distributions.
    """
    def __init__(self, initial_state: Dict[str, float], full_conditionals: Dict[str, Callable[[Dict[str, float]], float]]):
        """
        Args:
            initial_state: Dictionary of initial parameter values
            full_conditionals: Dictionary of full conditional sampling functions for each parameter
        """
        self.state = initial_state.copy()
        self.conditionals = full_conditionals
        self.history = [initial_state.copy()]
    
    def step(self) -> Dict[str, float]:
        """Perform one Gibbs sampling iteration."""
        for param, sampler in self.conditionals.items():
            self.state[param] = sampler(self.state)
        self.history.append(self.state.copy())
        return self.state
    
    def sample(self, n: int) -> List[Dict[str, float]]:
        """Run chain for n steps and return samples."""
        for _ in range(n):
            self.step()
        return self.history[-n:]
