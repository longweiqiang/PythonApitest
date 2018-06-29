#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm
import unittest

import requests
from utils.config import Config
from utils.dbconfig import database
from utils.extractor import JMESPathExtractor
from utils.log import logger
from utils.client import HTTPClient

URL = Config().get('URL')
print(URL)
LOGIN_URL = Config().get('login_url')
print(LOGIN_URL)
QUERY = Config().get('PARAMS')
logger.info(QUERY)
LOGIN = URL + LOGIN_URL
logger.info(LOGIN)




r = requests.post(LOGIN,data=QUERY)

# print(r.url)
# print(r.status_code)
# rr = r.text
# print(r.text)
# j = JMESPathExtractor()
# j_1 = j.extract(query='data.item.sessionid', body=rr)
# print(j_1)
#
#
#
# mh = database()
# sql = "select id from user_info where user_phone =17621717316"
# a = mh.fetch_one(sql)
# print(a.get("id"))


class TestXjxHTTP(unittest.TestCase):

    def setUp(self):
        self.client = HTTPClient(url=LOGIN, method='POST')
        self.j = JMESPathExtractor()

    def test_xjx_http(self):
        res = self.client.send(data=QUERY)
        logger.debug(res.text)
        self.assertIn('登录成功', res.text)
        j_1 = self.j.extract(query='data.item.sessionid', body=res.text)
        logger.debug('该用户的sessionid为:{0}'.format(j_1))


if __name__ == '__main__':
    unittest.main(TestXjxHTTP('test_xjx_http'))
