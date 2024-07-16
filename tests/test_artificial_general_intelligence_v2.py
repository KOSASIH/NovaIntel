import unittest
from src.core.artificial_general_intelligence_v2 import ArtificialGeneralIntelligenceV2

class TestArtificialGeneralIntelligenceV2(unittest.TestCase):
    def test_reason(self):
        agi = ArtificialGeneralIntelligenceV2(KnowledgeGraph(), NeuralNetwork(), QuantumProcessor())
        query = "What is the meaning of life?"
        result = agi.reason(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
