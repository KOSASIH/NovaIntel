import unittest
from src.core.quantum_artificial_general_intelligence import QuantumArtificialGeneralIntelligence

class TestQuantumArtificialGeneralIntelligence(unittest.TestCase):
    def test_reason_quantumly(self):
        qagi = QuantumArtificialGeneralIntelligence(KnowledgeGraph(), NeuralNetwork(), QuantumProcessor())
        query = "What is the nature of quantum consciousness?"
        result = qagi.reason_quantumly(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
