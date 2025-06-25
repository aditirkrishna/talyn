"""
Atomic tests for discrete and continuous distributions in Talyn.
"""
import unittest
from talyn.distributions.bernoulli import Bernoulli
from talyn.distributions.binomial import Binomial
from talyn.distributions.discrete_uniform import DiscreteUniform
from talyn.distributions.geometric import Geometric
from talyn.distributions.normal import Normal
from talyn.distributions.exponential import Exponential
from talyn.distributions.poisson import Poisson
import math

class TestDistributions(unittest.TestCase):
    def test_bernoulli(self):
        b = Bernoulli(p=0.7)
        samples = [b.sample() for _ in range(1000)]
        mean = sum(samples) / len(samples)
        self.assertAlmostEqual(mean, 0.7, delta=0.05)
        self.assertTrue(all(x in [0, 1] for x in samples))

    def test_binomial(self):
        b = Binomial(n=10, p=0.4)
        samples = [b.sample() for _ in range(1000)]
        mean = sum(samples) / len(samples)
        self.assertAlmostEqual(mean, 10*0.4, delta=0.5)

    def test_discrete_uniform(self):
        d = DiscreteUniform(a=1, b=6)
        samples = [d.sample() for _ in range(1200)]
        mean = sum(samples) / len(samples)
        self.assertAlmostEqual(mean, 3.5, delta=0.2)
        self.assertTrue(all(1 <= x <= 6 for x in samples))

    def test_geometric(self):
        g = Geometric(p=0.25)
        samples = [g.sample() for _ in range(2000)]
        mean = sum(samples) / len(samples)
        expected = (1 - 0.25) / 0.25
        self.assertAlmostEqual(mean, expected, delta=0.5)

    def test_normal(self):
        n = Normal(mu=2, sigma=3)
        samples = [n.sample() for _ in range(5000)]
        mean = sum(samples) / len(samples)
        var = sum((x-mean)**2 for x in samples) / len(samples)
        self.assertAlmostEqual(mean, 2, delta=0.2)
        self.assertAlmostEqual(var, 9, delta=0.5)

    def test_exponential(self):
        e = Exponential(lam=2)
        samples = [e.sample() for _ in range(3000)]
        mean = sum(samples) / len(samples)
        self.assertAlmostEqual(mean, 0.5, delta=0.05)

    def test_poisson(self):
        p = Poisson(lam=3)
        samples = [p.sample() for _ in range(3000)]
        mean = sum(samples) / len(samples)
        self.assertAlmostEqual(mean, 3, delta=0.2)

if __name__ == "__main__":
    unittest.main()
