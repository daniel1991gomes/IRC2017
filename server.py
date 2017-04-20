#!/usr/bin/python

import socket

HOST = "0.0.0.0"
PORT = 9090


def main():
    try:
        # Receive client connections
        server = socket.socket()
        server.bind((HOST, PORT))
        server.listen(5)
        print('Listening for connections at: {}:{}'.format(HOST, PORT))

        while True:
            # Client connected
            c, addr = server.accept()
            print('Client connected: {}'.format(addr))

            # Check if election is open
            message = c.recv(1024)
            if message is None:
                print('Client disconnected: {}'.format(addr))
                c.close()
                continue
            print("Received: {}".format(message))
            msg = message.decode().split()
            if msg[0] == "GETRESULTS":
                m = get_results(msg[1])
                c.send(str.encode(m))
            else:
                print('Invalid Command: {}'.format(msg[0]))
                c.close()
                continue

            # Check if election is open
            message = c.recv(1024)
            if message is None:
                print('Client disconnected: {}'.format(addr))
                c.close()
                continue
            print("Received: {}".format(message))
            msg = message.decode().split()
            vote_id = ''
            if msg[0] == "ID":
                vote_id = msg[1]
                c.send(str.encode("SUCCESS"))
            else:
                print('Invalid Command: {}'.format(msg[0]))
                c.close()
                continue

            # Vote
            message = c.recv(1024)
            if message is None:
                print('Client disconnected: {}'.format(addr))
                c.close()
                continue
            print("Received: {}".format(message))
            msg = message.decode().split()
            vote = ''
            if msg[0] == "VOTE":
                vote = msg[1]
                c.send(str.encode("SUCCESS"))
            else:
                print('Invalid Command: {}'.format(msg[0]))
                c.close()
                continue

            print("Client {} voted on {}".format(vote_id, vote))

    except KeyboardInterrupt:
        print("Shutting Down...")
        server.close()
    except Exception as e:
        print(e)
        server.close()
    finally:
        print("Finally...")
        server.close()


def get_results(name):
    m = "Not Found"
    f = open("elections.txt").read()
    if name in f:
        for l in f.splitlines():
            if l.split()[0] == name:
                estado = l.split()[1]
                if estado == "1":
                    m = "SUCCESS"
                elif estado == "2":
                    m = open(name + ".txt").read()
    return m


if __name__ == "__main__":
    main()
