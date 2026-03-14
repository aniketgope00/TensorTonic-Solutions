def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    values            = np.asarray(values)
    transform         = lambda x : np.log(1 + x)
    return transform(values)