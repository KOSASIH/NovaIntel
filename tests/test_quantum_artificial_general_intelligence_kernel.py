import unittest
from src.core.quantum_artificial_general_intelligence_kernel import QuantumArtificialGeneralIntelligenceKernel

class TestQuantumArtificialGeneralIntelligenceKernel(unittest.TestCase):
    def test_reason_quantumly(self):
        qagik = QuantumArtificialGeneralIntelligenceKernel(KnowledgeGraph(), NeuralNetwork(), QuantumProcessor())
        query = "What is the nature of quantum artificial general intelligence?"
        result = qagik.reason_quantumly(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
