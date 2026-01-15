import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean   = float(np.mean(x))
    median = float(np.median(x)) 
    mode   = float(Counter(x).most_common(1)[0][0])
    return (mean, median, mode)