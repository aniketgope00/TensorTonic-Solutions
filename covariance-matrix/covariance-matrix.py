import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X       = np.asarray(X)
    if X.ndim != 2 or X.shape[0] < 2:
        return None
    mean    = np.mean(X, axis = 0, keepdims = True)
    X_cent  = X - mean
    n       = X.shape[0]
    cov     = (1 / (n - 1)) * (X_cent.T @ X_cent)
    return cov