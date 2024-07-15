import numpy as np

class ExoticMatterInterface(InterfaceBase):
    def __init__(self, exotic_matter_system):
        self.exotic_matter_system = exotic_matter_system

    def send(self, energy_signature):
        self.exotic_matter_system.inject_energy(energy_signature)

    def receive(self):
        return self.exotic_matter_system.get_energy_level()
