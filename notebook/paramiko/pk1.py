#!/usr/bin/env python
# coding: utf8

import paramiko

hostname = '*****'
username = '*****'
password = '****'
paramiko.util.log_to_file('syslogin.log')  # 发送paramiko日志到syslogin.log文件

ssh = paramiko.SSHClient()  # 创建一个ssh客户端client
ssh.load_system_host_keys()  # 获取客户端host_keys,默认保存在~/.ssh/known_hosts,非默认需要指定路径

ssh.connect(hostname=hostname, port=22, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
