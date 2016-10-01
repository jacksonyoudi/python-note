#!/usr/bin/env python
# coding: utf8

import SocketServer
import os
class MyServer(SocketServer.BaseRequestHandler):
    def handler(self):
        conn = self.request
        base_path = '/tmp'
        print 'connnect.....'
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