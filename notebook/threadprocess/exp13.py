# coding: utf8
# 创建函数并将其作为多个进程

import multiprocessing
import time


def work_1(interval):
    print 'work_1 starting....'
    time.sleep(interval)
    print 'work_1 ending.....'


def work_2(interval):
    print 'work_2 starting....'
    time.sleep(interval)
    print 'work_2 ending.....'


def work_3(interval):
    print 'work_3 starting....'
    time.sleep(interval)
    print 'work_3 ending.....'


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work_1, name='work_01', args=(2,))
    p2 = multiprocessing.Process(target=work_2, name='work_02', args=(3,))
    p3 = multiprocessing.Process(target=work_3, name='work_03', args=(4,))

    p1.start()
    p2.start()
    p3.start()

    print "The number of CPU is:" + str(multiprocessing.cpu_count())
    for p in multiprocessing.active_children():
        print "child   p.name:" + p.name + "\tp.id" + str(p.pid)
    print "END!!!!!!!!!!!!!!!!!"
