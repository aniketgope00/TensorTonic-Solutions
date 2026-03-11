def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    ema = []
    if len(values) == 1:
        return [values[0]]
    else:
        ema.append(values[0])
        for i in range(1, len(values)):
            ema_t = alpha * values[i] + (1 - alpha) * ema[i - 1]
            ema.append(ema_t)
    return ema