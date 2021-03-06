#!/usr/bin/env python
# coding: utf8

import threading
import time

num = 0
num1 = 1

def run(n):
    time.sleep(1)
    lock.acquire()  # 加锁，独占CPU
    global num
    num += 1
    lock.acquire()
    num1 += 1
    lock.release()
    lock.release()
    time.sleep(0.01)  # 默认执行100条CPU指令
    print '%s\n' % num


lock = threading.RLock()  #定义递归锁

for i in range(100):
    t = threading.Thread(target=run, args=(i,))
    t.start()