#!/usr/bin/env python
# coding: utf8

import threading
import time

counter = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global counter, mutex
        time.sleep(0.5)
        if mutex.acquire():
            counter += 1
            print 'I am %s,set count: %s' % (self.name, counter)
            mutex.release()


if __name__ == '__main__':
    a = []
    for i in xrange(0, 100):
        my_thread = MyThread()
        a.append(my_thread)
    for i in a:
        i.start()
