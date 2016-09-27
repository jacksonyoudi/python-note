#!/usr/bin/env python
# coding: utf8


import pexpect

child = pexpect.spawn('scp ss.txt root@139.129.47.28:/tmp')
child.expect('password:')
child.sendline('*')
