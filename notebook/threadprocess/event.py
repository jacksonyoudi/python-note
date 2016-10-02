#!/usr/bin/env python
# coding: utf8

import threading
import time


def producer():
    print 'A:等人来买包子'
    event.wait()
    event.clear()
    print 'somebody coming.....'
    print 'making a baozi for someone.....'
    time.sleep(3)
    event.set()


def consumer():
    print 'B:去买包子'
    event.set()

    time.sleep(2)
    print "waiting for baozi to be read"
    event.wait()

    if event.isSet():
        pass


event = threading.Event()

p = threading.Thread(target=producer)
p.start()

c = threading.Thread(target=consumer)
c.start()
