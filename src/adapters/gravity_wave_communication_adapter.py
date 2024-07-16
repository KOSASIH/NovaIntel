import gravity_wave

class GravityWaveCommunicationAdapter(AdapterBase):
    def __init__(self, gravity_wave_transceiver):
        self.gravity_wave_transceiver = gravity_wave_transceiver

    def connect(self):
        self.gravity_wave_transceiver.initialize_transceiver()

    def disconnect(self):
        self.gravity_wave_transceiver.shutdown_transceiver()

    def send(self, data):
        self.gravity_wave_transceiver.send_gravity_wave(data)

    def receive(self):
        return self.gravity_wave_transceiver.receive_gravity_wave()
