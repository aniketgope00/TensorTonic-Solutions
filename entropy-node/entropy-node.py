import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y               = np.asarray(y)
    n               = y.shape[0]
    value, counts   = np.unique(y, return_counts = True)
    probs           = counts/n
    return np.sum(-1 * (probs * np.emath.log2(probs)))