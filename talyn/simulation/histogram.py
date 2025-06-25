"""
Talyn simulation: Histogram utilities with ASCII rendering.
"""
from typing import List, Tuple

def histogram(data: List[float], bins: int = 10) -> Tuple[List[int], List[float]]:
    """
    Compute histogram counts and bin edges for data.
    """
    if not data:
        return [], []
    min_val, max_val = min(data), max(data)
    width = (max_val - min_val) / bins
    edges = [min_val + i * width for i in range(bins + 1)]
    counts = [0] * bins
    for x in data:
        idx = int((x - min_val) / width) if width > 0 else 0
        if idx < 0:
            idx = 0
        elif idx >= bins:
            idx = bins - 1
        counts[idx] += 1
    return counts, edges

def ascii_histogram(data: List[float], bins: int = 10, width: int = 50) -> str:
    """
    Render an ASCII histogram for data.
    """
    counts, edges = histogram(data, bins)
    if not counts:
        return ""
    max_count = max(counts)
    lines: List[str] = []
    for i, count in enumerate(counts):
        bar_len = int((count / max_count) * width) if max_count > 0 else 0
        bar = "#" * bar_len
        lines.append(f"{edges[i]:.2f} - {edges[i+1]:.2f} | {bar}")
    return "\n".join(lines)
