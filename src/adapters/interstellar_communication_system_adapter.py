import interstellar_communication_system

class InterstellarCommunicationSystemAdapter(AdapterBase):
    def __init__(self, interstellar_communication_system_instance):
        self.interstellar_communication_system_instance = interstellar_communication_system_instance

    def connect(self):
        self.interstellar_communication_system_instance.activate_interstellar_communication_system()

    def disconnect(self):
        self.interstellar_communication_system_instance.deactivate_interstellar_communication_system()

    def get_communication_efficiency(self):
        return self.interstellar_communication_system_instance.get_communication_efficiency()
