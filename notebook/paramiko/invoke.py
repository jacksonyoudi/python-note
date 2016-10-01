#!/usr/bin/env python
# coding: utf8

import paramiko
import os, sys, time

# 定义堡垒机的信息参数 阿里云
blip =
bluser =
blpassword =

# 定义业务服务器的信息参数， 亚马逊云

hostname =
username =
password =

port = 22

# 记录日志，以及密码提示
passinfo = "\'s password:"
paramiko.util.log_to_file('syslogin.log')

# 创建ssh连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpassword)

# 创建会话，开启命令调用
channel = ssh.invoke_shell()

# 会话命令执行超时时间，默认为秒
channel.settimeout(30)

buff = ''
resp = ''

# 执行ssh登录业务主机
channel.send('ssh  ' + username + '@' + '\n')

# ssh登录的提示信息判断，输出串尾含有"\s password: 时退出循环

while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception, e:
        print 'Error info:%s connect time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    # 输出尾部含有 yes/no时发送yes并回车
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''

channel.send(password + '\n')

buff = ''

# 输出串尾# 提示符是说明校验通过并退出while循环
while not buff.endswith('# '):
    resp = channel.recv(9999)
    # 输出尾部含有 \s password: 时说明密码不正确
    if not resp.find(passinfo) == -1:
        print 'Error info: Authentication failed.'
        # 关闭连接对象后退出
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp

# 认证通过后发送ifconfig 命令来查看结果
channel.send('ifconfig')
buff = ''

try:
    while buff.find('# ') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception, e:
    print "error info:" + str(e)

# 打印输出串
print buff
channel.close()
ssh.close()
