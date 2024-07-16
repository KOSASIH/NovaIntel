import wormhole_stabilization_generator_v2

class WormholeStabilizationGeneratorV2Adapter(AdapterBase):
    def __init__(self, wormhole_stabilization_generator_v2_system):
        self.wormhole_stabilization_generator_v2_system = wormhole_stabilization_generator_v2_system

    def connect(self):
        self.wormhole_stabilization_generator_v2_system.activate_wormhole_stabilization_generator_v2()

    def disconnect(self):
        self.wormhole_stabilization_generator_v2_system.deactivate_wormhole_stabilization_generator_v2()

    def get_wormhole_stability_v2(self):
        return self.wormhole_stabilization_generator_v2_system.get_wormhole_stability_level_v2()
