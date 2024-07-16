import wormhole

class WormholeStabilizationAdapter(AdapterBase):
    def __init__(self, wormhole_stabilization_system):
        self.wormhole_stabilization_system = wormhole_stabilization_system

    def connect(self):
        self.wormhole_stabilization_system.stabilize_wormhole()

    def disconnect(self):
        self.wormhole_stabilization_system.destabilize_wormhole()

    def get_wormhole_stability(self):
        return self.wormhole_stabilization_system.get_wormhole_stability_level()
