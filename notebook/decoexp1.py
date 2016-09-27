#!/usr/bin/env python
# coding: utf8

def pans(f):
    def _f(*args, **kwargs):
        print "裤子"
        return f(*args, **kwargs)
    return _f

def shirt(f):
    def _f(*args, **kwargs):
        print "T恤"
        return f(*args, **kwargs)
    return _f

def cap(f):
    def _f(*args, **kwargs):
        print "帽子"
        return f(*args, **kwargs)
    return _f

def shoes(f):
    def _f(*args, **kwargs):
        print "鞋子"
        return f(*args, **kwargs)
    return _f

def shoes1(f):
    def _f(*args, **kwargs):
        print "皮鞋"
        return f(*args, **kwargs)
    return _f

def person(name):
    print "装扮好的",name

def wearperson(person,cloth):
    w = person
    for i in cloth:
        w = i(w)
    return w



if __name__ == '__main__':
    # person("小明")
    # perdson("小红")
    cloth1 = [pans,shirt,cap]
    cloth2 = [shoes1,shirt]

    wearperson(person("明"),cloth1)
    wearperson(person("红"),cloth2)