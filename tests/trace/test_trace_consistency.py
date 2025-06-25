"""
Trace consistency tests for Talyn (DAG, variable scoping, reproducibility).
"""
import unittest
from talyn.ppl.core import run_model
from talyn.symbolic.sampler_tracer import trace_model

class TestTraceConsistency(unittest.TestCase):
    def test_dag_structure(self):
        # Example model: simple Bayesian net
        def model():
            x = run_model("normal", mu=0, sigma=1)
            y = run_model("normal", mu=x, sigma=1)
            return x, y
        trace = trace_model(model)
        # Check for acyclicity
        self.assertTrue(trace.is_dag())
        # Each variable sampled once per scope
        self.assertTrue(trace.check_unique_sampling())

    def test_reproducibility(self):
        def model():
            x = run_model("normal", mu=0, sigma=1)
            y = run_model("normal", mu=x, sigma=1)
            return x, y
        trace1 = trace_model(model, seed=42)
        trace2 = trace_model(model, seed=42)
        self.assertEqual(trace1, trace2)

    def test_symbolic_scope(self):
        def model():
            a = run_model("bernoulli", p=0.5)
            b = run_model("bernoulli", p=0.5)
            return a, b
        trace = trace_model(model)
        self.assertTrue(trace.check_symbolic_scope())

if __name__ == "__main__":
    unittest.main()
