#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 14:31
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case2.py
# @Software: PyCharm

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("rm-bp1rc23s40ss8j9lwo.mysql.rds.aliyuncs.com",
                     "user_test", "pmn4FIBzkaRsSIqQ", "03cashman", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("select * from user_info where user_phone = 17621717316")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print(data)
print(type(data))

# 关闭数据库连接
db.close()