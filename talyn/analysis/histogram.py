"""
Histogram utilities for empirical distributions.
"""
from typing import List

def histogram(samples: List[float], bins: int = 10) -> List[int]:
    """
    Build a histogram count list for samples over [0,1).
    """
    counts = [0] * bins
    for v in samples:
        idx = int(v * bins)
        if idx < 0:
            idx = 0
        elif idx >= bins:
            idx = bins - 1
        counts[idx] += 1
    return counts


def ascii_histogram(counts: List[int], width: int = 50) -> None:
    """
    Print an ASCII histogram for given counts.
    """
    max_count = max(counts) if counts else 0
    for i, c in enumerate(counts):
        bar = '█' * int((c / max_count) * width) if max_count > 0 else ''
        print(f"Bin {i:2d}: {bar} ({c})")
