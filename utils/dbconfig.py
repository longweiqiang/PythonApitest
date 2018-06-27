#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 11:33
# @Author  : Weiqiang.long
# @Site    : 
# @File    : dbconfig.py
# @Software: PyCharm

# encoding:utf-8
# name:mod_db.py
'''
使用方法：1.在主程序中先实例化DB Mysql数据库操作类。
        2.使用方法:db=database()  db.fetch_all("sql")
'''
import MySQLdb
import MySQLdb.cursors
from utils.config import IniConfig

DBHOST = IniConfig().get('DB', 'host')
DBUSER = IniConfig().get('DB', 'user')
DBPWD = IniConfig().get('DB', 'password')
DBNAME = IniConfig().get('DB', 'database')
DBCHARSET = IniConfig().get('DB', 'charset')
DBPORT = IniConfig().get('DB', 'dbport')



# 数据库操作类
class database:
    # 注，python的self等于其它语言的this
    def __init__(self, dbname=None, dbhost=None):
        # 这里的None相当于其它语言的NULL
        if dbname is None:
            self._dbname = DBNAME
        else:
            self._dbname = dbname
        if dbhost is None:
            self._dbhost = DBHOST
        else:
            self._dbhost = dbhost

        self._dbuser = DBUSER
        self._dbpassword = DBPWD
        self._dbcharset = DBCHARSET
        self._dbport = int(DBPORT)
        self._conn = self.connectMySQL()

        if (self._conn):
            self._cursor = self._conn.cursor()

    # 数据库连接
    def connectMySQL(self):
        conn = False
        try:
            conn = MySQLdb.connect(host=self._dbhost,
                                   user=self._dbuser,
                                   passwd=self._dbpassword,
                                   db=self._dbname,
                                   port=self._dbport,
                                   cursorclass=MySQLdb.cursors.DictCursor,
                                   charset=self._dbcharset,
                                   )
        except Exception:
            conn = False
        return conn

    # 获取查询结果集
    def fetch_all(self, sql):
        res = ''
        if (self._conn):
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception:
                res = False
        return res

    # 获取查询结果集
    def fetch_one(self, sql):
        res = ''
        if (self._conn):
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchone()
            except Exception:
                res = False
        return res

    def update(self, sql):
        flag = False
        if (self._conn):
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                flag = True
            except Exception:
                flag = False
                # self._logger.warn("update database exception, %s" % data)

        return flag

    # 关闭数据库连接
    def close(self):
        if (self._conn):
            if (type(self._cursor) == 'object'):
                self._cursor.close()
            if (type(self._conn) == 'object'):
                self._conn.close()
                # self._logger.warn("close database exception, %s,%s,%s" % (data, type(self._cursor), type(self._conn)))