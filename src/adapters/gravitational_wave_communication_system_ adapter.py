import gravitational_wave_communication_system

class GravitationalWaveCommunicationSystemAdapter(AdapterBase):
    def __init__(self, gravitational_wave_communication_system_instance):
        self.gravitational_wave_communication_system_instance = gravitational_wave_communication_system_instance

    def connect(self):
        self.gravitational_wave_communication_system_instance.activate_gravitational_wave_communication_system()

    def disconnect(self):
        self.gravitational_wave_communication_system_instance.deactivate_gravitational_wave_communication_system()

    def get_communication_efficiency(self):
        return self.gravitational_wave_communication_system_instance.get_communication_efficiency()
