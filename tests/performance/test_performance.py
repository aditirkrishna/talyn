"""
Performance and scaling benchmarks for Talyn.
"""
import unittest
import time
from talyn.monte_carlo.estimate_pi import estimate_pi
from talyn.simulation.mcmc_convergence import gelman_rubin

class TestPerformance(unittest.TestCase):
    def test_monte_carlo_scaling(self):
        t0 = time.time()
        pi, _ = estimate_pi(100000)
        t1 = time.time()
        self.assertTrue(abs(pi - 3.1415) < 0.01)
        self.assertLess(t1-t0, 2.0)

    def test_mcmc_convergence(self):
        chains = [[i + 0.01*j for i in range(100)] for j in range(4)]
        r_hat = gelman_rubin(chains)
        self.assertLess(r_hat, 1.1)

if __name__ == "__main__":
    unittest.main()
