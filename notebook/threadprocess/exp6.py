#!/usr/bin/env python
# coding: utf8

import threading
import time

counter = 0


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global counter
        time.sleep(2)
        counter += 1
        print 'I am %s,Set counter:%s' % (self.name, counter)


if __name__ == '__main__':
    a = []
    for i in xrange(0, 100):
        my_thread = MyThread()
        a.append(my_thread)
    for i in a:
        i.start()

