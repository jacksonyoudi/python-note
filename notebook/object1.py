#!/usr.bin/env python
# conding: utf8

class A:
    # classic class
    '''
    this is class A
    '''
    pass
    __slots__ = ('x', 'y')

    def test(self):
        '''this is A.test()'''
        print "A class"


class B(object):
    # new class
    '''this is class B'''

    __slots__ = ('x', 'y')

    def test(self):
        # new class test
        '''this is B.test()'''
        print 'B class'


if __name__ == '__main__':
    a = A()
    b = B()
    print dir(a)
    print dir(b)
