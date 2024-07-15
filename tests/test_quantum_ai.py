import unittest
from src.core.quantum_ai import QuantumAI

class TestQuantumAI(unittest.TestCase):
    def test_process_quantum_data(self):
        qai = QuantumAI(QuantumProcessor(), KnowledgeGraph())
        data = np.random.rand(10, 10)
        result = qai.process_quantum_data(data)
        self.assertIsInstance(result, np.ndarray)

if __name__ == '__main__':
    unittest.main()
