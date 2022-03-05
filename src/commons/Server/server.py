import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12344
c_list = []
addr_list = []
s.bind(('', port))
s.listen(5)


def receve_from_client1(c1):
    while True:
        msg = c1.recv(1024).decode()

        f = open('Client.txt', 'a+')
        f.write("Client2: " + msg + "\n")
        f.close()

def receve_from_client2(c2):
    while True:
        msg = c2.recv(1024).decode()

        f = open('Client2.txt', 'a+')
        f.write("Client2: " + msg + "\n")
        f.close()

for i in range(0, 2):
    c, addr = s.accept()
    c_list.append(c)
    addr_list.append(addr)
    print(f"Got a connection from {addr_list[i]}")

t1 = threading.Thread(target=receve_from_client1, args=(c_list[0], ))
t2 = threading.Thread(target=receve_from_client2, args=(c_list[1], ))

t1.start()
t2.start()