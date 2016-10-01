#!/usr/bin/env python
# coding: utf8

show
databases;
user
database_name;
create
databse
database_name
default
charset
utf8;
grant
all
privileges
on
database

增删改查
insert
into
userinto(id, name)
values(1, 'youdi');

select *
from userinfo;

select
where
id =
select
tb1
left / right
join
tb2
on
update
tb1
set
name = 'sb'
where
id = 1;

delete
from userinfo where

...;

navigt
图形化数据库管理工具

id
自增类，用于生成用户唯一id

MySQldb

import MySQLdb

conn = MySQLdb.connect(host='localhsot', user='python', db='python', passwd='python', charset='utf8')
cur = conn.cursor()

reCount = cur.execute('select * from admin')
# 返回执行有影响的行数

data = cur.fetchall()
# 获取所有的数据

cur.close()
conn.close()

print reCount

sql = 'insert into admin(id,name,address) values(%s,%s,);'
params = ('alex_x', 'usa')
Recount = cur.exexcute(sql, params)  # 参数
# 影响的条数

cur.close()
conn.commit()  # 提交
conn.close()

事物：
多个语句，一次提交

一次打开，插入多条数据
import MySQLdb

conn = MySQLdb.connect()
cur = conn.cursor()

for i in a:
    sql =
    cur.execute(sql, params)

cur.executemany()

cur.close()
conn.commit()
conn.close()

事务：
提交，回滚

默认情况下，是事务提交的

conn.rollback()


提示：
Django中事务是通过装饰器进行操作的。


cur  = cur.cursor(cursorclass=MysQLdb.cursors.DictCursor)

fetchone 获取一条数据，每次一条，生成器 yied

cur.scroll(-1,mode='relative')  # 相对
cur.scroll(0,mode='absolute')   # 绝对

fetchmany()

如何在插入数据的时候返回自增id的值？
cur.lastrowid()
在有外键的情况下，进行操作。
