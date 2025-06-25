"""
Stub: Moments utilities for Talyn (mean, variance, skewness, kurtosis).
"""
def mean(data):
    return sum(data) / len(data)
def variance(data):
    m = mean(data)
    return sum((x-m)**2 for x in data) / len(data)
def skewness(data):
    return 0.0
def kurtosis(data):
    return 0.0
