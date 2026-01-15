import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    return np.maximum(0, np.atleast_1d(x))
