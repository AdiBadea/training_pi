import numpy as np

def sigmoid(x):
    # Functia de activare: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))
    # e = 2.7182
    # np.exp(-x) = e * e, de x ori


