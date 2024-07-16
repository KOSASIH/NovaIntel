import numpy as np

class DarkEnergyInterface(InterfaceBase):
    def __init__(self, dark_energy_system):
        self.dark_energy_system = dark_energy_system

    def send(self, energy_signature):
        self.dark_energy_system.inject_dark_energy(energy_signature)

    def receive(self):
        return self.dark_energy_system.get_dark_energy_level()
