import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    matrix = np.asarray(matrix)
    if matrix.ndim != 2 or (matrix.shape[0] != matrix.shape[1]): return None
    if matrix.size == 0:
        return np.array([])
    try:
        eigen_values    = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None
    indices  = np.lexsort((eigen_values.imag, eigen_values.real))
    return eigen_values[indices]