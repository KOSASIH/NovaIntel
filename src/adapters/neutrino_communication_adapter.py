import neutrino

class NeutrinoCommunicationAdapter(AdapterBase):
    def __init__(self, neutrino_detector):
        self.neutrino_detector = neutrino_detector

    def connect(self):
        self.neutrino_detector.start()

    def disconnect(self):
        self.neutrino_detector.stop()

    def send(self, data):
        self.neutrino_detector.send_neutrino_signal(data)

    def receive(self):
        return self.neutrino_detector.receive_neutrino_signal()
