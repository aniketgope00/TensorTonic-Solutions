import math
import numpy as np

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit using the high-precision 
    approximation used in modern neural networks.
    """
    x              = np.array(x)
    vectorized_erf = np.vectorize(math.erf)
    erf            = vectorized_erf(x/np.sqrt(2))
    return (0.5 * x) * ( 1 + erf) 