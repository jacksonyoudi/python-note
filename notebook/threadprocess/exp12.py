# coding: utf8

# 创建函数并将其作为单个进程
import multiprocessing
import time


def worker(interval):
    n = 5
    while n > 0:
        print 'the time is {0}'.format(time.ctime())
        time.sleep(interval)
        n -= 1


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))  # 实例化多进程对象，传递函数
    p.start()
    print 'p.pid:', p.pid
    print 'p.name:', p.name
    print 'p.is_alive:', p.is_alive()
