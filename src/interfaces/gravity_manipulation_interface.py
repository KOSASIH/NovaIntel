import numpy as np

class GravityManipulationInterface(InterfaceBase):
    def __init__(self, gravity_manipulation_system):
        self.gravity_manipulation_system = gravity_manipulation_system

    def send(self, gravity_waveform):
        self.gravity_manipulation_system.manipulate_gravity(gravity_waveform)

    def receive(self):
        return self.gravity_manipulation_system.get_gravity_field()
