#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm
import json

import requests
from utils.config import Config, CONFIG_FILE, INICONFIG_FILE
from utils.config import IniConfig
from utils.dbconfig import database
from utils.dbtest import MysqldbHelper

# URL = Config().get('URL')
# PARAMS = Config().get('PARAMS')
# print(PARAMS)
#
# te = IniConfig().get('test1','mask')
# print(te)
#
#
# r = requests.get(URL+'/credit-app/index',params=PARAMS)
#
# print(r.url)
# print(r.status_code)
# print(r.text)


mh = database()
sql = "select id from user_info where user_phone =17621717316"
a = mh.fetch_one(sql)
# print(a)
# print(type(a))
# b = json.dumps(a)

b = a.values()

print(b)
print(a.get("id"))
print(a["id"])



