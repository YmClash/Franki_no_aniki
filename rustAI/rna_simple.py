import numpy as np

class Neuron:
    def __init__(self, inputs, weights):
        self.inputs = inputs
        self.weights = weights

    def compute(self):
        weighted_sum = np.dot(self.inputs, self.weights)
        activation = self.activation_function(weighted_sum)
        return activation

    def activation_function(self, x):
        # You can use any activation function here, such as sigmoid, ReLU, etc.
        return 1 / (1 + np.exp(-x))

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers

    def add_layer(self, layer):
        self.layers.append(layer)

    def train(self, inputs, targets, learning_rate):
        for layer in self.layers:
            layer.inputs = inputs
            layer.weights = np.random.rand(layer.inputs.shape[1], layer.outputs)
            layer.compute()
            layer.weights = layer.weights * learning_rate

        for layer in reversed(self.layers):
            layer.inputs = layer.outputs
            layer.compute()
            layer.weights = layer.weights * learning_rate

    def predict(self, inputs):
        for layer in self.layers:
            layer.inputs = inputs
            layer.compute()
            inputs = layer.outputs

        return inputs