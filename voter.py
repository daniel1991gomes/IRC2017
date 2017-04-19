#!/usr/bin/env python

import socket
import sys

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print('sending {}'.format(message))
    socket.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = socket.recv(16)
        amount_received += len(data)
        print >> sys.stderr, 'received "%s"' % data

finally:
    print('closing socket')
    socket.close()