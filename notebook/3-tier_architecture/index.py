#!/usr/bin/env python
# coding: utf8
from model.admin import Admin


def main():
    user = raw_input('username:')
    pwd = raw_input('password:')
    admin = Admin()
    result = admin.checkvalidate(user, pwd)
    if not result:
        print ' 用户名或密码错误'
    else：
        print '进入管理界面'




