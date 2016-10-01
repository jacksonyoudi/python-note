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

    def getOwner(self):
        return self.__owner

    def setOwner(self, value):
        self.__owner = value

    def getLength(self):
        return self._length

    def setLength(self, value):
        assert value > 0, "length must large than 0"
        self._length = value


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')
    print a.getOwner()

    # a.setLength(-1)

