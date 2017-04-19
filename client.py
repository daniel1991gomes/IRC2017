#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 7070

s.connect((host, port))
s.send(b'Thank you for connecting')
s.close()
