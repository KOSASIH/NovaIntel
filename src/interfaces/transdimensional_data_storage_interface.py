import transdimensional_data_storage

class TransdimensionalDataStorageInterface(InterfaceBase):
    def __init__(self, transdimensional_data_storage_system):
        self.transdimensional_data_storage_system = transdimensional_data_storage_system

    def store_transdimensional_data(self, data):
        self.transdimensional_data_storage_system.store_transdimensional_data(data)

    def retrieve_transdimensional_data(self, data_id):
        return self.transdimensional_data_storage_system.retrieve_transdimensional_data(data_id)
