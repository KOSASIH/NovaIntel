import antimatter

class AntimatterPowerSourceAdapter(AdapterBase):
    def __init__(self, antimatter_power_source):
        self.antimatter_power_source = antimatter_power_source

    def connect(self):
        self.antimatter_power_source.activate_antimatter_reactor()

    def disconnect(self):
        self.antimatter_power_source.deactivate_antimatter_reactor()

    def get_power_level(self):
        return self.antimatter_power_source.get_antimatter_energy_level()
