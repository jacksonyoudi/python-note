#!./usr/bin/env python
# coding: utf8

class A(object):
    def test(self):
        print "A's test"


class B(A):
    def test(self):
        print "B's test"
        A.test(self)


class C(A):
    def test(self):
        print "C's test"
        A.test(self)


class D(B, C):
    def test(self):
        print "D's test"
        B.test(self)
        C.test(self)


if __name__ == '__main__':
    a = D()
    a.test()



