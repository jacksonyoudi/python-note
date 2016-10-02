#!/usr/bin/env python
# coding: utf8

from multiprocessing import Process, Value, Array


def f(n, a, raw):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]
    raw.append(9999)
    print raw


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    raw_list = range(10)

    p = Process(target=f, args=(num, arr, raw_list))
    p.start()
    p.join()

    print num.value
    print arr[:]
    print raw_list
