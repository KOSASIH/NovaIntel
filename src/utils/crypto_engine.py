import cryptography

class CryptoEngine:
    def __init__(self, key):
        self.key = key
        self.cipher = cryptography.Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data)

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data)
