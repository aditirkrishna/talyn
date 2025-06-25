"""
Talyn linear algebra: Covariance matrix implementation.
"""
from typing import List
import math

def covariance_matrix(data: List[List[float]]) -> List[List[float]]:
    """
    Calculate covariance matrix for multivariate data.
    Args:
        data: List of vectors (each vector is a list of floats)
    Returns:
        Covariance matrix
    """
    if not data or not data[0]:
        return []
    
    n = len(data)
    dim = len(data[0])
    
    # Calculate means for each dimension
    means = [sum(vector[i] for vector in data)/n for i in range(dim)]
    
    # Initialize covariance matrix
    cov = [[0.0 for _ in range(dim)] for _ in range(dim)]
    
    # Fill covariance matrix
    for i in range(dim):
        for j in range(i, dim):
            cov_ij = sum((vector[i] - means[i]) * (vector[j] - means[j]) for vector in data) / (n - 1)
            cov[i][j] = cov_ij
            if i != j:
                cov[j][i] = cov_ij
    
    return cov
