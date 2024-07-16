import unittest
from src.core.neural_network_quantum_teleportation import NeuralNetworkQuantumTeleportation

class TestNeuralNetworkQuantumTeleportation(unittest.TestCase):
    def test_teleport_neural_network(self):
        nnqt = NeuralNetworkQuantumTeleportation(NeuralNetwork(), QuantumProcessor())
        destination = "QuantumComputer123"
        nnqt.teleport_neural_network(destination)
        self.assertTrue(nnqt.is_teleported)

if __name__ == '__main__':
    unittest.main()
