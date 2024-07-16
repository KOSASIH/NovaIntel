import exotic_energy

class ExoticEnergySourceAdapter(AdapterBase):
    def __init__(self, exotic_energy_source):
        self.exotic_energy_source = exotic_energy_source

    def connect(self):
        self.exotic_energy_source.activate_exotic_energy_source()

    def disconnect(self):
        self.exotic_energy_source.deactivate_exotic_energy_source()

    def get_energy_level(self):
        return self.exotic_energy_source.get_exotic_energy_level()
