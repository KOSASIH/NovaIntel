import unittest
from src.core.quantum_processor import QuantumProcessor

class TestQuantumProcessor(unittest.TestCase):
    def test_execute(self):
        processor = QuantumProcessor('ibmq_qasm_simulator')
        circuit = qiskit.QuantumCircuit(5, 5)
        result = processor.execute(circuit)
        self.assertIsInstance(result, qiskit.result.Result)

if __name__ == '__main__':
    unittest.main()
