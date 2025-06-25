"""
Talyn RNG package.
"""

from .lcg import LCG
from .xorshift import XORShift32
from .stats import rng_histogram, print_ascii_histogram, chi_square_statistic, chi_square_degrees_of_freedom

__all__ = [
    "LCG",
    "XORShift32",
    "rng_histogram",
    "print_ascii_histogram",
    "chi_square_statistic",
    "chi_square_degrees_of_freedom",
]
