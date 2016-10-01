#!/usr/bin/env python
# coding: utf8

from threading import Thread
import time

def Foo(arg):
    for i in range(arg):
        print i
        time.sleep(1)


print 'before'
t1 = Thread(target=Foo, args=(8,))  # 将函数和线程进行绑定
t1.start()  # 线程执行
print t1.getName()
print t1.isDaemon()

t1.join()

# print "---------------"
# t2 = Thread(target=Foo, args=(2,))  # 将函数和线程进行绑定
# t2.start()  # 线程执行
# print t2.getName()

print 'after'
