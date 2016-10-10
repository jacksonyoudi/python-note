# coding: utf8
# 使用进程池（非阻塞）

import multiprocessing
import time


def func(msg):
    print 'msg:', msg
    time.sleep(3)
    print 'end'


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    for i in xrange(5):
        msg = 'hello %d' % i
        pool.apply_async(func, (msg,)) # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程去

    print 'Mark,Mark，Mark，Mark'

    pool.close()
    pool.join()  # 调用join()之前，先调用close(),否则会出错。执行完close()后不会有新的进程加入到pool,join()函数等待所有的子进程结束。
    print "Sub-process(es) done."