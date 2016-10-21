#!/usr/bin/env python
# coding: utf8

class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        '''Return the next element.'''
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        '''Return the iterator itself.'''
        return self
