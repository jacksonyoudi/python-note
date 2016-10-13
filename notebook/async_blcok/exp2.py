# coding: utf8
import time
def b(a):
    a()


def asynca(func):
    def f():
        time.sleep(5)
        print 'a'
    func(f)
    return 'b'

asynca(b)
