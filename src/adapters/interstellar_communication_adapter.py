import socket

class InterstellarCommunicationAdapter(AdapterBase):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def disconnect(self):
        self.socket.close()

    def send(self, data):
        self.socket.send(data.encode())

    def receive(self):
        return self.socket.recv(1024).decode()
