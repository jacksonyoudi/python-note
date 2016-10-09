并行编程

并行和并发

分而治之
mapreduce
将任务划分为可并行的多个子任务，每个任务完成后合并得到结果。

map：映射，划分任务，分配到不同的任务
reduce：合并，折叠

流水：
将任务划分串行的多个子任务，每个子任务并行productConsume。

为什么要用，为什么难用？
多核，云计算，使得实现并行编程的条件更容易满足。
大数据，机器学习，高并发，使得并行编程很必要。

任务分割，共享数据的访问，死锁，互斥，信号量，利用管道，队列通行，线程，进程的管理。

站在巨人的肩膀，使用比较成熟的库。
Threading,实现多线程
Multiprocess，实现多进程

Parallelpython，可实现分布式计算，同事解决CPU和网络资源受限问题。

celery+rabbitMQ/redis,可实现分布式任务队列
Django和celery搭配可实现异步任务队列

Gevent，可实现高效的异步IO，协程

协程：用单线程实现多线程的功能。


进程和线程

cpu同一时刻只能调度一个进程
进程之间Mem独立
进程内线程共享Men

cpu在不同进程之间上下文切换。

线程在同一个进程中，做不同事件。

进程之间的通信：IPC,队列，管道，套接字

进程中一定有一个主线程，线程共享内存，通过锁机制进行控制竞态

进程之间通信
线程之间同步


并行编程--计算密集型任务

def countdown(n):
    while n>0:
        n-=1
count = 10000000

from threading import Thread
from multiprocessing import Process
实例化
a = Thread(target=countdown,args=(n,))

开始运行
a.start()

等待结束
a.join()

print "a is end"


