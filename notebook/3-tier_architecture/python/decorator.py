#!/usr/bin/env python
# conding: utf8

# 装饰器

设计模式：装饰模式，对一个函数或类进行装饰，在函数原有的功能的基础上进行添加功能。


装饰器-无嵌套
函数作为返回值

def decorator(f):
    print "before f() called"
    return f

def myfunc1():
    print  "myfunc1 called"

@decorator
def myfunc2()
    print "myfunc1 called"

if __name__ == "__main__":
    pass
    #decorator(myfunc1)()  直接调用
    #myfunc2()


提示： @function 在被导入的时候就会被运行的。最早执行的

问题1：如何避免在导入的运行？


import time
import random

def time_cost(f):
    start = time.clock()
    a=f()
    end = time.clock()
    print f.__name__,"run cost time is ",end-start
    return a  # 返回的是一个函数的执行结果

@time_cost
def list_comp():
    return [(x,y) for x in range(11000) for y in range(1000)]


if __name__ == "__main__":
    pass
    a = list_comp  # 返回的是一个值
    #a=time_cost(list_comp)


问题2：如何返回一个函数，又让装饰器对函数前后进行装饰?

问题3：函数有参数？如何装饰？

1@装饰器会提前执行（导入的时候执行）
2目标函数无法带参数
3目标函数调用后无法插入代码


装饰器-2层嵌套
函数带参数

def time_cost(f):  # 绑定外部变量的内部函数（外部变量是函数）
    def f(*args,**kwargs):
        start = time.clock()
        f(*args,**kwargs)
        end = time.clock()
        print end-start
    return f  # 闭包返回函数

@time_cost
def list_comp(length):
    return [(x,y) for x in range(length) for y in range(length) if x*y >25]


list_comp(1000)

解决：
@装饰器会提前执行
目标函数无法带参数
函数调用后无法插入代码



装饰器-3层嵌套
装饰器带参数


def time_cost(timef):

    def decorator(f):
        def _f(*args,**kwargs):
            start = timef()
            a = f(*arg,**kwargs)
            end = timef()
            print f.__name__,"run cost time is",end-start
            return a
        return _f

    return decorator


装饰器-装饰模式
设计模式

给小明穿衣服：
工作时穿工作服，西装，皮鞋，裤子
运动是穿运动服，T恤，运动鞋，裤子，帽子

把这种搭配做成套装可以直接给另一个人小红穿上

这种套装可以根据日期随意更换


