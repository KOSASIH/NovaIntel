import exotic_matter_energy_converter

class ExoticMatterEnergyConverterAdapter(AdapterBase):
    def __init__(self, exotic_matter_energy_converter_system):
        self.exotic_matter_energy_converter_system = exotic_matter_energy_converter_system

    def connect(self):
        self.exotic_matter_energy_converter_system.activate_exotic_matter_energy_converter()

    def disconnect(self):
        self.exotic_matter_energy_converter_system.deactivate_exotic_matter_energy_converter()

    def get_energy_conversion_efficiency(self):
        return self.exotic_matter_energy_converter_system.get_energy_conversion_efficiency()
