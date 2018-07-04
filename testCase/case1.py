#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm
import json
import unittest

import jmespath

from utils.config import Config, JsonConfig
from utils.extractor import JMESPathExtractor
from utils.log import logger
from utils.client import HTTPClient

j = {'id': 10967022}

# a = JsonConfig(path='wholesale', jsonpath='before_borrowMoney.json')
# print(a.get_jsondata())
# b = json.dumps(j)
# a = JMESPathExtractor()
# print(a.extract())


all_rights = j
print(all_rights)
json_str = json.dumps(all_rights)
print(json_str)
b = jmespath.search('id', json.loads(json_str))
print(b)
