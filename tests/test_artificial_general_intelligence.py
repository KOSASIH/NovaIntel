import unittest
from src.core.artificial_general_intelligence import ArtificialGeneralIntelligence

class TestArtificialGeneralIntelligence(unittest.TestCase):
    def test_reason(self):
        agi = ArtificialGeneralIntelligence(KnowledgeGraph(), NeuralNetwork())
        query = "What is the meaning of life?"
        result = agi.reason(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
