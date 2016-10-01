#!/usr/bin/env python
# coding: utf8

from threading import Thread


class MyThread(Thread):
    def run(self):
        print 'I am threading'
        Thread.run(self)


def bar():
    print 'bar'


t1 = MyThread(target=bar)
t1.start()
print 'over'
