def getDifference(series):
    n = len(series)
    result = []
    for i in range(1, n):
        diff = series[i] - series[i - 1]
        result.append(diff)
    return result

def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for _ in range(order):
        series = getDifference(series)
    return series