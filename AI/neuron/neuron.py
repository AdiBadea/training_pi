import numpy as np

def sigmoid(x):
    # Functia de activare: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))
    # e = 2.7182
    # np.exp(-x) = e * e, de x ori

# print(sigmoid(3))

def class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    # Feedforward = Aa introduce input-urile in neuron
    def feedforward(self, inputs):

