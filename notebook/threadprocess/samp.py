#!/usr/bin/env python
# coding: utf8

import threading
import time

num = 0
num1 = 1


def run(n):
    time.sleep(1)
    samp.acquire()  # 加锁，独占CPU
    time.sleep(0.01)
    global num
    num += 1
    samp.release()
    time.sleep(0.01)  # 默认执行100条CPU指令
    print '%s\n' % num


# lock = threading.RLock()  #定义递归锁
samp = threading.BoundedSemaphore(4)  # 信号量，锁多个人，mysql的最大连接数

for i in range(100):
    t = threading.Thread(target=run, args=(i,))
    t.start()
