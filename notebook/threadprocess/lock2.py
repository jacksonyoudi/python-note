#!/usr/bin/env python
# coding: utf8

import threading
import time

num = 0


def run(n):
    time.sleep(1)
    lock.acquire()  # 加锁，独占CPU
    global num
    num += 1
    lock.release()
    time.sleep(0.01)  # 默认执行100条CPU指令
    print '%s\n' % num


lock = threading.Lock()

for i in range(100):
    t = threading.Thread(target=run, args=(i,))
    t.start()

