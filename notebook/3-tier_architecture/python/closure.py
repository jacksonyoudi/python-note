# 绑定外部变量的函数
def pow_x(x):
    def echo(value):
        return value ** x

    return echo


lst = [pow_x(2), pow_x(3), pow_x(4)]
for p in lst:
    print p(2)

闭包的特点：
1.
嵌套函数
2.
内部函数用到了外部变量
3.
外部函数返回内部函数

参数查找规则：LEGB（local, Extend,
global, base）





1.
内部函数不能“改变”外部变量
2.
内部函数用到了外部变量为list，则可以从外部或内部改变值，并且从外部或内部改变值，并且使外部没有引用也不会回收


def pow_y(x):
    def echo(value):
        x[0] = x[0] * 2  # 修改外部变量 E
        # x = [2, 2]   # 本地变量
        return value ** x[0], value ** x[1]  # 返回元组

    return echo


def largerx(x):
    def echo(value):
        return Ture if value > x[0] else False

    return echo


内部修改外部变量
def pow_y(x):
    def echo(value):
        x[0] = x[0] * 2  # 修改外部变量 E
        # x = [2, 2]   # 本地变量
        return value ** x[0], value ** x[1]  # 返回元组

    return echo

外部修改内部外部变量

x = [1,1]
lst2 = pow_y(x)

print lst2(2)
x = x * 2 # 外部修改外部变量
print lst2(2)
print lst2(3)
print lst2(4)



origin = [0,0]
legal_x = [0,50]
legal_y = [0,50]

def create(pos):
    def palyer(direction,step):
        new_x = pos[0] + direction[0] + step
        new_y = pos[1] + direction[1] + step
        pos[0] = new_x
        pos[1] = new_y

# 自己维护修改外部变量

player1 = create(origin[:])
print payer1()
