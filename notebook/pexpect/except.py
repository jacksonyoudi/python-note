#!/usr/bin/env python
# coding: utf8

import pexpect
import sys

child = pexpect.spawn('ssh root@remote')
fout = file('log.txt', 'w')
child.logfile = fout

child.expect('password:')
child.sendline('passwordstring')
print "before" + child.before
print "after" + child.after

child1 = pexpect.run('ssh root@remote', events={'password': password})
