#!/usr/bin/env python
# coding: utf8

import threading

counterA = 0
counterB = 0
mutexA = threading.Lock()
mutexB = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        global mutexA, mutexB
        if mutexA.acquire():
            print 'I am %s,get res: %s' % (self.name, "ResA")

            if mutexB.acquire():
                print 'I am %s,get res: %s' % (self.name, "ResB")
                mutexB.release()
        mutexA.release()

    def fun2(self):
        global mutexA, mutexB
        if mutexB.acquire():
            print 'I am %s,get res: %s' % (self.name, "ResB")
            mutexB.acquire()

            if mutexA.acquire():
                print 'I am %s,get res: %s' % (self.name, "ResA")
                mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in xrange(0, 100):
        my_thread = MyThread()
        my_thread.start()
