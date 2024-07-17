import quantum_entanglement

class QuantumEntanglementInterface(InterfaceBase):
    def __init__(self, quantum_entanglement_system):
        self.quantum_entanglement_system = quantum_entanglement_system

    def entangle_particles(self, particles):
        self.quantum_entanglement_system.entangle_particles(particles)

    def measure_entanglement(self):
        return self.quantum_entanglement_system.measure_entanglement()
