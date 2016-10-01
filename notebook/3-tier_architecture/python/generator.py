生成器
generator
生成器和yield

Iterable, Iterator, Generator

iterable
包含Iterator, 可迭代的包含迭代器，但是不是所有的可迭代的都是迭代器

什么是可迭代的？iterable
list，dict

generator是生成一个迭代器的东西。
迭代器是一个对象，生成器是一个函数，（工厂函数）

如何把函数变成生成器，就是通过yield语句。
表达式变成生成器，通过()
解析式

range()
xrange()


避免每次执行都要调用，并返回
def fib_opt(n):
    a, b, i = 0, 1, 0
    while i <= n:
        a, b = b, a + b
        i += 1
    else:
        return a


print [fib_opt(i) for i in range(100)]

def fib_iter():
    a,b = 0,1
    while Ture:
        yield b
        a,b = b,a+b


yield 和 return 差不多，但是yield会保存以前执行的结果，只能向后计算。

a = fib_iter()
print [A.next() for i in xrange(10000)]

惰性计算


send用法

def func():
    input = []
    while Ture:
        a = (yield)
        # statement
        input.apppend(a)

可以再函数中保存变量，每次只执行一次，

itertools产生迭代器

horses= [1,2,3,4,5]
races = itertools.permutations(horses)  # 一个对象
返回所有组合

A = itertools.product([1,2],[3,4])
组合

B = itertools.repeat([1,2],4)

C = itertools.chain(races,B,C)  # 将迭代器连接起来
