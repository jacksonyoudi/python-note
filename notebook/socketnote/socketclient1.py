#!/usr/bin/env python
# coding: utf8

import socket
import os

# 服务器
sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 9999)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn, addr = sk.accept()   # 阻塞
    conn.recv(1024)
    flag = True
    while flag:
        data = conn.recv(1024)  # 阻塞
        print data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()


# 客户端

so = socket.socket()
so.connect(ip_port)
flag = True
while flag:
    dat = so.recv(1024)
    pritn dat
    if dat == 'exit':
        flag = False
    so.send('hello')

so.close()



import SocketServer

class Myserver(SocketServer.BaseRequestHandler):
    def handle(self):
        con = self.request
        addr = self.client_address
        con.recv()
        conn.send()
        

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer((ip_port),Myserver)
    server.serve_forever()