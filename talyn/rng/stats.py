"""
RNG benchmarking utilities: histogram test and chi-square statistic.
"""
from typing import Callable, List


def rng_histogram(rng: Callable[[], float], n: int = 10000, bins: int = 10) -> List[int]:
    """
    Generate a histogram of n samples from rng, divided into `bins` equal-width bins in [0,1).
    Returns a list of counts per bin.
    """
    counts = [0] * bins
    for _ in range(n):
        v = rng()
        idx = int(v * bins)
        if idx >= bins:
            idx = bins - 1
        counts[idx] += 1
    return counts


def print_ascii_histogram(counts: List[int], width: int = 50) -> None:
    """
    Print an ASCII histogram for the given counts.
    Bars are scaled to max width.
    """
    max_count = max(counts) if counts else 0
    for i, count in enumerate(counts):
        bar_len = int((count / max_count) * width) if max_count > 0 else 0
        bar = '█' * bar_len
        print(f"Bin {i:2d}: {bar} ({count})")


def chi_square_statistic(counts: List[int]) -> float:
    """
    Compute chi-square statistic for observed `counts` against uniform expected frequency.
    Expected frequency = total_samples / number_of_bins.
    """
    total = sum(counts)
    k = len(counts)
    if k == 0:
        return 0.0
    expected = total / k
    stat = sum((obs - expected) ** 2 / expected for obs in counts)
    return stat


def chi_square_degrees_of_freedom(counts: List[int]) -> int:
    """
    Degrees of freedom for chi-square test = bins - 1.
    """
    return max(len(counts) - 1, 0)
