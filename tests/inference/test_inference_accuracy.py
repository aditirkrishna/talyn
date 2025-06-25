"""
Inference accuracy validation tests for Talyn.
"""
import unittest
from talyn.inference.variable_elimination import variable_elimination
from talyn.inference.importance_sampling import importance_sampling

class TestInferenceAccuracy(unittest.TestCase):
    def test_variable_elimination(self):
        result = variable_elimination()
        self.assertTrue(abs(result['marginal'] - result['expected']) < 1e-2)

    def test_importance_sampling(self):
        result = importance_sampling()
        self.assertTrue(abs(result['mean'] - result['expected']) < 1e-2)

if __name__ == "__main__":
    unittest.main()
