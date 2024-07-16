import unittest
from src.core.artificial_general_intelligence_kernel import ArtificialGeneralIntelligenceKernel

class TestArtificialGeneralIntelligenceKernel(unittest.TestCase):
    def test_reason_artificially(self):
        agik = ArtificialGeneralIntelligenceKernel(KnowledgeGraph(), NeuralNetwork(), QuantumProcessor())
        query = "What is the nature of artificial general intelligence?"
        result = agik.reason_artificially(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
