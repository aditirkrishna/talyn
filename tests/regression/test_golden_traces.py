"""
Regression tests with golden traces for Talyn.
"""
import unittest
import json
from talyn.hmm.forward import forward_algorithm
from talyn.inference.kalman import kalman_filter

class TestGoldenTraces(unittest.TestCase):
    def test_hmm_golden(self):
        obs = [0, 1, 0]
        golden = json.load(open('tests/regression/golden_hmm.json'))
        result = forward_algorithm(obs)
        self.assertEqual(result, golden)

    def test_kalman_golden(self):
        obs = [1.0, 0.5, 1.2]
        golden = json.load(open('tests/regression/golden_kalman.json'))
        result = kalman_filter(obs)
        self.assertEqual(result, golden)

if __name__ == "__main__":
    unittest.main()
