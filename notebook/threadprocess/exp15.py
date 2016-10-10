# coding: utf8
# daemon程序对比结果

import multiprocessing
import time


def work(interval):
    print 'work start:{0}'.format(time.ctime())
    time.sleep(interval)
    print 'work end:{0}'.format(time.ctime())


if __name__ == '__main__':
    p = multiprocessing.Process(target=work, args=(3,))
    p.daemon = True
    p.start()
    p.join()
    print 'end'
