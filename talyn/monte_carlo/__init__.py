"""
Talyn Monte Carlo package: integration and sampling methods.
"""
from .integrate import integrate
from .estimate_pi import estimate_pi
from .rejection_sampling import rejection_sampling
from .importance_sampling import importance_sampling
from .antithetic import antithetic_variates
from .stratified import stratified_sampling
from .control_variates import control_variates

__all__ = [
    "integrate", "estimate_pi", "rejection_sampling", "importance_sampling",
    "antithetic_variates", "stratified_sampling", "control_variates"
]
