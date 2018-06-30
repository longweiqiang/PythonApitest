#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 17:26
# @Author  : Weiqiang.long
# @Site    : 
# @File    : test_ini.py
# @Software: PyCharm

import os
import configparser

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
INICONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.ini')

# print(INICONFIG_FILE)

config=configparser.ConfigParser()
config.read(INICONFIG_FILE)


# c = config.get("test1")
# print(c)