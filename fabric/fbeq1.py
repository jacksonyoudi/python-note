#!/usr/bin/env python
# coding: utf8

from fabric.api import *

env.user = 'root'
env.hosts = ['8888888', '*']
env.passwords = {
    'root@*': '*',
    'root@*': '*',
}


#  查看本地系统信息，当有多台主机时只运行一次
@runs_once
def local_task():
    local("uname -s")

def remote_task():
    with cd("/root/"):
        run("ls -l")