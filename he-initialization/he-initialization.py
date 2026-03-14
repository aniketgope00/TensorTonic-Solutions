def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    W = np.asarray(W)
    L = np.sqrt(6/fan_in)
    mapper = lambda x: x * (2*L) - L
    return mapper(W)