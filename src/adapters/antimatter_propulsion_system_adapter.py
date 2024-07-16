import antimatter_propulsion_system

class AntimatterPropulsionSystemAdapter(AdapterBase):
    def __init__(self, antimatter_propulsion_system_instance):
        self.antimatter_propulsion_system_instance = antimatter_propulsion_system_instance

    def connect(self):
        self.antimatter_propulsion_system_instance.activate_antimatter_propulsion_system()

    def disconnect(self):
        self.antimatter_propulsion_system_instance.deactivate_antimatter_propulsion_system()

    def get_propulsion_efficiency(self):
        return self.antimatter_propulsion_system_instance.get_propulsion_efficiency()
