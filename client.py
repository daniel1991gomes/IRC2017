#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 7070

s.connect((host, port))

msg = b'Thank you for connecting'
print("Sending: {}".format(msg))

s.send(msg)
s.close()
