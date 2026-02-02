import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    image = np.asarray(image).flatten()
    hist  = [0] * 256
    for pixel in image:
        hist[pixel] += 1
    return hist