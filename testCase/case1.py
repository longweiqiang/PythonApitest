#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm

import requests
from utils.config import Config, CONFIG_FILE, INICONFIG_FILE
from utils.config import IniConfig

# URL = Config().get('URL')
PARAMS = Config().get('PARAMS')
print(PARAMS)

te = IniConfig().get('test1','mask')
print(te)


# r = requests.get(URL+'/credit-app/index',params='clientType=android&appVersion=3.3.0&deviceId=864553033145254&mobilePhone=17621717316&deviceName=OPPO%20R11&osVersion=7.1.1&appName=jsxjx&packageId=com.innext.xjx&appMarket=xjx-MySelf&merchantNumber=cjxjx')
#
# print(r.url)
# print(r.status_code)
# print(r.text)