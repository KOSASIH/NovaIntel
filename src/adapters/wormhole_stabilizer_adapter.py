import wormhole

class WormholeStabilizerAdapter(AdapterBase):
    def __init__(self, wormhole_stabilizer):
        self.wormhole_stabilizer = wormhole_stabilizer

    def connect(self):
        self.wormhole_stabilizer.stabilize_wormhole()

    def disconnect(self):
        self.wormhole_stabilizer.deactivate_wormhole()

    def send(self, data):
        self.wormhole_stabilizer.send_through_wormhole(data)

    def receive(self):
        return self.wormhole_stabilizer.receive_from_wormhole()
