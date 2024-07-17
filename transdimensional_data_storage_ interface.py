import transdimensional_data_storage

class TransdimensionalDataStorageInterface(InterfaceBase):
    def __init__(self, transdimensional_data_storage_system):
        self.transdimensional_data_storage_system = transdimensional_data_storage_system

    def store_data_transdimensionally(self, data):
        self.transdimensional_data_storage_system.store_data_transdimensionally(data)

    def retrieve_data_transdimensionally(self):
        return self.transdimensional_data_storage_system.retrieve_data_transdimensionally()
