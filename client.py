#!/usr/bin/python

import socket
HOST = socket.gethostname()
PORT = 8080


def main():
    s = socket.socket()
    s.connect((HOST, PORT))

    msg = b'GETRESULTS FUTEBOL'
    print("Sending: {}".format(msg))
    s.send(msg)

    rsp = s.recv(1024)
    print("Received: {}".format(rsp))
    s.close()


if __name__ == "__main__":
    main()
