""" Reading messages from a file """

import socket

class client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 12345
        self.s.connect(('127.0.0.1', self.port))

    def send(self, message):
        self.s.send(message.encode())
    
    def receve(self):
        f = open('client1.txt', 'r')
        content = f.read()
        return content