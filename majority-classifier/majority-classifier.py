import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    majority_elem = np.argmax(np.bincount(y_train))
    return np.full(X_test.shape[0], majority_elem)