#!/usr/bin/python

import socket
HOST = socket.gethostname()
PORT = 8080


def main():
    s = socket.socket()
    s.connect((HOST, PORT))

    m = input()
    if m == "EXIT":
        s.close()
    msg = str.encode(m)
    print("Sending: {}".format(msg))
    s.send(msg)

    rsp = s.recv(1024)
    print(rsp.decode("utf-8"))
#    print("Received: {}".format(rsp))





if __name__ == "__main__":
    main()
