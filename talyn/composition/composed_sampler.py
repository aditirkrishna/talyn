"""
Stub: ComposedSampler for Talyn compositional sampling tests.
"""
class ComposedSampler:
    def __init__(self, nested=False):
        self.nested = nested
    def sample(self):
        import random
        return random.gauss(0, 1)
