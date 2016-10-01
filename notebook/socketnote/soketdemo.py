#!/usr/bin/env python
# coding: utf8

import socket

sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, _sock=None)
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn, address = sk.accept()  # 客户端对象和客户端的端口,阻塞
    conn.send('hello')
    flag = True
    while flag:
        data = conn.recv(1024)  # 阻塞
        print 'client:', data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()

sk.close()
