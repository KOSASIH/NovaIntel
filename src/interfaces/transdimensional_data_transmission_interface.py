import transdimensional_data_transmission

class TransdimensionalDataTransmissionInterface(InterfaceBase):
    def __init__(self, transdimensional_data_transmission_system):
        self.transdimensional_data_transmission_system = transdimensional_data_transmission_system

    def transmit_data_transdimensionally(self, data):
        self.transdimensional_data_transmission_system.transmit_data_transdimensionally(data)

    def receive_data_transdimensionally(self):
        return self.transdimensional_data_transmission_system.receive_data_transdimensionally()
