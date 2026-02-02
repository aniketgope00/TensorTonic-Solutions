def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    n              = len(series)
    percent_change = []
    for i in range(1, n):
        if series[i - 1] != 0:
            change = (series[i] - series[i - 1])/series[i - 1]
        else:
            change = 0.0
        percent_change.append(change)
    return percent_change