import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v       = np.asarray(v, dtype = float)
    n       = v.shape[0]
    _zeros  = np.zeros((n, n))
    for i in range(n):
        _zeros[i][i] = v[i]
    return _zeros