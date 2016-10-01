'''
create on 2016-0928
'''

import MySQLdb


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


#
