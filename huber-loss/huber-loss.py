import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    error = y_true - y_pred
    abs_error = np.abs(error)

    quadratic_loss = 0.5 * (error ** 2)
    linear_loss = delta * (abs_error - 0.5 * delta)
    
    losses = np.where(abs_error <= delta, quadratic_loss, linear_loss)
    
    return float(np.mean(losses))