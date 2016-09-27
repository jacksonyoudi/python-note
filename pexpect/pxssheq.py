#!/usr/bin/env python
# coding:utf8

import pxssh
import getpass

try:
    s = pxssh.pxssh()  # 创建pxssh对象 s
    hostname = raw_input("hostname:")
    username = raw_input("username:")
    password = getpass.getpass('please input password:')  # 接收密码输入
    s.login(hostname, username, password)  # 建立ssh连接
    s.sendline('uptime')  # 运行uptime命令
    s.prompt()  # 匹配系统提示符
    print s.before  # 打印出现系统提示符前的命令输出
    s.sendline('ls -l')
    s.prompt()
    print s.before
    s.sendline('df')
    s.prompt()
    print s.before
    s.logout()
except Exception, e:
    print "pxssh failed on login."
    print str(e)
