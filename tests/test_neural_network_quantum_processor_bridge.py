import unittest
from src.core.neural_network_quantum_processor_bridge import NeuralNetworkQuantumProcessorBridge

class TestNeuralNetworkQuantumProcessorBridge(unittest.TestCase):
    def test_integrate_neural_network_with_quantum_processor(self):
        nnqp_bridge = NeuralNetworkQuantumProcessorBridge(NeuralNetwork(), QuantumProcessor())
        nnqp_bridge.integrate_neural_network_with_quantum_processor()
        self.assertTrue(nnqp_bridge.is_integrated)

if __name__ == '__main__':
    unittest.main()
