import transdimensional_communication

class TransdimensionalCommunicationInterface(InterfaceBase):
    def __init__(self, transdimensional_communication_system):
        self.transdimensional_communication_system = transdimensional_communication_system

    def send_transdimensional_message(self, message):
        self.transdimensional_communication_system.send_transdimensional_message(message)

    def receive_transdimensional_message(self):
        return self.transdimensional_communication_system.receive_transdimensional_message()
