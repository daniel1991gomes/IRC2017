#!/usr/bin/python

import socket
import select

HOST = "0.0.0.0"
PORT = 8080


def main():
    try:
        # Setup server socket
        server = socket.socket()
        server.setblocking(0)
        server.bind((HOST, PORT))
        server.listen(5)
        print('Listening for connections at: {}:{}'.format(HOST, PORT))

        # Sockets from which we expect to read
        inputs = [server]

        # Wait of socket activity
        while inputs:
            inputready, _, _ = select.select(inputs, [], [])

            # Check which socket had activity
            for s in inputready:
                if s is server:
                    # A server socket is ready to accept a connection
                    c, addr = s.accept()
                    print('Got connection from {}'.format(addr))
                    inputs.append(c)
                else:
                    # A connected client has sent data
                    data = s.recv(1024)
                    if data:
                        parse_message(s, data)
                    else:
                        # Interpret empty result as closed connection
                        print('Client disconnected')
                        inputs.remove(s)
                        s.close()
    finally:
        server.close()


def parse_message(s, message):
    print("Received: {}".format(message))

    msg = message.decode().split(" ")

    if msg[0] == "GETRESULTS":
        m = get_results(msg[1])
    if msg[0] == "VOTE":
        m = vote(msg[1])

    message = str.encode(m)
    s.send(message)

def get_results(name):
    m = "ELEIcAO NAO ABRIU"
    f = open("elections.txt").read()
    if name in f:
        for l in f.splitlines():
            if l.split()[0] == name:
                estado = l.split()[1]
                if estado == "1":
                    m = "ELEIcAO ESTA A DECORRER"
                elif estado == "2":
                    m = open(name + ".txt").read()
    return m



if __name__ == "__main__":
    main()
