"""
Random function contract tests for Talyn.
"""
import unittest
from talyn.utils.sampling import weighted_sample

class TestRandomContract(unittest.TestCase):
    def test_weighted_sample_distribution(self):
        weights = [0.1, 0.2, 0.7]
        samples = [weighted_sample([1,2,3], weights) for _ in range(10000)]
        props = [samples.count(i)/10000 for i in [1,2,3]]
        self.assertAlmostEqual(props[0], 0.1, delta=0.02)
        self.assertAlmostEqual(props[1], 0.2, delta=0.02)
        self.assertAlmostEqual(props[2], 0.7, delta=0.02)

    def test_seed_independence(self):
        s1 = [weighted_sample([1,2], [0.5,0.5], seed=1) for _ in range(1000)]
        s2 = [weighted_sample([1,2], [0.5,0.5], seed=2) for _ in range(1000)]
        self.assertNotEqual(s1, s2)

if __name__ == "__main__":
    unittest.main()
