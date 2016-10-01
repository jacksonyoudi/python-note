#!/usr/bin/env python
# coding: utf8


import socket

sk = socket.socket()
ip_port = ('ip', port)
sk.bind(ip_port)
sk.listen(5)

while True:
    result = sk.accept()
    client = result[0]
    client_port = result[1]

    client, address = sk.accept()  # client是客户端的对象
    client.send()  # 向客户端发送数据

sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, _sock=None)
默认参数是TCP的
参数一：family, 地址簇
socket.AF_INET
socket.AF_INET6
socket.AF_UNSPEC

参数二： 类型
type
socket.SOCK_STREAM
socket.SOCK_DGRAM
socket.SOCK_RAW

方法：
sk.bind(ip_port)  # 绑定端口
sk.listen()  # 监听多少个
sk.accept()  # 接收请求，返回的是客户端对象和端口的元组

sk.connect()  # 连接服务器 ，
sk.connect_ex(adress),  # 同connect，但是会有返回值

sk.close()

conn.recv(buf)  # 接收数据，注意，是阻塞的，等待，buf，最多只能拿的数据缓存，最多8K

conn.send()  # 数据发送到缓存区，发送出去

sk.send()
sk.sendall(string[, flags])
sk.sendto(string, [flag])
sk.sendto(string, [flag], address)

sk.settimeout(timeout=timeout)
sk.getpeername()  # 返回套接字的远程地址，返回值是元组的(ipaddr,port)
sk.getsockname()  # 返回自己的地址，返回值是元组的(ipaddr,port)
sk.fileno()  # 套接字的文件描述符
socket只能处理一个客户端的连接

网络传递，IO不占用CPU

select
epoll

SocketServer

import SocketServer


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.request, self.client_address, self.server

import SocketServer


class MyServer(SocketServer.BaseRequestHandler):
    def handler(self):
        print self.request, self.client_address, self.server


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()


    server.server_address = ('127.0.0.1', 9999)
    server.RequestHandlerClass = MyServer
    server.serve_forever()

class BaseServer:
def __init__(self, server_address, RequestHandlerClass):
    """Constructor.  May be extended, do not override."""
    self.server_address = server_address
    self.RequestHandlerClass = RequestHandlerClass
    self.__is_shut_down = threading.Event()
    self.__shutdown_request = False


class TCPServer(BaseServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        BaseServer.__init__(self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)

class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass

ThreadingMixIn TCPServer

ThreadingTCPServer--->ThreadingMixIn,TCPServer--->BaseServer

self.server_address = server_address
self.RequestHandlerClass = RequestHandlerClass

类没有构造函数，就会调用父类的构造函数


def serve_forever(self, poll_interval=0.5):
    """Handle one request at a time until shutdown.

    Polls for shutdown every poll_interval seconds. Ignores
    self.timeout. If you need to do periodic tasks, do them in
    another thread.
    """
    self.__is_shut_down.clear()
    try:
        while not self.__shutdown_request:
            # XXX: Consider using another file descriptor or
            # connecting to the socket to wake this up instead of
            # polling. Polling reduces our responsiveness to a
            # shutdown request and wastes cpu at all other times.
            r, w, e = _eintr_retry(select.select, [self], [], [],
                                   poll_interval)
            if self in r:
                self._handle_request_noblock()
    finally:
        self.__shutdown_request = False
        self.__is_shut_down.set()


异步 +  多线程


提示：

class  MyServer(SocketServer.ThreadingTCPServer):
    def handle_request(self):

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass


结果：

print self.client_address
print self.request
print self.server

('127.0.0.1', 46621)
<socket._socketobject object at 0x7f3fc99e8520>
<SocketServer.ThreadingTCPServer instance at 0x7f3fc9989dd0>


socket传文件

recvfrom() 最大接收的大小

注意：传送的文件名，文件大小。
# !/usr/bin/env python
# coding:utf-8

import SocketServer
import os


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'G:/temp'
        conn = self.request
        print 'connected...'
        while True:
            pre_data = conn.recv(1024)
            # 获取请求方法、文件名、文件大小
            cmd, file_name, file_size = pre_data.split('|')
            # 已经接收文件的大小
            recv_size = 0
            # 上传文件路径拼接
            file_dir = os.path.join(base_path, file_name)
            f = file(file_dir, 'wb')
            Flag = True
            while Flag:
                # 未上传完毕，
                if int(file_size) > recv_size:
                    # 最多接收1024，可能接收的小于1024
                    data = conn.recv(1024)
                    recv_size += len(data)
                # 上传完毕，则退出循环
                else:
                    recv_size = 0
                    Flag = False
                # 写入文件
                f.write(data)
            print 'upload successed.'
            f.close()


instance = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
instance.serve_forever()

# !/usr/bin/env python
# coding:utf-8


import socket
import sys
import os

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)

container = {'key': '', 'data': ''}
while True:
    input = raw_input('path:')  # 输入路径
    cmd, path = input.split('|')  # 命令，路径
    file_name = os.path.basename(path) # 文件名
    file_size = os.stat(path).st_size # 文件大小
    sk.send(cmd + "|" + file_name + '|' + str(file_size))  # 将方法|文件名|大小
    send_size = 0 # 发送大小为0
    f = file(path, 'rb') # 读写文件
    Flag = True
    while Flag:
        if send_size + 1024 > file_size: # 是否发送完了
            data = f.read(file_size - send_size) # 最后一次读取
            Flag = False
        else:
            data = f.read(1024)  # 读取1024
            send_size += 1024   # 发送计算+1024
        sk.send(data) # 发送数据
    f.close()

sk.close()



面向对象
断言
python mysql
三层架构
socket

对事物的分类，
类就是模板
字段，方法，@property
公有，私有

__init__()  :实例化
__call__()  :


class Foo(object):
    def __init__(self):
        print "init"

    def __call__(self):
        return "call"


foo = Foo()
foo()  实例可调用

classmethod:


断言：
assert

socket
SocketServer



