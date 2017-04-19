#!/usr/bin/python

import socket

HOST = "0.0.0.0"
PORT = 7070


def main():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(5)

    try:
        while True:
            c, addr = s.accept()
            print('Got connection from {}'.format(addr))
            msg = c.recv(1024)
            print("Received: {}".format(msg))
            c.send(b'FUTEBOL 0')

    finally:
        print('Closing socket')
        c.close()


if __name__ == "__main__":
    main()
