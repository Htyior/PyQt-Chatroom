import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12365
addr_list = []
c_list = []
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(2)


def send_to_client1(c1, c2):
    while True:
        msg1 = c1.recv(1024).decode()
        c2.send(msg1.encode())

def send_to_client2(c1, c2):
    while True:
        msg = c2.recv(1024).decode()
        c1.send(msg.encode())

for i in range(0, 2):
     c, addr = s.accept()
     c_list.append(c)
     addr_list.append(addr)
     print(f"Got connection from {addr_list[i]}")

t1 = threading.Thread(target=send_to_client1, args=(c_list[0], c_list[1], ))
t2 = threading.Thread(target=send_to_client2, args=(c_list[0], c_list[1], ))

t1.start()
t2.start()