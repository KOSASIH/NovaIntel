import unittest
from src.core.neural_network_quantum_entanglement import NeuralNetworkQuantumEntanglement

class TestNeuralNetworkQuantumEntanglement(unittest.TestCase):
    def test_entangle_neurons(self):
        nnqe = NeuralNetworkQuantumEntanglement(NeuralNetwork(), QuantumProcessor())
        neurons = [Neuron(1), Neuron(2)]
        nnqe.entangle_neurons(neurons)
        self.assertTrue(nnqe.is_entangled)

if __name__ == '__main__':
    unittest.main()
