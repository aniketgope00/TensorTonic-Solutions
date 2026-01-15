import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    _norm_a = np.linalg.norm(a)
    _norm_b = np.linalg.norm(b)
    if (_norm_a == 0) or (_norm_b == 0):
        return 0.0
    else:
        return np.dot(a, b)/(_norm_a * _norm_b)