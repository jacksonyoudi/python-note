我们已经见过了使用subprocess包来创建子进程，但这个包有两个很大的局限性：
1) 我们总是让subprocess运行外部的程序，而不是运行一个Python脚本内部编写的函数。
2) 进程间只通过管道进行文本交流。以上限制了我们将subprocess包应用到更广泛的多进程任务。
(这样的比较实际是不公平的，因为subprocessing本身就是设计成为一个shell，而不是一个多进程管理包)

multiprocessing包是Python中的多进程管理包。
与threading.Thread类似，它可以利用multiprocessing.Process对象来创建一个进程。
该进程可以运行在Python程序内部编写的函数。
该Process对象与Thread对象的用法相同，也有start(), run(), join()
的方法。
此外multiprocessing包中也有Lock / Event / Semaphore / Condition类
(这些对象可以像多线程那样，通过参数传递给各个进程)，用以同步进程，其用法与threading包中的同名类一致。
所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。

但在使用这些共享API的时候，我们要注意以下几点:
在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。所以，有必要对每个Process对象调用join()
方法
(实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。

multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue，
避免使用Lock / Event / Semaphore / Condition等同步方式(因为它们占据的不是用户进程的资源)。

多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。
在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源。
但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率。

Process.PID中保存有PID，如果进程还没有start()，则PID为None。


python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。
Python提供了非常好用的多进程包multiprocessing，只需要定义一个函数，Python会完成其他所有事情。借助这个包，可以轻松完成从单进程到并发执行的转换。
multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。

1.
Process
from multiprocessing import Process

a = Process()


def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
    pass


方法：
is_alive()
join([timeout])
run()
start()
terinate()

属性：
authkey, deamon(需要通过start()
设置)，exitcode(进程在运行时，如果为 - N, 表示信号N结束)，name，pid，ppid
其中deamon是父进程终止

提示：
因子进程设置了daemon属性，主进程结束，它们就随着结束了。

当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。

import multiprocessing

a = multiprocessing.Lock()
a.acquire()
statement
a.release()

Rlock可以重入
multiprocessing.RLock

Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。
Semaphore
信号量

a = multiprocessing.Semaphore(5)
a.acquire()
statement
a.release()


Event
Event用来实现进程间同步通信。
a = multiprocessing.Event

a.is_set() # True或者 False
a.set()
a.wait()  #  在is_set()为True的时候才会运行

Queue
Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。
如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。
如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。

b = multiprocessing.Queue()
b.put()
def put(self, obj, block=True, timeout=None):
    pass

get方法可以从队列读取并且删除一个元素。
同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。
如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常。
b.get()
def get(self, block=True, timeout=None):
    pass
方法：

'_writer',
'cancel_join_thread',
'close',
'empty',
'full',
'get',
'get_nowait',
'join_thread',
'put',
'put_nowait',
'qsize'

b.qsize()
b.empty()
b.close()
b.get()
b.put()



pipe:
Pipe方法返回(conn1, conn2)代表一个管道的两个端。
Pipe方法有duplex参数，如果duplex参数为True(默认值)，那么这个管道是全双工模式
也就是说conn1和conn2均可收发。duplex为False，conn1只负责接受消息，conn2只负责发送消息。
p = multiprocessing.Pipe()
p.sent()
p.recv()





Pool:
在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，并行操作可以节约大量的时间。
当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥进程池的功效。
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求
但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。


