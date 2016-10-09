collections模块在内置的数据类型的基础上，提供了几个额外的数据类型：
1.namedtuple():生成可以使用名字来访问元素内容的tuple子类
2.deque：双端队列，可以快速的从另一侧追加和弹出对象
3.Counter：计数器，主要用来计数
4.orderDict:有序字典
5.defaultdict：带默认值的字典


1.namedtuple
def namedtuple(typename, field_names, verbose=False, rename=False):
    pass

2.deque是double-ended queue的缩写双端队列，最大的好处就是实现从队列的头部快速增加和取出对象：.popleft(),.appendleft()
a.append      a.clear       a.extend      a.maxlen      a.popleft     a.reverse
a.appendleft  a.count       a.extendleft  a.pop         a.remove      a.rotate   


