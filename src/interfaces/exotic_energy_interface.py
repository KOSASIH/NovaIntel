import numpy as np

class ExoticEnergyInterface(InterfaceBase):
    def __init__(self, exotic_energy_system):
        self.exotic_energy_system = exotic_energy_system

    def send(self, energy_signature):
        self.exotic_energy_system.inject_exotic_energy(energy_signature)

    def receive(self):
        return self.exotic_energy_system.get_exotic_energy_level()
