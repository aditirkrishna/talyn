"""
Compositional sampler tests for Talyn.
"""
import unittest
from talyn.composition.composed_sampler import ComposedSampler

class TestCompositionalSamplers(unittest.TestCase):
    def test_simple_composition(self):
        # f(x) = x + epsilon
        sampler = ComposedSampler()
        samples = [sampler.sample() for _ in range(1000)]
        mean = sum(samples) / len(samples)
        self.assertTrue(abs(mean) < 2)  # Loose sanity check

    def test_nested_composition(self):
        sampler = ComposedSampler(nested=True)
        samples = [sampler.sample() for _ in range(1000)]
        self.assertEqual(len(samples), 1000)

    def test_independence(self):
        sampler = ComposedSampler()
        s1 = [sampler.sample() for _ in range(1000)]
        s2 = [sampler.sample() for _ in range(1000)]
        # Correlation should be low
        corr = sum((a-b)**2 for a, b in zip(s1, s2)) / 1000
        self.assertGreater(corr, 0.1)

if __name__ == "__main__":
    unittest.main()
