#!/usr/bin/env python
# coding: utf8

import pexpect
import sys

child = pexpect.spawn('ssh root@139.129.47.28', logfile=True)
fout = file('mylog.txt', 'w')
# child.logfile = sys.stdout

child.expect('password:')
child.sendline('*')
child.expect('#')
child.sendline('ls /root')
child.expect('#')

fout.close()
