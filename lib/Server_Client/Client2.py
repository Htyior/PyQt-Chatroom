import socket
import threading

class Client2:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 12365
        self.s.connect(('127.0.0.1', self.port))

    def receve(self): # TODO: give username from another function
        while True:
            msg = self.s.recv(1024).decode()
            return(f"server: {msg}")
    
    def send(self, message):
        while True:
            self.s.send(message.encode())
