递归
函数调用


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


[fib(i) for i in range(100)]

fib1 = lambda n: i if n <= 2 else fib(n - 1) + fib(n - 2)


字符串取反

def str_rev(s):
    if len(s) <=1:
        return s
    else:
        return str_rev(s[1:])+s[0]

s = "ijakgnug"
print str_rev(s)


平方根的二分法：

