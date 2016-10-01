#!/usr/bin/env python
# coding: utf8

import socket


def handler_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 Ok\r\n\r\n")
    client.send("Hello,World")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 80))
    sock.listen(5)

    while True:
        connection, address = sock.accept()  # connect 代表客户端，address，地址
        print connection, address
        handler_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
