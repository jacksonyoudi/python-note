python的数据结构概述
python数据结构中的栈
python数据结构中的队列

什么是数据结构？
数据结构实例
数据结构与算法的关系

什么是数据结构？
一个程序中必然会有数据存在，同样的一个或几个数据要组织起来，可以有不同的组织方式，也就是不同的存储方式。不同的
组织，也就是不同的存储方式。不同的组织方式就是不同的结构，我们把这些数据组织在一起的结构称之为数据的结构。
也叫数据结构。
数据结构：python的数据结构，list，tuple，

python的内置数据结构
元组，列表，字典

python的扩展数据结构：
栈，队列

python的内置数据结构
从数据的存储方式的角度分析

现在有三个物品, apple, orange, pear, 需要将这三个物品存储起来

存储方式一：这三个物品每个武平按顺序分别存储到一个柜子中，这些物品可以取出来，
[apple, orange, pear]

存储方式二：这三个物品按顺序分别存储到一个柜子中，这些物品不可以取出来，也不可以放新物品跟其挤在一个柜子，
（apple, orangle, pear）
元素不可以修改

存储方式：这三个物品不仅按顺序存储在一个柜子中，而且每个柜子害的有名字
{'sam', apple, 'jac':"orangle"}

数据结构就是数据的组织方式，就是数据存储的方式，也就是说，数据结构是静态的。算法是指运算方法，
通俗的说，算法就是思维。不同的运算方法，数据结构是算法的基础，相同的数据结构运用不同算法拥有不同的效率。



什么是栈？
栈的图示？
python中栈的实现

首先，栈是一种数据结构，栈相当于一端开口一端封闭的的容器。压栈，入栈，出栈
只能对栈顶的数据进行操作
栈指针

模拟：使用list

l = []

l.append()
l.pop()

l.insert(0, value)
l.pop(0)

栈的实现：

class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = 1

    def push(self, content):
        if self.Full():
            print "Stack is Full"
        else:
            self.stack.append(content)
            self.top = self.top + 1

    def pop(self):
        if self.Empty():
            print "Stack is Empty"
        else:
            self.stack.pop()
            self.top = self.top - 1

    def Full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.top == -1:
            return True
        else:
            return False


什么是队列？
图示

队列是两端都开的容器，但是一端只能进行删除操作, 一端只能进行插入的操作。插入是队尾，删除的是队首。数据的流向是单项的。

class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def Empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def Full(self):
        if self.tail - self.head + 1 == self.size:
            return True
        else:
            return False

    def enQueue(self, content):
        if self.Full():
            print "Queue is Full!"
        else:
            self.queue.append(content)
            self.tail = self.tail + 1
    def outQueue(self):
        if self.Empty():
            print "Queue is Empty!"
        else:
            self.head = self.head + 1
            self.pop(0)


python数据结构的的树

什么是树
树的图示
什么是二叉树？
二叉树的图示
python中的树的实现

树是一种非线性的数据结构，树具有非常高的层次性。
利用树来存储数据，能够使用公有元素进行存储，能够很大的程度上节约存储空间。
树的定义是首先有且只有一个根节点，其次他有N个不相交子集，每个子集为一棵子树。

二叉树：
二叉树是一种特殊的树，二叉树要么为空树，要么为左右两个不相交的子树组成。
二叉树是有序树，即使只有一个子树，也需要区分该子树是左子树还是右子树。
二叉树每个节点的度不能大于2，可以去0,1,2.二叉树的存储方式有二种，一种是顺序存储，
一种是链式存储。顺序存储中采用一维数组的存储方式，链式存储中，采用链表的存储反思，通常三部分：数据域，左孩子链域和右孩子链域。
链式：指针(链域)+ 数据（数据域）

树
树的基本构造
tree = [2,3,[58,6,[5]]]
print tree[0]
2
print tree[1]
3
print tree[2]
[58,6,[5]]
print tree[2][0]
58

二叉树的构造
比如要构造一个二叉树:
   7
8     9
  23    36
57  58

可以这样分析：
base=(-->8也就是jd2,--->9也就是jd3，base)
jd2=(no,--->23也就是jd4,8)
jd3=(no,--->36也就是jd5,9)
jd4=(-->57也就是jd6，-->58也就是jd7,23)
jd5=(no,no,36)
jd6=(no,no,57)
jd7=(no,no,58)
但是要注意，写的时候要到倒过来写。


class Tree():
    def __init__(self,leftjd=0,rightjd=0,data=0):
        self.leftjd = leftjd
        self.rightjd = rightjd
        self.data = data

class Btree():
    def __init__(self,base):
        self.base=base
    def empty(self):
        if self.base is 0:
            return True
        else:
            return False
    def quot(self,jd):
        '''
        前序遍历，NLR，根左右
        '''
        if jd==0:
            return
        print jd.data
        self.quot(jd.leftjd)
        self.quot(jd.rightjd)

    def mount(self,jd):
       '''中序遍历，LNR，左根右'''
       if jd==0:
           return
       self.mount(jd.leftjd)
       print jd.data
       self.mount(jd.rightjd)
    def hout(self,jd):
        '''后序遍历，LRN，左右根'''
        if jd==0:
            return
        self.hout(jd.leftjd)
        self.hout(jd.rightjd)
        print self.data


In [1]: jd1 = Tree(data=8)

In [2]: jd2=Tree(data=9)

In [3]: base=Tree(jd1,jd2,7)

In [4]: x=Btree(base)

In [13]: x.quot(x.base)
7
8
9
In [19]: x.hout(x.base)
8
9
7
In [23]: x.mount(x.base)
8
7
9

python中常见的数据结构链表
什么是链表
链表的图示
python中链表的实现


什么是链表？
首先，链表是一种数据结构。链表是一种非连续的，非顺序的数据存储方式。链表由一系列节点组成，每个节点包含两部分，
一部分是数据域，另一部分是指向下一节点的指针域。链表可以分为单向链表，单向循环链表，双向链表，双向循环链表。

# coding: utf8
class jd():
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist():
    def __init__(self, jd2):
        self.head = jd2
        self.head.next = None
        self.tail = self.head

    def add(self, jd2):
        self.tail.next = jd2
        self.tail = self.tail.next

    def view(self):
        jd2 = self.head
        linkstr = ''
        while jd2 is not None:
            if jd2.next is not None:
                linkstr = linkstr + str(jd2.data) + "--->"
            else:
                linkstr += str(jd2.data)
            jd2 = jd2.next
        print linkstr


In [1]: jd1 = jd(7)
In [3]: jd2 = jd('hello')

In [4]: jd3 = jd(8899)

In [5]: L
Linklist     LookupError

In [5]: x =  Linklist(jd1)

In [6]: x.add(jd3)

In [7]: x.add(jd2)

In [8]: x.view()
7--->8899--->hello


python中常见数据结构 bitmap
什么是bitmap
bitmap的图示
python中bitmap的实现，实现排序


什么是bitmap？
首先，bitmap也是一种数据结构，bit指的位，map指的是图，bitmap也叫位图。
这种数据结构的存储简单来说就是把原来的数，转化为二进制来存储，每个位占一个存储单元。
我们操作bitmap中的数据，也就是相当于操作一个位。bitmap数据结构的优点是可实现很好的排序。

数字的二进制的形式：
32位，31位符号位
5  00000000000000000000000000000000000000000101
这种类型的数据结构就叫做bitmap。

# coding: utf8
class Bitmap():
    def __init__(self, max):
        self.size = int((max + 31 - 1) / 31)
        self.array = [0 for i in range(self.size)]

    def bitIndex(self, num):
        return num % 31

    def set(self, num):
        elemIndex = num / 31
        byteIndex = self.bitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def test(self, i):
        elemIndex = x / 31
        byteIndex = self.bitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex)
            return True
        return False


python常见数据结构中的图
什么是图
图示

什么是图？
图是一种数据结构，图可以简单的理解为时一个关系网络，该网络中有N多节点，每个节点上存储着一个数据，
数据之间的关联我们可以用线把关联的节点连起来的方式表示。其中，有的数据关系是由方向的，比如数据A--->数据B
其关系只能从A到B，不能从B到A，如果数据之间的关系是由方向的，这个数据关系用弧线表示。有的数据关系是没有方向的，
A--B表示既可以A到B关联，也可以B到A关联，这种没有方向的关系用线段表示。

