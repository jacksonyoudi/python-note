#!/usr/bin/env python
# coding: utf8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, singal):
        super(MyThread, self).__init__()
        self.singal = singal

    def run(self):
        print 'I am %s,I will sleep...' % self.name
        self.singal.wait()  # 进入等待状态，直到另一个线程调用Event的set()方法将内置标志设置为Ture，才会执行
        print 'I am %s,I awake....' % self.name


if __name__ == '__main__':
    singal = threading.Event()
    for t in range(0, 3):
        thread = MyThread(singal)
        thread.start()

        print 'main thread sleep 3 seconds'
        time.sleep(3)

        singal.set()  # 修改内置标志
