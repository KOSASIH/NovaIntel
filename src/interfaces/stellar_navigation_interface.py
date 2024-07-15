import numpy as np

class StellarNavigationInterface(InterfaceBase):
    def __init__(self, navigation_system):
        self.navigation_system = navigation_system

    def send(self, coordinates):
        self.navigation_system.plot_course(coordinates)

    def receive(self):
        return self.navigation_system.get_current_location()
