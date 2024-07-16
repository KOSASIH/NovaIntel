import wormhole

class WormholeStabilizerV2Adapter(AdapterBase):
    def __init__(self, wormhole_stabilizer_v2):
        self.wormhole_stabilizer_v2 = wormhole_stabilizer_v2

    def connect(self):
        self.wormhole_stabilizer_v2.stabilize_wormhole_v2()

    def disconnect(self):
        self.wormhole_stabilizer_v2.deactivate_wormhole_v2()

    def send(self, data):
        self.wormhole_stabilizer_v2.send_through_wormhole_v2(data)

    def receive(self):
        return self.wormhole_stabilizer_v2.receive_from_wormhole_v2()
