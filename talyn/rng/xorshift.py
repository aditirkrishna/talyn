"""
XORShift pseudorandom number generator.
"""

class XORShift32:
    """
    XORShift RNG producing floats in [0,1). Algorithm:
      x ^= x << 13; x ^= x >> 17; x ^= x << 5
    """
    def __init__(self, seed: int):
        self.state = seed & 0xFFFFFFFF

    def random(self) -> float:
        """Generate next pseudorandom number as float in [0,1)."""
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17)
        x ^= (x << 5) & 0xFFFFFFFF
        self.state = x & 0xFFFFFFFF
        return self.state / 2**32
