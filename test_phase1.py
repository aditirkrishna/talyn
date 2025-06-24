import talyn.rng as rng_module
from talyn.rng import LCG, XORShift32
from talyn.rng_stats import rng_histogram, chi_square_statistic
from talyn.sample_space import SampleSpace
from talyn.probability import ProbabilityMeasure, validate_nonnegativity, validate_unit_total

def main():
    rng = LCG(42)
    print("LCG sample:", rng.random())
    xrng = XORShift32(42)
    print("XORShift sample:", xrng.random())
    tests = rng_histogram(rng.random, n=1000, bins=10)
    print("Histogram:", tests, "Chi2:", chi_square_statistic(tests))
    space = SampleSpace([1,2,3])
    pm = ProbabilityMeasure(space, {1:1,2:1,3:1})
    print("P({1,2}):", pm.prob({1,2}))
    validate_nonnegativity(pm)
    validate_unit_total(pm)
    print("All Phase1 tests passed")

if __name__ == "__main__":
    main()
