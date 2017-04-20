#!/usr/bin/python

import socket

HOST = socket.gethostname()
PORT = 9090


def main():
    try:
        s = socket.socket()
        s.connect((HOST, PORT))

        while True:
            msg = str.encode(input())
            print("Sending: {}".format(msg))
            s.send(msg)

            rsp = s.recv(1024)
            print(rsp.decode("utf-8"))
    except KeyboardInterrupt:
        print("Closing...")
        s.close()


if __name__ == "__main__":
    main()
