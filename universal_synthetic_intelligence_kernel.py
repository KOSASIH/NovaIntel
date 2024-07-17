import unittest
from src.core.universal_synthetic_intelligence_kernel import UniversalSyntheticIntelligenceKernel

class TestUniversalSyntheticIntelligenceKernel(unittest.TestCase):
    def test_reason_universally(self):
        usik = UniversalSyntheticIntelligenceKernel(KnowledgeGraph(), NeuralNetwork(), QuantumProcessor(), ExoticMatterEnergyConverter())
        query = "What is the nature of universal synthetic intelligence?"
        result = usik.reason_universally(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
