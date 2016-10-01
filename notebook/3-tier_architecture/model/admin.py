#!/usr/bin/env python
# coding: utf8

from utility.sql_helper import MySqlHelper

class Admin(object):
    def __init__(self):
        self.__helper = MySqlHelper()

    def get_one(self, id):
        sql = "select * from admin where id=%s;"
        params = (id,)
        return self.__helper.get_one(sql, params)

    def checkvalidate(self, username, password):
        sql = "select ccount(*)  from admin where name=%s and password =%s; "
        params = (username, password)
        return self.__helper.get_one(sql, params)
