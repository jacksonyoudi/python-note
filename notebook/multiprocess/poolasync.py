#!/usr/bin/env python
# coding: utf8

from multiprocessing import Pool
import time


def f(x):
    print x * x
    time.sleep(1)
    return x * x


pool = Pool(processes=4)

res_list = []
for i in range(10):
    res = pool.apply_async(func=f, args=[i, ])  # 函数放入进程池
    # res = Process(target)
    res_list.append(res)
    # res.get()
    print '---------------', i

for i in res_list:
    print i.get()


# pool.apply()  同步的方式