#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm
import unittest

import requests
from utils.config import Config, CONFIG_FILE1
# from utils.dbconfig import database
from utils.extractor import JMESPathExtractor
from utils.log import logger
from utils.client import HTTPClient



# URL1 = Config(config=CONFIG_FILE1).get('URL')
# print(URL1)


# r = requests.post(LOGIN,data=QUERY)
#
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
    URL = Config().get('URL')
    logger.info('请求的URL为:{0}'.format(URL))
    LOGIN_URL = Config().get('login_url')
    INDEX_URL = Config().get('index_url')
    RISK_URL = Config().get('risk_url')


    QUERY = Config().get('PARAMS')
    LOGIN = URL + LOGIN_URL
    INDEX = URL + INDEX_URL
    RISK = URL + RISK_URL


    def setUp(self):
        self.j = JMESPathExtractor()
        # self.data = 'sessionid: DA9C5688C65DC9BDD3E1115191A7FAAF'
    #     self.client = HTTPClient(url=self.LOGIN, method='POST')
    #     logger.info('请求的api路径为:{0}'.format(self.LOGIN_URL))
    #     logger.info('拼接后的请求路径为:{0}'.format(self.LOGIN))
    #     self.j = JMESPathExtractor()

    def test_xjx_http_login(self):
        self.client = HTTPClient(url=self.LOGIN, method='POST')
        logger.info('请求的api路径为:{0}'.format(self.LOGIN_URL))
        logger.info('拼接后的请求路径为:{0}'.format(self.LOGIN))
        res = self.client.send(data=self.QUERY)
        logger.info('接口入参为:{0}'.format(self.QUERY))
        self.assertIn('登录成功', res.text)
        self.j_1 = self.j.extract(query='data.item.sessionid', body=res.text)
        logger.debug('该用户的sessionid为:{0}'.format(self.j_1))
        print('该用户的sessionid为:{0}'.format(self.j_1))
        return self.j_1

    # def test_xjx_http_index(self):
    #     self.client = HTTPClient(url=self.INDEX, method='GET')
    #     logger.info('请求的api路径为:{0}'.format(self.INDEX_URL))
    #     logger.info('拼接后的请求路径为:{0}'.format(self.INDEX))
    #     res = self.client.send(params=self.QUERY, data=self.j_1)
    #     logger.info('接口入参为:query--{0}\ndata--{1}'.format(self.QUERY, self.j_1))
    #     self.assertIn('访问首页成功',res.text)

    def test_xjx_http_risk(self):
        self.client = HTTPClient(url=self.INDEX, method='GET')
        logger.info('请求的api路径为:{0}'.format(self.RISK_URL))
        logger.info('拼接后的请求路径为:{0}'.format(self.RISK))
        j_2 = TestXjxHTTP.test_xjx_http_login(self.j_1)
        self.client.send(params=self.QUERY, data=j_2)
        logger.info('接口入参为:query--{0}\ndata--{1}'.format(self.QUERY, j_2))





if __name__ == '__main__':
    unittest.main()
