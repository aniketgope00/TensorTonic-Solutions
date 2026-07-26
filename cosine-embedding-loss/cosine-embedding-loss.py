import numpy as np

def norm(x):
    return np.linalg.norm(x)

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)

    dot_prod = np.dot(x1, x2)
    cosine   = dot_prod/(norm(x1) * norm(x2))

    if label == 1:
        return 1 - cosine
    else:
        return max(0, cosine - margin)