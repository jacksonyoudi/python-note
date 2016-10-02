线程和进程

一个程序可有多个进程
一个进程有多个线程

应用程序是工厂
车间是进程
工人是线程

CPU

时钟分片
滴答，抢占

import threading, thread

threading和thread功能相同，但是，threading的更高级，守护线程。


线程：
主线程

线程的数量没有限制，但是线程数太多，其性能会下降。
上下文切换造成资源浪费。

threading.Thread()

print 'before'
t1 = Thread(target=Foo, args=(1,))  # 将函数和线程进行绑定
t1.start()  # 线程执行
print t1.getName()

t2 = Thread(target=Foo, args=(1,))  # 将函数和线程进行绑定
t2.start()  # 线程执行
print t2.getName()


def getName(self):
    return self.name


@property
def name(self):
    assert self.__initialized, "Thread.__init__() not called"
    return self.__name


self.__name = str(name or _newname())


class Thread(_verbose):


    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):


def _newname(template="Thread-%d"):
    return template % _counter()


threading.Thread模块
start
getName()
setName()
IsDaemon()
Join(timeout)
run()

主线程一直按顺序执行, 运到创建子线程，创建并运行，不会去等待，一直向下执行。
子线程

print 'before'
t1 = Thread(target=Foo, args=(1,))  # 将函数和线程进行绑定
t1.setDeamon(True)
t1.start()  # 线程执行
print t1.getName()

print "---------------"
t2 = Thread(target=Foo, args=(2,))  # 将函数和线程进行绑定
t2.start()  # 线程执行
print t2.getName()

print 'after'

输出：
root @ VM - 166 - 182 - ubuntu:~ / python / notebook / threadprocess  # python exp1.py
before
Thread - 1
---------------
Thread - 2
after
1
2



Thread.setDeamon(True)
当主进程执行完以后，线程就会退出，如果，主进程没有执行结束，线程还会继续执行。
另外，默认是False，是会继续执行的


Thread.join(timeout)
等待当前线程执行结束才会执行后续的进程。
timeout，最多等待多长时间

Thread.run()


自定义run,通过target进行绑定


#!/usr/bin/env python
# coding: utf8

from threading import Thread

class MyThread(Thread):
    def run(self):
        print 'I am threading'


def bar():
    print 'bar'

t1 = MyThread(target=bar)
t1.start()
print 'over'



self.__target = target


def run(self):
    """Method representing the thread's activity.

    You may override this method in a subclass. The standard run() method
    invokes the callable object passed to the object's constructor as the
    target argument, if any, with sequential and keyword arguments taken
    from the args and kwargs arguments, respectively.

    """
    try:
        if self.__target:
            self.__target(*self.__args, **self.__kwargs)
    finally:
        # Avoid a refcycle if the thread is running a function with
        # an argument that has a member that points to the thread.
        del self.__target, self.__args, self.__kwargs


#!/usr/bin/env python
# coding: utf8

from threading import Thread


class MyThread(Thread):
    def run(self):
        print 'I am threading'
        Thread.run(self)


def bar():
    print 'bar'


t1 = MyThread(target=bar)
t1.start()
print 'over'


生产者，消费者

生产者---->容器(阈值)<-----消费者

线程安全
    资源挣用，引入锁机制，队列

队列，先进先出
堆栈,后进先出（弹夹）

from Queue import Queue

que = Queue(maxsize=100)
que.put(data)
que.empty() # 是否为空
que.qsize()
que.get()


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


线程和进程的区别
线程共享内存
进程不能共享内存

线程是更小的单元

线程安全：
    资源争用
python需要自己控制
加锁

在函数中不能直接修改全局变量

num = 0
def run(n):
    global num
    num += 1
    print num



死锁

#!/usr/bin/env python
# coding: utf8

import threading
import time

num = 0
num1 = 2

def run(n):
    time.sleep(1)
    lock.acquire()  # 加锁，独占CPU
    global num
    num += 1
    lock.acquire  # 锁竞争
    num1 += 1
    lock.release
    lock.release()
    time.sleep(0.01)  # 默认执行100条CPU指令
    print '%s\n' % num


lock = threading.Lock()

for i in range(100):
    t = threading.Thread(target=run, args=(i,))
    t.start()

解决方法：
使用Rlock()
允许自己调用多次锁




线程安全

lock
Rlock
samph
event


生产者消费者模型
解耦
支持并发
支持忙闲不均


paramiko



多进程
paramiko
审计开发
select异步模型

多进程解决GIL的问题
充分利用多核的优势

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print p.map(f,[1,2,3])




from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name',__name__
    if hasattr(os,'getppid'):
        print 'parent process:',os.getpid
    print 'process id:',os.getppid()

def f(name):
    info('function f')
    print 'hello',name

if __name__ == '__main__':
    info('main line')
    print '--------------'
    p = Process(target=info,args=(''))
    p.start()
    p.join()



import os

os.getpid()
os.getppid()
