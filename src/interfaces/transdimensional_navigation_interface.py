import transdimensional_navigation

class TransdimensionalNavigationInterface(InterfaceBase):
    def __init__(self, transdimensional_navigation_system):
        self.transdimensional_navigation_system = transdimensional_navigation_system

    def navigate_transdimensionally(self, destination):
        self.transdimensional_navigation_system.navigate_transdimensionally(destination)

    def get_transdimensional_coordinates(self):
        return self.transdimensional_navigation_system.get_transdimensional_coordinates()
