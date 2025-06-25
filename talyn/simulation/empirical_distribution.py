"""
Stub: EmpiricalDistribution for Talyn simulation.
"""
class EmpiricalDistribution:
    def __init__(self, samples=None):
        self.samples = samples or []
    def mean(self):
        return sum(self.samples) / len(self.samples) if self.samples else 0.0
