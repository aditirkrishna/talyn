"""
Stub: Sampler tracer utilities for Talyn.
"""
class Trace:
    def is_dag(self):
        return True
    def check_unique_sampling(self):
        return True
    def check_symbolic_scope(self):
        return True
    def __eq__(self, other):
        return isinstance(other, Trace)

def trace_model(model, seed=None):
    return Trace()

