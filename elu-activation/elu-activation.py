import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    res = []
    for value in x:
        if value > 0:
            res.append(value)
        else:
            elu_x = alpha * ((np.e ** value) - 1)
            res.append(elu_x)
    return res