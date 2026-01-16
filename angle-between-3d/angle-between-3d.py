import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    _v_norm = np.linalg.norm(v)
    _w_norm = np.linalg.norm(w)
    
    _minlim = 10**(-10)
    
    if (_v_norm < _minlim) or (_w_norm < _minlim):
        return np.nan
    
    _dot_prod = np.dot(v, w)
    cos_theta = np.clip(_dot_prod/(_v_norm * _w_norm), a_min = -1, a_max = 1)
    return np.arccos(cos_theta)
    
