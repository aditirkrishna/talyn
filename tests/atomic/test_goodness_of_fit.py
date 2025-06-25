"""
Goodness-of-fit tests for Talyn distributions (chi-square, KS).
"""
import unittest
import math
from talyn.distributions.discrete_uniform import DiscreteUniform
from talyn.distributions.normal import Normal
from scipy.stats import chisquare, kstest

class TestGoodnessOfFit(unittest.TestCase):
    def test_discrete_uniform_chi2(self):
        d = DiscreteUniform(a=1, b=6)
        samples = [d.sample() for _ in range(6000)]
        counts = [samples.count(i) for i in range(1, 7)]
        expected = [1000] * 6
        chi2, p = chisquare(counts, expected)
        self.assertGreater(p, 0.01)

    def test_normal_ks(self):
        n = Normal(mu=0, sigma=1)
        samples = [n.sample() for _ in range(3000)]
        d, p = kstest(samples, 'norm')
        self.assertGreater(p, 0.01)

if __name__ == "__main__":
    unittest.main()
