#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 14:02
# @Author  : yhl
# @Software: PyCharm

import pyodbc as po


class My_pyodbc(object):

    def __init__(self, DSN, UID, PWD):
        self.DSN = DSN
        self.UID = UID
        self.PWD = PWD

    def on_open(self):
        sqlserver_par = "DSN={};UID={};PWD={}".format(self.DSN, self.UID, self.PWD)
        conn = po.connect(sqlserver_par)
        cursor = conn.cursor()
        return conn, cursor

    def cl_close(self, cursor):
        cursor.close()

    def select(self, sqls):
        '''
        :param sqls:
        :return:
        '''
        conn, cursor = self.on_open()
        # 定义要执行的SQL语句
        # sql = "SELECT * from admininfo WHERE user=%s and password=%s;"
        sql = sqls
        cursor.execute(sql)
        ret = cursor.fetchall()
        # 获取多条查询数据
        self.cl_close(cursor)
        return ret

    def insert(self, sqls):
        conn, cursor = self.on_open()
        try:
            # 执行SQL语句
            cursor.execute(sqls)
            # 提交事务
            conn.commit()
            print('Insert SQL OK!')
        except Exception as e:
            # 有异常，回滚事务
            print(e)
            import time
            time.sleep(5)
            conn.rollback()
        self.cl_close(cursor)

    def update(self, sqls):
        conn, cursor = self.on_open()
        # 定义要执行的SQL语句
        # sql = "UPDATE studentinfo SET STUNAME=%s WHERE studentinfo.id=%s;"
        sql = sqls
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交事务
            conn.commit()
            print('Update SQL OK!')
        except Exception as e:
            # 有异常，回滚事务
            print(e)
            conn.rollback()
        self.cl_close(cursor)

    def delcte(self, sqls):
        conn, cursor = self.on_open()
        # 定义要执行的SQL语句
        # sql = "DELETE FROM studentinfo WHERE id=%s;"
        sql = sqls
        try:
            cursor.execute(sql)
            # 提交事务
            conn.commit()
        except Exception as e:
            # 有异常，回滚事务
            conn.rollback()
        self.cl_close(cursor)


if __name__ == '__main__':
    my_pyodbc = My_pyodbc('xxx', 'xxx', 'xxx')
