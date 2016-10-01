#!/usr/bin/env python
# coding: utf8

class Car(object):
    country = u'中国'

    def __init__(self, length, width, height, owner=None):
        self.__owner = owner

        assert length > 0, "length mush larger than 0"
        self._length = length
        self._width = width
        self._height = height

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @owner.deleter
    def owner(self):
        self.__owner = None

    @property
    def length(self):
        return self._length

    @length.deleter
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        assert value > 0, "length must large than 0"
        self._length = value


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')
    print a.owner
    del a.owner
    print a.owner
    a.length = 3
    print a.length




