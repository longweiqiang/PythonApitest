#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 11:44
# @Author  : Weiqiang.long
# @Site    : 
# @File    : xjx_login_testcase.py
# @Software: PyCharm
import json

from utils.config import JsonConfig

#
a = JsonConfig()
# print(a.get_jsondata())
print(a.get_jsondata(element='clientType'))
# b = a.get_jsondata()
# print(b)
# c = json.dumps(b)
# print(c)


