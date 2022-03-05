import socket
import threading
import os

class hello:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 12345
        self.c_list = []
        self.addr_list = []
        self.s.bind('', self.port)
        self.s.listen(5)

    def receve_from_client1(self, c1):
        while True:
            msg = c1.revc(1024).decode()
            """ Writing the message in file """

            f = open('client1.txt', 'a+')
            f.write("Client2: " + msg + "\n")
            f.close()

    def receve_from_client2(self, c2):
        while True:
            msg = c2.recv(1024).decode()
            """ Writing the message in the file"""

            f = open('client2', 'a+')
            f.write("Client1: " + msg + "\n")
            f.close()