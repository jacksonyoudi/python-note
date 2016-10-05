#!/usr/bin/env python
# coding: utf8

import select
import socket
import sys
import Queue

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.setblocking(0)  # 其他客户端是可以连接的

server_address = ('localhost', 1000)
server.bind(server_address)

server.listen(5)

