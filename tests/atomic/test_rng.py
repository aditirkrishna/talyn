"""
Atomic tests for RNGs (LCG, XORShift) and uniformity.
"""
import unittest
from talyn.rng.lcg import LCG
from talyn.rng.xorshift import XORShift32

class TestRNGs(unittest.TestCase):
    def test_lcg_uniformity(self):
        lcg = LCG(seed=123)
        samples = [lcg.random() for _ in range(10000)]
        self.assertAlmostEqual(sum(samples)/len(samples), 0.5, delta=0.02)
        self.assertTrue(all(0 <= x < 1 for x in samples))
    
    def test_xorshift_uniformity(self):
        rng = XORShift32(seed=456)
        samples = [rng.random() for _ in range(10000)]
        self.assertAlmostEqual(sum(samples)/len(samples), 0.5, delta=0.02)
        self.assertTrue(all(0 <= x < 1 for x in samples))

if __name__ == "__main__":
    unittest.main()
