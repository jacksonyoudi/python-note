import threading
import time

condition = threading.Condition()  #实例化 Condition对象
products = 0


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products
        while True:
            if condition.acquire():  # 获取condition条件
                if products < 10:  # 条件
                    products += 1;  # 改变条件
                    print "Producer(%s):deliver one, now products:%s" % (self.name, products)
                    condition.notify()  # 通知其他线程，其中wait()的线程开始重新判断线程
                else:
                    print "Producer(%s):already 10, stop deliver, now products:%s" % (self.name, products)
                    condition.wait();  # 线程等待
                condition.release()  # 释放condition
                time.sleep(2)


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print "Consumer(%s):consume one, now products:%s" % (self.name, products)
                    condition.notify()
                else:
                    print "Consumer(%s):only 1, stop consume, products:%s" % (self.name, products)
                    condition.wait();
                condition.release()
                time.sleep(2)


if __name__ == "__main__":
    for p in range(0, 2):
        p = Producer()
        p.start()

    for c in range(0, 10):
        c = Consumer()
        c.start()
