#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm
import configparser
import os
import unittest

import requests

from utils import config
from utils.config import Config
# from utils.dbconfig import database
from utils.extractor import JMESPathExtractor
from utils.log import logger
from utils.client import HTTPClient


PARAMS = {'clientType':'android',
            'appVersion':'3.3.0',
            'deviceId':'864553033145254',
            'mobilePhone':'17621717316',
            'deviceName':'OPPO%20R11',
            'osVersion':'7.1.1',
            'appName':'jsxjx',
            'packageId':'com.innext.xjx',
            'appMarket':'xjx-MySelf',
            'merchantNumber':'cjxjx',
            'username':'17621717316',
            'password':'a123456'
          }

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


    # QUERY = I().get('PARAMS')
    LOGIN = URL + LOGIN_URL
    INDEX = URL + INDEX_URL
    RISK = URL + RISK_URL



    # def setUp(self):

        # self.data = 'sessionid: DA9C5688C65DC9BDD3E1115191A7FAAF'
    #     self.client = HTTPClient(url=self.LOGIN, method='POST')
    #     logger.info('请求的api路径为:{0}'.format(self.LOGIN_URL))
    #     logger.info('拼接后的请求路径为:{0}'.format(self.LOGIN))
    #     self.j = JMESPathExtractor()

    def setUp(self):
        self.j = JMESPathExtractor()
        self.client = HTTPClient(url=self.LOGIN, method='POST')
        logger.info('请求的api路径为:{0}'.format(self.LOGIN_URL))
        logger.info('拼接后的请求路径为:{0}'.format(self.LOGIN))
        res = self.client.send(data=PARAMS)
        logger.info('接口入参为:{0}'.format(PARAMS))
        # self.assertIn('登录成功', res.text)
        self.sessionid = self.j.extract(query='data.item.sessionid', body=res.text)
        PARAMS['sessionid'] = self.sessionid
        logger.debug('该用户的sessionid为:{0}'.format(self.sessionid))
        print('该用户的sessionid为:{0}'.format(self.sessionid))
        print(PARAMS)

    # def test_xjx_http_index(self):
    #     self.client = HTTPClient(url=self.INDEX, method='GET')
    #     logger.info('请求的api路径为:{0}'.format(self.INDEX_URL))
    #     logger.info('拼接后的请求路径为:{0}'.format(self.INDEX))
    #     res = self.client.send(params=self.QUERY, data=self.j_1)
    #     logger.info('接口入参为:query--{0}\ndata--{1}'.format(self.QUERY, self.j_1))
    #     self.assertIn('访问首页成功',res.text)

    def test_xjx_http_index1(self):
        # self.client = HTTPClient(url=self.INDEX, method='GET')
        # logger.info('请求的api路径为:{0}'.format(self.RISK_URL))
        # logger.info('拼接后的请求路径为:{0}'.format(self.RISK))
        # res = self.client.send(params=self.QUERY, data=self.sessionid)
        res = requests.get(url=self.RISK, params=PARAMS)
        logger.info('返回的参数为:{0}'.format(res.text))
        logger.info('接口入参为:query--{0}'.format(PARAMS))







if __name__ == '__main__':
    unittest.main()
