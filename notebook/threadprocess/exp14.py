# coding: utf8
# 将进程定义为类

import multiprocessing
import time


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        super(ClockProcess, self).__init__()
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print 'the time is {0}'.format(time.ctime())
            time.sleep(self.interval)
            n -= 1


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    print 'pid:', p.pid, 'ppid:', p._parent_pid
