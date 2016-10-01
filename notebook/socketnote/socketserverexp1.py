#!/usr/bin/env python
# coding: utf8
import SocketServer


class Myserver(SocketServer.BaseRequestHandler):
    def handle(self):
        # print self.client_address
        # print self.request
        # print self.server
        conn = self.request
        conn.send('sb')
        flag = True
        while flag:
            data = conn.recv(1024)
            print data
            if data == 'exit':
                flag = False
            conn.send('sb')
        conn.close()


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), Myserver)
    server.address_family
    server.serve_forever()
