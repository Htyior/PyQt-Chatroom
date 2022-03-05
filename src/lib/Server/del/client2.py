import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12344
s.connect(('127.0.0.1', port))

def send():
    while True:
        message = input("Me: ")
        s.send(message.encode())

def receve():
    f = open('Client2.txt', 'r')
    while True:
        content = f.read()
        print(content)


t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receve)


t1.start()
t2.start()