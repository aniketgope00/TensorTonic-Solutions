def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    W = np.asarray(W)
    L = np.sqrt(6/(fan_in + fan_out))
    mapper = lambda x: x * (2*L) - L
    return mapper(W)