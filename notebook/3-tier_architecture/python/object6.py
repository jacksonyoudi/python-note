#!/usr/bin/env python
# coding: utf8

class PositiveNum(object):
    def __init__(self, value):
        self.val = value

    def __get__(self, instance, owner):
        # instance = a, b
        owner = self.val
        print "__get__", instance, owner
        return self.val

    def __set__(self, instance, value):
        # instance = a, b
        print "__set__", instance, value
        try:
            assert int(value) > 0
            self.val = value
        except AssertionError:
            print "Error:" + str(value) + "is not positiveNum"
        except:
            print "ERROR:" + str(value) + "is not number"

    def __delete__(self, instance):
        print "__delete__", instance
        self.val = None

    def __getattr__(self, name):
        print self, name


class Car(object):
    country = u'中国'
    length = PositiveNum(0)
    width = PositiveNum(0)
    height = PositiveNum(0)

    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')
    b = Car(2.2, 3.4, 4.5, u'李四')
