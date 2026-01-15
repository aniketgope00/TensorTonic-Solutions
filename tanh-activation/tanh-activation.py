import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    return np.tanh(np.atleast_1d(x), dtype = float)