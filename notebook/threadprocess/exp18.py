# coding: utf8
# Event用来实现进程间同步通信。

import multiprocessing
import time


def wait_for_event(e):
    print 'wait_for_event:starting.....'
    e.wait()  # 设置Event进入 wait状态，直到等到  a.set()
    print 'wait_for_event: e.is_set()-->', str(e.is_set()) # is_set() 的Event的状态


def wait_for_event_timeout(e, t):
    print 'wait_for_event_timeout:starting...'
    e.wait(t) # 设置Event进入等待
    print 'wait_for_eventtimeout:e.is_set()', str(e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(target=wait_for_event, name='block', args=(e,))
    w2 = multiprocessing.Process(target=wait_for_event_timeout, name='non-block', args=(e, 2))
    w1.start()
    w2.start()

    time.sleep(3)

    e.set()  # 设置is_set()为Ture，通知其他wait()状态下的进程开始运行。
    print 'main: event is set'
