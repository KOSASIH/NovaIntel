import wormhole

class WormholeCommunicationAdapter(AdapterBase):
    def __init__(self, wormhole_address):
        self.wormhole_address = wormhole_address
        self.wormhole = wormhole.Wormhole(self.wormhole_address)

    def connect(self):
        self.wormhole.connect()

    def disconnect(self):
        self.wormhole.close()

    def send(self, data):
        self.wormhole.send(data)

    def receive(self):
        return self.wormhole.recv()
