import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    # check if matrix is 2D
    THRESH = 10 ** (-10)
    A = np.asarray(A, dtype = float)
    if A.ndim < 2:
        return None
    if A.shape[0] != A.shape[1]:
        return None
    if abs(np.linalg.det(A)) < THRESH:
        return None
    return np.linalg.inv(A)

     
