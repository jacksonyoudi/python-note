#!/usr/bin/env python
# coding:utf8


三层架构

config.py, setting.py: 存放配置信息，定义配置信息
models:
    __init__.py : 保存对数据的操作

utility:
    __init__.py :公共的库函数之类的

三层架构

数据访问层
业务处理层
表示层，UI层

将数据的连接都提取出来
self.__conn_dict = dict(host='locahost', user='python', db='python', passwd='python', port=3306, charset='utf8')
等价于
self.__conn_dict = {'host':'localhost','user':'python'.....}


class MysqlHelper(object):
    def __init__(self):
        self.__conn_dict = dict(host='locahost', user='python', db='python', passwd='python', port=3306, charset='utf8')

        pass

    def get_dict(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursor.DictCursor)

        reCount = cur.execute(sql, params)
        data = cur.fetchall()

        cur.close()
        conn.close()
        return data

    def get_one(self, sql, params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorClass=MySQLdb.cursor.DictCursor)

        reCount = cur.execute(sql, params)
        data = cur.fetchone()

        cur.close()
        conn.close()
        return data


注意：参数的收集 (): * {}: **

self.__conn_dict = ('locahost', 'python', 'python', 'python', 3306,'utf8')
conn = MySQLdb.connect(*self.__conn_dict)