#!/usr/bin/env python
# coding: utf8


from threading import Thread
from Queue import Queue
import time


class Procuder(Thread):
    def __init__(self, name, queue):
        '''
        @:param name: 生产者的名称
        @:param queue: 容器
        '''

        self.__Name = name
        self.__Queue = queue
        super(Procuder, self).__init__()

    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('baozi')
                time.sleep(1)
                print "%s 生产了一个包子" % (self.__Name,)
                # Thread.run(self)


class Consumer(Thread):
    def __init__(self, name, queue):
        '''
        @:param name: 生产者的名称
        @:param queue: 容器
        '''

        self.__Name = name
        self.__Queue = queue
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get()
                time.sleep(1)
                print "%s 消费了一个包子" % (self.__Name,)
                # self.__Queue.get('baozi')
                # Thread.run(self)


que = Queue(maxsize=100)  # 线程安全
xiong = Procuder('xiong', que)  # 线程
xiong.start()

xiong1 = Procuder('xiong1', que)  # 线程
xiong1.start()

xiong2 = Procuder('xiong2', que)  # 线程
xiong2.start()

for item in range(20):
    name = 'peng%d' % item
    temp = Consumer(name=name, queue=que)
    temp.start()

# print que.qsize()
# que.put('1')
# que.put('2')
# print que.qsize()
# print que.get()
# print que.qsize()
