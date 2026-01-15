import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    result = []
    for percentile in q:
        _percentile_val = np.percentile(x, percentile, method = "linear")
        result.append(_percentile_val)
    return np.array(result)