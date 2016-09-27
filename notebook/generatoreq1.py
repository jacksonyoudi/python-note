#!/usr/bin/env python
# coding: utf8

def a():
    i = 1
    while True:
        yield i
        i += 10

if __name__ == '__main__':
    b = a()
    for i in xrange(10):
        print b.next()
