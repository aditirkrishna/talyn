"""
Talyn distributions: discrete and continuous distribution classes.
"""
import math
import random
from typing import Optional, Iterable, List, Set

class Bernoulli:
    """
    Bernoulli(p) distribution on {0,1}.
    """
    def __init__(self, p: float, rng_func: Optional[callable] = None):
        if not 0.0 <= p <= 1.0:
            raise ValueError("p must be in [0,1]")
        self.p = p
        self.rng = rng_func or random.random

    def sample(self) -> int:
        return 1 if self.rng() < self.p else 0

    def pmf(self, k: int) -> float:
        if k == 1:
            return self.p
        if k == 0:
            return 1 - self.p
        return 0.0

    prob = pmf

    def cdf(self, k: int) -> float:
        if k < 0:
            return 0.0
        if k < 1:
            return 1 - self.p
        return 1.0

class Binomial:
    """
    Binomial(n, p) distribution.
    """
    def __init__(self, n: int, p: float, rng_func: Optional[callable] = None):
        if n < 0:
            raise ValueError("n must be non-negative")
        if not 0.0 <= p <= 1.0:
            raise ValueError("p must be in [0,1]")
        self.n = n
        self.p = p
        self.rng = rng_func or random.random

    def sample(self) -> int:
        count = 0
        for _ in range(self.n):
            if self.rng() < self.p:
                count += 1
        return count

    def pmf(self, k: int) -> float:
        if k < 0 or k > self.n:
            return 0.0
        comb = math.comb(self.n, k)
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    prob = pmf

    def cdf(self, k: int) -> float:
        total = 0.0
        for i in range(0, k + 1):
            total += self.pmf(i)
        return total

class DiscreteUniform:
    """
    Discrete uniform distribution over integers 1..n.
    """
    def __init__(self, n: int, rng_func: Optional[callable] = None):
        if n <= 0:
            raise ValueError("n must be positive")
        self.n = n
        self.rng = rng_func or random.random

    def sample(self) -> int:
        return int(self.rng() * self.n) + 1

    def pmf(self, k: int) -> float:
        return 1.0 / self.n if 1 <= k <= self.n else 0.0

    prob = pmf

    def cdf(self, k: int) -> float:
        if k < 1:
            return 0.0
        if k >= self.n:
            return 1.0
        return k / self.n

class Geometric:
    """
    Geometric(p) distribution: trials until first success (support 1,2,...).
    """
    def __init__(self, p: float, rng_func: Optional[callable] = None):
        if not 0.0 < p <= 1.0:
            raise ValueError("p must be in (0,1]")
        self.p = p
        self.rng = rng_func or random.random

    def sample(self) -> int:
        count = 1
        while True:
            if self.rng() < self.p:
                return count
            count += 1

    def pmf(self, k: int) -> float:
        if k < 1:
            return 0.0
        return ((1 - self.p) ** (k - 1)) * self.p

    prob = pmf

    def cdf(self, k: int) -> float:
        if k < 1:
            return 0.0
        return 1 - (1 - self.p) ** k

class Poisson:
    """
    Poisson(lambda) distribution.
    """
    def __init__(self, lam: float, rng_func: Optional[callable] = None):
        if lam < 0:
            raise ValueError("lambda must be non-negative")
        self.lam = lam
        self.rng = rng_func or random.random

    def sample(self) -> int:
        L = math.exp(-self.lam)
        k = 0
        p = 1.0
        while p > L:
            p *= self.rng()
            k += 1
        return k - 1

    def pmf(self, k: int) -> float:
        if k < 0:
            return 0.0
        return (self.lam ** k) * math.exp(-self.lam) / math.factorial(k)

    prob = pmf

    def cdf(self, k: int) -> float:
        if k < 0:
            return 0.0
        total = 0.0
        for i in range(0, k + 1):
            total += self.pmf(i)
        return total

class Exponential:
    """
    Exponential(lambda) continuous distribution.
    """
    def __init__(self, lam: float, rng_func: Optional[callable] = None):
        if lam <= 0:
            raise ValueError("lambda must be positive")
        self.lam = lam
        self.rng = rng_func or random.random

    def sample(self) -> float:
        u = self.rng()
        return -math.log(1 - u) / self.lam

    def pdf(self, x: float) -> float:
        return self.lam * math.exp(-self.lam * x) if x >= 0 else 0.0

    def cdf(self, x: float) -> float:
        return 1 - math.exp(-self.lam * x) if x >= 0 else 0.0

class ContinuousUniform:
    """
    Continuous uniform distribution on [a, b].
    """
    def __init__(self, a: float, b: float, rng_func: Optional[callable] = None):
        if b <= a:
            raise ValueError("b must be > a")
        self.a = a
        self.b = b
        self.rng = rng_func or random.random

    def sample(self) -> float:
        return self.a + (self.b - self.a) * self.rng()

    def pdf(self, x: float) -> float:
        return 1.0 / (self.b - self.a) if self.a <= x <= self.b else 0.0

    def cdf(self, x: float) -> float:
        if x < self.a:
            return 0.0
        if x > self.b:
            return 1.0
        return (x - self.a) / (self.b - self.a)

class Normal:
    """
    Standard normal distribution via Box-Muller.
    """
    def __init__(self, rng_func: Optional[callable] = None):
        self.rng = rng_func or random.random
        self._cache: Optional[float] = None

    def sample(self) -> float:
        if self._cache is not None:
            z = self._cache
            self._cache = None
            return z
        u1 = self.rng()
        u2 = self.rng()
        r = math.sqrt(-2 * math.log(u1))
        theta = 2 * math.pi * u2
        z0 = r * math.cos(theta)
        z1 = r * math.sin(theta)
        self._cache = z1
        return z0

    def pdf(self, x: float) -> float:
        return (1.0 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x * x)

    def cdf(self, x: float) -> float:
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))
