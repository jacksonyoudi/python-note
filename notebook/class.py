面向对象编程

基本语法
属性和封装
方法
继承和组合
多态
特殊方法
wxpython

类：
基本语法：

class class_name(base_class):
    class_var

    def methods(selfself, args):
        statements


类的变量，属性
实例的变量，属性


class A:
    pass


class B(object):
    pass


a = A()
b = B()

类实例化成对象

经典类和新式类
区别：
1
__slots__,
2
继承顺序，super
3
__new__
4
__getattribute__

经典类


class A:
    pass


新式类


class B(object):
    pass


__slots__:限定访问类的属性
继承属性：广度查找，深度查找

例子：
# !/usr.bin/env python
# conding: utf8

class A:
    # classic class
    '''
    this is class A
    '''
    pass

    def test(self):
        '''this is A.test()'''
        print "A class"


class B(object):
    # new class
    '''this is class B'''

    # __slots__ = ('x','y')
    def test(self):
        # new class test
        '''this is B.test()'''
        print 'B class'


if __name__ == '__main__':
    a = A()
    b = B()
    print dir(a)
    print dir(b)

输出：
['__doc__', '__module__', 'test']
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
 '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'test']
经典类和新式类的区别

自己添加属性
>> > a.x = 1
>> > a.x
1
>> > b.x = 2
>> > b.x
2
>> > b.__dict__
{'x': 2}
>> > a.__dict__
{'x': 1}

使用: __slots__ = ('x', 'y')
限制自定义属性


class A:
    # classic class
    '''
    this is class A
    '''
    pass
    __slots__ = ('x', 'y')

    def test(self):
        '''this is A.test()'''
        print "A class"


class B(object):
    # new class
    '''this is class B'''

    __slots__ = ('x', 'y')

    def test(self):
        # new class test
        '''this is B.test()'''
        print 'B class'


if __name__ == '__main__':
    a = A()
    b = B()
    print dir(a)
    print dir(b)

输出结果：
>> > a.x = 1
>> > a.y = 2
>> > a.z = 3
>> > a.d = 5
>> > a.__dict__
{'y': 2, 'x': 1, 'z': 3, 'd': 5}
>> > b.x = 1
>> > b.y = 2
>> > b.z = 3
Traceback(most
recent
call
last):
File
"<stdin>", line
1, in < module >
AttributeError: 'B'
object
has
no
attribute
'z'
dir(a)
dir(b)

由上述可知，__slots__
对经典类没有作用

help()
的使用
help(A)
Help
on


class A in module __main__:


class A
    | this is

    class A

        |
        | Methods
        defined
        here:
        |
        | test(self)
        | this is A.test()

    (END)

    help(B)
    Help
    on

    class B in module __main__:

    class B(__builtin__.object)
        | this is

        class B

            |
            | Methods
            defined
            here:
            |
            | test(self)
            | this is B.test()
            |
            | ----------------------------------------------------------------------
            | Data
            descriptors
            defined
            here:
            |
            | x
            |
            | y

        (END)

        其中
        x, y
        是由于__slots__的原因

        属性和封装

        实例和类的属性

        实例属性
        类属性
        描述符
        __init__

        实例属性：一般定义在__init__函数中
        类属性，在类中定义的变量，定义在方法之外的

        class Car(object):
            country = u'中国'  # 类属性

            def __init__(selfself, length, width, height, owner):
                self.owner = owner  # 实例属性
                self.length = length
                self.width = width
                self.height = height

        __init__是特殊方法，隐性的调用时机，如在实例化一个对象

        类属性和类属性的区别
        如果实例属性没有，就会查找类属性

        例子：
        # !/usr/bin/env python
        # coding: utf8

        class Car(object):
            country = u'中国'

            def __init__(self, length, width, height, owner=None):
                self.owner = owner
                self.length = length
                self.width = width
                self.height = height
                self.country = "China"

        if __name__ == '__main__':
            a = Car(1.2, 1.4, 1.5, u'张三')
            b = Car(2.2, 2.5, 2.5, u'李四')
            print a.owner, b.owner
            print a.country, b.country

            b.country = u'美国'

            print a.country, b.country
            print Car.country

            del a.country
            print a.country

        结果：
        张三
        李四
        China
        China
        China
        美国
        中国
        中国

        >> > a.__dict__
        {'owner': u'\u5f20\u4e09', 'width': 1.4, 'length': 1.2, 'height': 1.5}
        >> > b.__dict__
        {'owner': u'\u674e\u56db', 'width': 2.5, 'length': 2.2, 'country': u'\u7f8e\u56fd', 'height': 2.5}
        >> > a.__class__.__dict__
        dict_proxy({'__module__': '__main__', 'country': u'\u4e2d\u56fd', '__dict__': < attribute
        '__dict__'
        of
        'Car'
        objects >, '__weakref__': < attribute
        '__weakref__'
        of
        'Car'
        objects >, '__doc__': None, '__init__': < function
        __init__
        at
        0x7fa13a2e77d0 >})
        >> > Car.country = '中华人民共和国'
        >> > a.__class__.__dict__
        dict_proxy({'__module__': '__main__',
                    'country': '\xe4\xb8\xad\xe5\x8d\x8e\xe4\xba\xba\xe6\xb0\x91\xe5\x85\xb1\xe5\x92\x8c\xe5\x9b\xbd',
                    '__dict__': < attribute
        '__dict__'
        of
        'Car'
        objects >, '__weakref__': < attribute
        '__weakref__'
        of
        'Car'
        objects >, '__doc__': None, '__init__': < function
        __init__
        at
        0x7fa13a2e77d0 >})
        >> > a.country
        '\xe4\xb8\xad\xe5\x8d\x8e\xe4\xba\xba\xe6\xb0\x91\xe5\x85\xb1\xe5\x92\x8c\xe5\x9b\xbd'
        >> > b.country
        u'\u7f8e\u56fd'

        由以上例子：
        可以看出，当实例没有属性的时候，会继承类的属性

        属性和封装

        私有属性：不能直接访问它，要通过内部的接口进行处理，就是在类内部可见，对外不可见

        __xxx:不能直接访问
        _xxx:可以直接访问，提示直接访问，不合理
        __xxx__:系统自带的属性

        例子：

        # !/usr/bin/env python
        # coding: utf8

        class Car(object):
            country = u'中国'

            def __init__(self, length, width, height, owner=None):
                self.__owner = owner

                assert length > 0, "length mush larger than 0"
                self._length = length
                self._width = width
                self._height = height

            def getOwner(self):
                return self.__owner

            def setOwner(self, value):
                self.__owner = value

            def getLength(self):
                return self._length

            def setLength(self, value):
                assert value > 0, "length must large than 0"
                self._length = value

        if __name__ == '__main__':
            a = Car(1.2, 1.4, 1.5, u'张三')
            print a.getOwner()

            a.setLength(-1)

        结果：
        张三
        Traceback(most
        recent
        call
        last):
        File
        "object2.py", line
        33, in < module >
        a.setLength(-1)

    File
    "object2.py", line
    25, in setLength
    assert value > 0, "length must large than 0"


AssertionError: length
must
large
than
0

>> > a.__owner
Traceback(most
recent
call
last):
File
"<stdin>", line
1, in < module >
AttributeError: 'Car'
object
has
no
attribute
'__owner'
>> > dir(a)
['_Car__owner', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__',
 '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', '_height', '_length', '_width', 'country', 'getLength', 'getOwner', 'setLength',
 'setOwner']
>> > a._length
1.2
>> > a._Car__owner
u'\u5f20\u4e09'
>> > a._Car__owner = u'china'
>> > a._Car__owner
u'china'
>> > a._length
1.2
>> > a._length = 3
>> > a._length = 3
>> > a._length
3
>> > a.setLength(4)
>> > a._length
4

封装
把属性给隐藏起来，提供出来，定义接口

装饰器描述符

描述符：定义了get，set的对象, 方法当成属性访问


@property
@xxx.setter
@xxx.deleter
class Car(object):
    country = u'中国'

    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height
        self.country = "China"

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self):
        self._owner = value


例子：

# !/usr/bin/env python
# coding: utf8

class Car(object):
    country = u'中国'

    def __init__(self, length, width, height, owner=None):
        self.__owner = owner

        assert length > 0, "length mush larger than 0"
        self._length = length
        self._width = width
        self._height = height

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @owner.deleter
    def owner(self):
        self.__owner = None

    @property
    def length(self):
        return self._length

    @length.deleter
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        assert value > 0, "length must large than 0"
        self._length = value


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')
    print a.owner
    del a.owner
    print a.owner
    a.length = 3
    print a.length

结果：
root @ VM - 166 - 182 - ubuntu:~ / python / notebook  # python -i object3.py
张三
None
3
>> > a.length
3
>> > a.length = -1
Traceback(most
recent
call
last):
File
"<stdin>", line
1, in < module >
File
"object3.py", line
37, in length
assert value > 0, "length must large than 0"
AssertionError: length
must
large
than
0
>> > a.length = 4
>> > dir(a)
['_Car__owner', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__',
 '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', '_height', '_length', '_width', 'country', 'length', 'owner']

问题1： 如果每个属性的设置都使用 @ property,


@attr.setter

, @attr.deleter

, 就会代码太冗余，并且很麻烦？如何解决，
使用getattr(), setattr()

特殊方法：

__getattr__
__setattr__
__delattr__

__getattr__: 在一些情况下，会自动调用，调用方式，在instance.__dict__和
instance._Class.__dict__没有找到属性的时候就会调用

__setattr__: 在你进行属性赋值设置的时候就会调用

__delattr__: 在你删除属性的时候，就会调用

例子：
# !/usr/bin/env python
# coding: utf8

class Car(object):
    country = u'中国'

    def __init__(self, length, width, height, owner=None):
        self.__owner = owner

        assert length > 0, "length mush larger than 0"
        self._length = length
        self._width = width
        self._height = height

    def __getattr__(self, item):
        print "__getattr__", item
        return self.__dict__.get(item, None)

    def __setattr__(self, key, value):
        print "__setattr__", key, value
        if key != 'owner':
            assert value > 0, name + "must large than 0"
        self.__dict__[key] = value

    def __delattr__(self, item):
        print "__delattr__", item
        if item == 'owner':
            self.__dict__[item] = None


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')

结果：
root @ VM - 166 - 182 - ubuntu:~ / python / notebook  # python -i object4.py
__setattr__
_Car__owner
张三
__setattr__
_length
1.2
__setattr__
_width
1.4
__setattr__
_height
1.5
>> > a.length = -1
__setattr__
length - 1
Traceback(most
recent
call
last):
File
"<stdin>", line
1, in < module >
File
"object4.py", line
22, in __setattr__
assert value > 0, name + "must large than 0"
NameError: global name
'name' is not defined
>> > a.length = 5
__setattr__
length
5
>> > a.owner
__getattr__
owner
>> > a.owner = 'china'
__setattr__
owner
china
>> > a.owner  # 当 属性在 instance.__dict__和instance._Class.__dict__中找不到的时候，才会调用__getattr__
'china'
>> > a.item
__getattr__
item
>> > del a.owner
__delattr__
owner
Traceback(most
recent
call
last):
File
"<stdin>", line
1, in < module >
File
"object4.py", line
28, in __delattr__
self.__dict__[name] = None
NameError: global name
'name' is not defined
>> > a.length
5

问题：如何设置在使用


def __setattr__情况下，


限制属性的设置，使用
__slots__ = (), 不起作用?
由于在__dict__中，__slots__中限制了，但是在__getattr__中，没有限制。在__dict__中不能进行设置属性，但是在__settattr__就可以执行。


提示：容易出现下面的问题：
RuntimeError: maximum
recursion
depth
exceeded

解决__getattr__和
__slots__限制属性访问
通过在判断是否在__slots__中判断

assert item in self.__dict__

例子：
# !/usr/bin/env python
# coding: utf8

class Car(object):
    country = u'中国'
    __slots__ = ('length', 'owner', 'height', '__dict__')

    def __init__(self, length, width, height, owner=None):
        self.__owner = owner

        assert length > 0, "length mush larger than 0"
        self._length = length
        self._width = width
        self._height = height

    def __getattr__(self, item):
        print "__getattr__", item
        assert item in self.__dict__, "Not have this attr"
        return self.__dict__.get(item, None)

    def __setattr__(self, key, value):
        print "__setattr__", key, value
        assert key in self.__dict__, "not have this attr"
        if key != 'owner':
            assert value > 0, name + "must large than 0"
        self.__dict__[key] = value

    def __delattr__(self, item):
        print "__delattr__", item
        assert item in self.__dict__, "Not have this attr"
        if item == 'owner':
            self.__dict__[item] = None


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')

__getattr__的另一个用法：

getattr(a, 'length')
在程序运行的时候，动态的获取属性。



描述符

描述符，定义了描述符，可以将这个类在其他类中当做属性进行调用。

__get__
非数据描述符

__get__
__set__


def __get__(self, instance, owner):
    # instance = x
    # owner = type(x)
    print "__get__", instance
    print self.val


def __set__(self, instance, value)
    # instance = x
    PRINT
    "__SET__", instance
    assert value > 0, "Negative value not allowed:" + str(value)
    self.val = value


例子：
# !/usr/bin/env python
# coding: utf8

class PositiveNum(object):
    def __init__(self, value):
        self.val = value

    def __get__(self, instance, owner):
        # instance = a, b
        owner = self.val
        print "__get__", instance, owner
        return self.val

    def __set__(self, instance, value):
        # instance = a, b
        print "__set__", instance, value
        try:
            assert int(value) > 0
            self.val = value
        except AssertionError:
            print "Error:" + str(value) + "is not positiveNum"
        except:
            print "ERROR:" + str(value) + "is not number"

    def __delete__(self, instance):
        print "__delete__", instance
        self.val = None

    def __getattr__(self, name):
        print self, name


class Car(object):
    country = u'中国'
    length = PositiveNum(0)
    width = PositiveNum(0)
    height = PositiveNum(0)

    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height


if __name__ == '__main__':
    a = Car(1.2, 1.4, 1.5, u'张三')
    b = Car(2.2, 3.4, 4.5, u'李四')

方法：
分类

类方法，@method


--绑定类
实例方法 - - 绑定实例对象
静态方法,


@staticmethod


--无绑定, 只是通过实例或类进行调用

特殊方法(魔法方法), __init__

形式上的区别：
1.
调用是通过类和实例进行的，不能直接调用
2.
有自己的特殊参数，self，cls
3.
有自己的声明语法，@classmethod

, @staticmethod

, __xxx__()

实质区别：

--绑定类
--绑定实例方法

维护原始的方法，但是因为绑定不同的对象或类，表现的形式也不同

例子：
# !/usr/bin/env python
# coding: utf-8
# http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner

class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{0}-{1}-{2}".format(self.year, self.month, self.day)

    @classmethod
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    @staticmethod
    def millenium(month, day):
        return Date(month, day, 2000)


class DateTime(Date):
    def __str__(self):
        return "{0}-{1}-{2} - 00:00:00PM".format(self.year, self.month, self.day)


if __name__ == "__main__":

    s = '2012-09-11'
    if Date.is_date_valid(s):
        date1 = Date.from_string('2012-09-11')
        print date1
        date2 = DateTime.from_string('2012-09-11')
        print date2

    millenium_new_year1 = Date.millenium(1, 1)
    print millenium_new_year1

    millenium_new_year2 = DateTime.millenium(10, 10)
    print millenium_new_year2

特殊方法：

属性访问： __getattr__, __setattr__, __getattribute__
实例生成、类生成：__init__, __new__
数值计算: __add__, __sub__, __mul__, __div__, __pow__, __round__
调用方法： __str__, __repr__, __len__, __bool__(可以str(), repr(), len(), bool())
比较大小： __cmp__, __lt__, __le__, __eq__, __ne__, __gt__, __get__
集合访问：__setslice__, __getaslice__, __getitem__, __setitem__, __contains__,
迭代器: __iter__, __next__

__init__:实例初始化
__new__:实例或类初始化
__add__:加（对象）

__str__: print 给人看的
__repr__: 给计算机看的，交互模式下，对象名，就会显示repr下定义的内容
__bool__:进行布尔判断

__setslice__, __getslice__:设置切片

__iter__: 迭代器（把一个类做成迭代器）
__next__:

例子：
# !/usr/bin/env python
# coding: utf8

class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __sub__(self, other):
        assert isinstance(other, Point)
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        assert isinstance(other, Point)
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __div__(self, other):
        return Point(self.x / other, self.y / other)

    @property
    def xy(self):
        return (self.x, self.y)

    def __str__(self):
        return "x={0},y={1}".format(self.x, self.y)

    def __repr__(self):
        return str(self.xy)


if __name__ == '__main__':
    a = Point(50, 60)
    b = Point(30, 40)

    print a - b
    print a + b
    print a * 2
    print a / 2

结果：
root @ VM - 166 - 182 - ubuntu:~ / python / notebook  # python object8.py
x = 20.0, y = 20.0
x = 80.0, y = 100.0
x = 100.0, y = 120.0
x = 25.0, y = 30.0
root @ VM - 166 - 182 - ubuntu:~ / python / notebook  # python -i object8.py
x = 20.0, y = 20.0
x = 80.0, y = 100.0
x = 100.0, y = 120.0
x = 25.0, y = 30.0
>> > a - b
(20.0, 20.0)
>> > print a - b
x = 20.0, y = 20.0
>> > str(a)
'x=50.0,y=60.0'
>> > repr(a)
'(50.0, 60.0)'
>> > a + b
(80.0, 100.0)
>> > a.xy
(50.0, 60.0)

继承
简单继承：

class Employee(object):
    def __init__(self, name, job=None, pay=0):
        self._name = name
        self._job = job
        self.pay = pay

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Employee:%s,%s,%s]' % (self._name, self._job, self._pay)

    class Manager(Employee):
        def __init__(self, name, pay):
            Employee.__init__(self.name, 'mgr', pay)  # 调用父类的__init__

        def giveRaise(self, percent, bonus=.10):
            Employee.giveRaise(self, percent + bonus)  # 调用父类的函数，进行重载，覆盖


通过已有的类生成新的类

例子：
#!/usr/bin/env python
# coding: utf8

class Employee(object):
    def __init__(self, name, job=None, pay=0):
        self._name = name
        self._job = job
        self._pay = pay

    def giveRaise(self, percent):
        self._pay = int(self._pay * (1 + percent))

    def __str__(self):
        return '[Employee:%s,%s,%s]' % (self._name, self._job, self._pay)


class Manager(Employee):
    def __init__(self, name, pay):
        Employee.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Employee.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    a = Employee("xiaoli", "sw_engince", 10000)
    b = Employee("xiaowang", "hw_engince", 12000)
    c = Manager("xiaozhang", 8000)

    members = [a, b, c]

    for member in members:
        member.giveRaise(0.1)
        print member
输出：
root@VM-166-182-ubuntu:~/python/notebook# python -i object9.py
[Employee:xiaoli,sw_engince,11000]
[Employee:xiaowang,hw_engince,13200]
[Employee:xiaozhang,mgr,9600]
>>> c.__class__
<class '__main__.Manager'>
>>> c.__class__.__base__
<class '__main__.Employee'>
>>> c.__class__.__base__.__base__
<type 'object'>
>>> c.__class__.__base__.__base__.__base__
>>>





