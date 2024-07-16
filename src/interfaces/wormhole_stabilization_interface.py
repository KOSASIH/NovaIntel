import wormhole

class WormholeStabilizationInterface(InterfaceBase):
    def __init__(self, wormhole_stabilization_system):
        self.wormhole_stabilization_system = wormhole_stabilization_system

    def stabilize_wormhole(self, wormhole_coordinates):
        self.wormhole_stabilization_system.stabilize_wormhole(wormhole_coordinates)

    def get_wormhole_stability(self):
        return self.wormhole_stabilization_system.get_wormhole_stability_level()
