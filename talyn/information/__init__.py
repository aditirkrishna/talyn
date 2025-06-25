"""
Talyn information package: entropy and divergence measures.
"""
from .entropy import entropy, kl_divergence
from .mutual_information import mutual_information
from .jensen import jensen_shannon

__all__ = ["entropy", "kl_divergence", "mutual_information", "jensen_shannon"]
