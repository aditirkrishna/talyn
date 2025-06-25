"""
Graph integrity tests for Talyn (factor multiplication, marginalization, BP).
"""
import unittest
from talyn.symbolic.factor import Factor
from talyn.symbolic.graph import BeliefGraph

class TestGraphIntegrity(unittest.TestCase):
    def test_factor_multiplication(self):
        f1 = Factor(['A'], [0.6, 0.4])
        f2 = Factor(['A', 'B'], [[0.1, 0.9],[0.2,0.8]])
        prod = f1.multiply(f2)
        self.assertEqual(prod.vars, ['A', 'B'])
        self.assertEqual(prod.table.shape, (2,2))

    def test_marginalization(self):
        f = Factor(['A', 'B'], [[0.1, 0.9],[0.2,0.8]])
        marg = f.marginalize('B')
        self.assertEqual(marg.vars, ['A'])
        self.assertAlmostEqual(sum(marg.table), 1.0, delta=1e-6)

    def test_belief_propagation_tree(self):
        g = BeliefGraph.tree_example()
        marginals = g.belief_propagation()
        for marg in marginals.values():
            self.assertAlmostEqual(sum(marg), 1.0, delta=1e-6)

    def test_belief_propagation_loopy(self):
        g = BeliefGraph.loopy_example()
        marginals = g.belief_propagation(max_iters=50)
        for marg in marginals.values():
            self.assertTrue(0.9 < sum(marg) < 1.1)

if __name__ == "__main__":
    unittest.main()
