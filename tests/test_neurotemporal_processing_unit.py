import unittest
from src.core.neurotemporal_processing_unit import NeurotemporalProcessingUnit

class TestNeurotemporalProcessingUnit(unittest.TestCase):
    def test_process_neurotemporal_data(self):
        ntpu = NeurotemporalProcessingUnit(KnowledgeGraph(), NeuralNetwork(), QuantumProcessor(), ExoticMatterEnergyConverter())
        data = np.random.rand(100, 100)
        result = ntpu.process_neurotemporal_data(data)
        self.assertIsInstance(result, np.ndarray)

if __name__ == '__main__':
    unittest.main()
