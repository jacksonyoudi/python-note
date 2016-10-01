#!/usr/bin/env python
# coding: utf8

import paramiko
import os

# 定义参数
hostname = "****"
username = "***"
port = 22

# 记录日志
paramiko.util.log_to_file('syslogin.log')

# 创建SSHClient
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
# 定义私钥存放路径
privatekey = os.path.expanduser('~/.ssh/id_rsa')

# 创建私钥对象key
key = paramiko.RSAKey.from_private_key_file(privatekey)

# ssh连接
ssh.connect(hostname=hostname, username=username, pkey=key)

# 输出结果
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()
