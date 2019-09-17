import numpy as np

# Temporar --------------------------

def sigmoid(x):
    # Functia de activare: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))
    # e = 2.7182
    # np.exp(-x) = e * e, de x ori

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    # Feedforward = Aa introduce input-urile in neuron
    def feedforward(self, inputs):
        result = np.dot(self.weights, inputs) + self.bias
        return sigmoid(result)

# ------------------------------------

class Network: 
    def __init__(self, weights = np.array([0, 0]), bias = 0):
        self.weights = weights 
        self.bias = bias

        self.neuron1 = Neuron(self.weights, self.bias)
        self.neuron2 = Neuron(self.weights, self.bias)
        self.neuronOutput1 = Neuron(self.weights, self.bias)

    def feedforward(self, inputs):
        outputNeuron1 = self.neuron1.feedforward(inputs)
        outputNeuron2 = self.neuron2.feedforward(inputs)

        output = self.neuronOutput1.feedforward(np.array([outputNeuron1, outputNeuron2]))

        return output

# ------------------------------------

weights = np.array([1, 1])
bias = 1

network = Network(weights, bias)

inputs = np.array([1, 1])

networkCalculation = network.feedforward(inputs)

print(networkCalculation)