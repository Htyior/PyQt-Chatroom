import threading
import socket


class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 12365
        self.addr_list = []
        self.c_list = []
        self.s.bind(('', self.port))
        self.s.listen(2)
    
    def send_to_client1(c1, c2):
        while True:
            msg1 = c1.recv(1024).decode()
            c2.send(msg1.encode())
    
    def send_to_client2(c1, c2):
        while True:
            msg = c2.recv(1024).decode()
            c1.send(msg.encode())

    def start_server(self):
        for i in range(0, 2):
            c, addr = self.s.accept()
            self.c_list.append(c)
            self.addr_list.append(addr)
            print(f"Got connection from {self.addr_list[i]}")

        t1 = threading.Thread(target=Server.send_to_client1, args=(self.c_list[0], self.c_list[1], ))
        t2 = threading.Thread(target=Server.send_to_client2, args=(self.c_list[0], self.c_list[1], ))

        t1.start()
        t2.start()