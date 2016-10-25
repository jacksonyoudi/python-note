# coding: utf8
迭代器只不过是一个实现迭代协议的容器对象。它基于两个方法：

next  返回容器的下一个项目
__iter__  返回迭代器本身

迭代器可以通过使用一个iter内建函数和一个序列来创建。

i = iter('abc')
i.next()

当序列遍历完，会抛出一个StopIteration异常


生成器
基于yield指令，可以暂停一个函数并返回中结果。该函数将保存执行环境并且可以在必要时间恢复。


def  fibonacci():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a + b

函数将会返回一个特殊的迭代器，也就是generator对象，它知道如何保存执行环境。对它的调用是不确定的，每
次都产生序列中下一个元素。

生成器对降低程序复杂性也有帮助，并且能够提升基于多个序列的数据转换算法的性能。
把每个序列当做一个迭代器，然后将它们合并到一个高级的函数中，这是一个避免函数变的庞大、丑陋
、不可理解的好办法。而且，还可以给整个处理链提供实时的反馈。

def power(values):
    for value in values:
        print  'powering %s' % value
        yield value

def adder(values):
    for value in values:
        print 'adding to %s' % value
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

elements = [1,4,7,9,12,19]
res = adder(power(elements))

嵌套，多层的yield语句

res.next()


保持代码简单，而不是数据
拥有许多简单的处理序列的可迭代函数，要比一个复杂的每次计算一个值的函数更好一些。

python引入的与生成器相关的诸侯一个特性是提供了与next方法调用的代码进行交互的功能。yield将变成一个表达式
，而一个值可以通过名为send的新方法来传递。

def psychoologist():
    print 'Please tell me your problems'
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print ("Don't ask yourself too much questions")
            elif 'good' in answer:
                print  "A that's good, go on"
            elif 'bad' in answer:
                print "Don't be so negative"


协同程序
协同程序可以挂起、恢复，并且可以有多个进入点的函数。有些语言本身就提供这种特性。如Io和Lua，它们可以实现协同的多任务和管道机制。
例如，每个协程程序将消费或生产成数据，然后暂停，知道其他数据被传递。
在python中，协同程序的替代者是线程，他可以实现代码块之间的交互。但是因为它们表现出一种抢先式的风格，所以必须注意资源锁，而协同陈旭不需要。这样的代码可能变得相当
复杂，难以创建和调试。但是生成器几乎就是协同程序，添加send,throw和close,qi初始的意图就是为该语言提供一种类似协同程序的特性。


import multitask



