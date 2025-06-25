"""
Stub: Factor class for symbolic probabilistic graphs.
"""
import numpy as np
class Factor:
    def __init__(self, vars, table):
        self.vars = list(vars)
        self.table = np.array(table)
    def multiply(self, other):
        # Merge variables, preserving order and uniqueness
        vars = self.vars + [v for v in other.vars if v not in self.vars]
        # For stub, just use element-wise multiply and broadcast
        table = self.table * other.table
        return Factor(vars, table)
    def marginalize(self, var):
        # Remove var and sum over its axis
        if var not in self.vars:
            return Factor(self.vars, self.table)
        axis = self.vars.index(var)
        new_vars = [v for v in self.vars if v != var]
        table = self.table.sum(axis=axis)
        norm = table.sum() if hasattr(table, 'sum') else sum(table)
        if norm != 0:
            table = table / norm
        return Factor(new_vars, table)

