#!/usr/bin/env python
# coding: utf8

class Car(object):
    country = u'中国'
    __slots__ = ('length', 'owner', 'height', '__dict__')

    def __init__(self, length, width, height, owner=None):
        self.__owner = owner

        assert length > 0, "length mush larger than 0"
        self._length = length
        self._width = width
        self._height = height

    def __getattr__(self, item):
        print "__getattr__", item
        assert item in self.__dict__, "Not have this attr"
        return self.__dict__.get(item, None)

    def __setattr__(self, key, value):
        print "__setattr__", key, value
        assert key in self.__dict__, "not have this attr"
        if key != 'owner':
            assert value > 0, name + "must large than 0"
        self.__dict__[key] = value

    def __delattr__(self, item):
        print "__delattr__", item
        assert item in self.__dict__, "Not have this attr"
        if item == 'owner':
            self.__dict__[item] = None


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')
