# coding: utf8
import time
def synca():
    def f():
        time.sleep(5)
        print 'a'
    return f()

synca()
