#!/usr/bin/env python
# coding: utf8

import threading
import time
import Queue
import random

def Producer(name, queue):
    while True:
        queue.put('baozi')
        print 'Made a baozi.....'
        time.sleep(random.randrange(5))


def Consumer(name, queue):
    while True:
        try:
            queue.get()
            queue.get_nowait()
        except Exception,e:
            print "没有包子"
        print 'Got a baozi....'
        time.sleep(random.randrange(3))


q = Queue.Queue()
p1 = threading.Thread(target=Producer, args=('youdi', q))
p2 = threading.Thread(target=Producer, args=('xiongwl', q))
p1.start()
p2.start()


c1 = threading.Thread(target=Consumer, args=('hahah', q))
c2 = threading.Thread(target=Consumer, args=('hui', q))
c1.start()
c2.start()