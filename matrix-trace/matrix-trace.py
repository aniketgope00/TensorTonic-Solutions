import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    trace: float = 0.0
    m: int = len(A)
    n: int = len(A[0])
    if (m == 1) and (n == 1):
        return A[0][0]
    else:
        for i in range(m):
            for j in range(n):
                if i == j:
                    trace += A[i][j]
        return trace