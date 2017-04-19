#!/usr/bin/python

import socket

s = socket.socket()
host = "0.0.0.0"
port = 7070
s.bind((host, port))

s.listen(5)

try:
    while True:
        c, addr = s.accept()
        print('Got connection from {}'.format(addr))
        msg = c.recv(1024)
        print("Received: {}".format(msg))
        c.close()
finally:
    print('Closing socket')
    c.close()
