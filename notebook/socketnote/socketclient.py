#!/usr/bin/env python
# coding: utf8

import socket
import os

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, _sock=None)

ip_port = ('127.0.0.1', 9999)
client.connect(ip_port)
while True:
    data = client.recv(1024)
    print 'server:', data
    inp = raw_input('client:')
    client.send(inp)
    if inp == 'exit':
        client.close()
        os._exit(1)
