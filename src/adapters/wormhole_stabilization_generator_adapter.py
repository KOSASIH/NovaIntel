import wormhole_stabilization_generator

class WormholeStabilizationGeneratorAdapter(AdapterBase):
    def __init__(self, wormhole_stabilization_generator_system):
        self.wormhole_stabilization_generator_system = wormhole_stabilization_generator_system

    def connect(self):
        self.wormhole_stabilization_generator_system.activate_wormhole_stabilization_generator()

    def disconnect(self):
        self.wormhole_stabilization_generator_system.deactivate_wormhole_stabilization_generator()

    def get_wormhole_stability(self):
        return self.wormhole_stabilization_generator_system.get_wormhole_stability_level()
