#!/usr/bin/env python
# coding: utf8

import os

print 'Process %s start....' % os.getpid()
pid = os.fork()

if pid == 0:
    print 'i am child process %s and parent process %s' % (os.getpid(), os.getppid())
else:
    print 'i am %s just create a child process %s' %(os.getpid(),pid)
