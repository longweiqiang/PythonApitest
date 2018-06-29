#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm

import requests
from utils.config import Config
from utils.dbconfig import database
from utils.extractor import JMESPathExtractor

URL = Config().get('URL')
print(URL)
LOGIN_URL = Config().get('login_url')
print(LOGIN_URL)
QUERY = Config().get('PARAMS')
print(QUERY)
LOGIN = URL + LOGIN_URL
print(LOGIN)




r = requests.post(LOGIN,data=QUERY)

# print(r.url)
# print(r.status_code)
rr = r.text
# print(r.text)
j = JMESPathExtractor()
j_1 = j.extract(query='data.item.sessionid', body=rr)
print(j_1)



mh = database()
sql = "select id from user_info where user_phone =17621717316"
a = mh.fetch_one(sql)
print(a.get("id"))


