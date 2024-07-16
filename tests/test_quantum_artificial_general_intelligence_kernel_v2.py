import unittest
from src.core.quantum_artificial_general_intelligence_kernel_v2 import QuantumArtificialGeneralIntelligenceKernelV2

class TestQuantumArtificialGeneralIntelligenceKernelV2(unittest.TestCase):
    def test_reason_quantumly_v2(self):
        qagikv2 = QuantumArtificialGeneralIntelligenceKernelV2(KnowledgeGraph(), NeuralNetwork(), QuantumProcessor(), ExoticMatterEnergyConverter())
        query = "What is the nature of quantum artificial general intelligence?"
        result = qagikv2.reason_quantumly_v2(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
