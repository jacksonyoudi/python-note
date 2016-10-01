#!/usr/bin/env python
# coding: utf8

import paramiko

# 定义参数
username = "root"
hostname = "********"
port = ****
password = "******"

try:
    # 创建SFTPclient连接
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    # 上传文件
    localpath = "/root/flask/hello.py"
    remotepath = "/tmp/hello.py"
    sftp.put(localpath=localpath, remotepath=remotepath)

    # 下载文件
    localpath = "/tmp/text1.txt"
    remotepath = "/root/CMDB.sql"
    sftp.get(remotepath=remotepath, localpath=localpath)

    # 创建目录
    sftp.mkdir("/root/paramiko1", 755)

    # 查看目录
    sftp.listdir("/root")

    # 文件重命名
    sftp.rename('/root/apps.sql', '/root/apps2.sql')

    # 查看文件状态
    sftp.stat('/root/apps2.sql')

    sftp.close()
    t.close()
except Exception, e:
    print str(e)
