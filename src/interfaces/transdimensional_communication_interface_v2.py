import transdimensional_communication

class TransdimensionalCommunicationInterfaceV2(InterfaceBase):
    def __init__(self, transdimensional_communication_system):
        self.transdimensional_communication_system = transdimensional_communication_system

    def transmit_data_transdimensionally_v2(self, data):
        self.transdimensional_communication_system.transmit_data_transdimensionally_v2(data)

    def receive_data_transdimensionally_v2(self):
        return self.transdimensional_communication_system.receive_data_transdimensionally_v2()
