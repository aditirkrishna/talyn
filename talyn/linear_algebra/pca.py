"""
Talyn linear algebra: Principal Component Analysis implementation.
"""
from typing import List, Tuple
import math
import random
from .covariance import covariance_matrix

def pca(data: List[List[float]], n_components: int = 2) -> Tuple[List[List[float]], List[float], List[List[float]]]:
    """
    Perform PCA dimensionality reduction.
    Args:
        data: Input data (list of vectors)
        n_components: Number of principal components to keep
    Returns:
        (transformed_data, explained_variance, components)
    """
    if not data or not data[0]:
        return [], [], []
    
    # Calculate covariance matrix
    cov = covariance_matrix(data)
    dim = len(cov)
    
    # Power iteration to find top eigenvectors
    components = []
    explained_variance = []
    
    for _ in range(n_components):
        # Initialize random vector
        v = [random.random() for _ in range(dim)]
        v_norm = math.sqrt(sum(x**2 for x in v))
        v = [x/v_norm for x in v]
        
        # Power iteration
        for _ in range(100):
            v_new = [sum(cov[i][j] * v[j] for j in range(dim)) for i in range(dim)]
            v_norm = math.sqrt(sum(x**2 for x in v_new))
            v = [x/v_norm for x in v_new]
        
        # Deflate matrix
        for i in range(dim):
            for j in range(dim):
                cov[i][j] -= v[i] * v[j] * sum(v[k] * sum(cov[k][l] * v[l] for l in range(dim)) for k in range(dim))
        
        components.append(v)
        explained_variance.append(sum(v[i] * sum(cov[i][j] * v[j] for j in range(dim)) for i in range(dim)))
    
    # Transform data
    transformed = []
    for vector in data:
        transformed.append([sum(comp[i] * vector[i] for i in range(dim)) for comp in components])
    
    return transformed, explained_variance, components
