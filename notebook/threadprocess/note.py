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


treading的模块：
Thread线程类，这是我们用的最多的一个类，你可以指定线程函数执行或者继承它都是可以实现子线程功能。
Timer与Thread类似，但是要等一段时间才开始执行。
Lock锁原语，竞态时使用
Rlock可重入锁，使单线程可以再次获得已获得的锁。
Condition条件变量，能让一个线程停下来，等待其他线程满足条件
Event：通用的条件变量。多线程可以等待某个事件发生，在事件发生后，所有的线程都被激活。
Semaphore为等待锁的线程提供一个类似'等候室'的结构。
BoundedSemaphore与Semaphore类似，但是不允许超过初始值
Queue：实现多生成者(produrcer),多消费者（Consumer)的队列，支持锁原语，能够在多个线程之间提供很好的同步支持。


Thread类
是你主要的线程类，可以创建进程实例，该类提供的函数包括：
getName()
isAlive()
isDeamon()
join(self,timeout=None)
run() 定义线程的功能函数
setDeamon(self,daemonic)
setName(self,name)
start()

Thread的主要方法：


setName设置线程的名字，默认是 Thread-1
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setName('new'+ self.name)

join()方法
join方法是用来阻塞当前的上下文，直到该线程运行结束。
def join(self,timeout=None)

setDaemon()方法
当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程就兵分两路。
当主线程完成想要退出，会检验子线程是否完成。如果子线程未完成，则子线程会等待线程完成后再退出。但是有时候
有时候，只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时可以用setDeamon方法，并设置参数为True。


使用Lock互斥锁

python编程中引入对象互斥锁的概念，来保证共享数据操作的完整性。每个对象都应该对于一个
可称为"互斥锁"的标记，这个标记用来保证任意时刻，只能有一个线程访问该对象。
在python中我们使用threading模块的Lock类。
mutex = threading.Lock() #实例化锁对象
mutex.acquire()  #获取锁对象
mutex.release()  #释放锁对象

同步阻塞
当一个线程调用Lock对象的acquire()方法获得锁使，这把锁就进入'locked'状态。因为每次只有一个线程1可以获得锁，所以如果此时另一个线程2
视图获得这个锁，该线程2就会变为'block'同步阻塞状态。直到拥有锁的线程1调用锁的release()方法释放锁之后，该锁进入'unlocked'状态。
线程调度程序从处于同步阻塞状态中选择一个来获得锁，并使得该线程进行运行'running'状态。

进一步考虑：
通过对公共资源使用互斥锁，这样就简单的达到我们的目的，但是如果我们遇到下面情况：
1.遇到锁嵌套的情况该怎么办，这个嵌套是指当我一个线程在获取临界资源时，又需要再次获取；
2、如果有多个公共资源，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源；

上述这两种情况会直接造成程序挂起，造成死锁。可使用可重入锁Rlock

死锁的形成：
死锁概念
所谓死锁： 是指两个或两个以上的进程在执行过程中，因争夺资源而造成的一种互相等待的现象，
若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程。
由于资源占用是互斥的，当某个进程提出申请资源后，使得有关进程在无外力协助下，永远分配不到必需的资源而无法继续运行，这就产生了一种特殊现象死锁。

避免死锁
避免死锁主要方法就是：正确有序的分配资源，避免死锁算法中最有代表性的算法是Dijkstra E.W 于1968年提出的银行家算法


可重入锁RLock

之后就直接挂起了，这种情况形成了最简单的死锁。
那有没有一种情况可以在某一个线程使用互斥锁访问某一个竞争资源时，可以再次获取呢？
在Python中为了支持在同一线程中多次请求同一资源，python提供了“可重入锁”：threading.RLock。这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，
其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁


使用Condition实现复杂同步
Python提供的Condition对象提供了对复杂线程同步问题的支持。
Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。

使用Condition的主要方式为：
线程首先acquire一个条件变量，然后判断一些条件。如果条件不满足则wait；
如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。
不断的重复这一过程，从而解决复杂的同步问题。

另外：Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock；
除了notify方法外，Condition对象还提供了notifyAll方法，可以通知waiting池中的所有线程尝试acquire内部锁。
由于上述机制，处于waiting状态的线程只能通过notify方法唤醒，所以notifyAll的作用在于防止有线程永远处于沉默状态。

使用Event实现线程间通信

使用threading.Event可以使一个线程等待其他线程的通知，我们把这个event传递到线程对象中，Event默认内置
一个标志，初始值为Flase。一旦该线程通过wait()方法进入等待状态，知道另一个线程调用该Event的set方法将内置标志设置为Ture时，
该Event会通知等待状态的线程回复运行。

