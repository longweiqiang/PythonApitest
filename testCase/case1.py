#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:16
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case1.py
# @Software: PyCharm

import unittest
from utils.config import Config, JsonConfig
from utils.extractor import JMESPathExtractor
from utils.log import logger
from utils.client import HTTPClient


# PARAMS = {'clientType':'android',
#             'appVersion':'3.3.0',
#             'deviceId':'864553033145254',
#             'mobilePhone':'17621717316',
#             'deviceName':'OPPO%20R11',
#             'osVersion':'7.1.1',
#             'appName':'jsxjx',
#             'packageId':'com.innext.xjx',
#             'appMarket':'xjx-MySelf',
#             'merchantNumber':'cjxjx',
#             'username':'17621717316',
#             'password':'a123456'
#           }




class TestXjxHTTP(unittest.TestCase):
    URL = Config().get('URL')
    logger.info('请求的URL为:{0}'.format(URL))
    LOGIN_URL = Config().get('login_url')
    INDEX_URL = Config().get('index_url')

    LOGIN = URL + LOGIN_URL
    INDEX = URL + INDEX_URL


    def setUp(self):

        self.j = JMESPathExtractor()
        # 获取json配置文件数据
        self.jsondata = JsonConfig().get_jsondata()
        self.client = HTTPClient(url=self.LOGIN, method='POST')
        logger.info('请求的api路径为:{0}'.format(self.LOGIN_URL))
        logger.info('拼接后的请求路径为:{0}'.format(self.LOGIN))
        res = self.client.send(data=self.jsondata)
        logger.info('接口入参为:{0}'.format(self.jsondata))
        self.assertIn('登录成功', res.text)
        self.sessionid = self.j.extract(query='data.item.sessionid', body=res.text)
        self.jsondata['sessionid'] = self.sessionid
        logger.debug('该用户的sessionid为:{0}'.format(self.sessionid))
        print('该用户的sessionid为:{0}'.format(self.sessionid))
        print(self.jsondata)


    def test_xjx_http_index1(self):
        self.client = HTTPClient(url=self.INDEX, method='GET')
        logger.info('请求的api路径为:{0}'.format(self.INDEX_URL))
        logger.info('拼接后的请求路径为:{0}'.format(self.INDEX))
        res = self.client.send(params=self.jsondata)
        logger.info('返回的参数为:{0}'.format(res.text))
        logger.info('接口入参为:query--{0}'.format(self.jsondata))
        self.assertIn('访问首页成功', res.text)
        # data.item.loginStatus的值为登录标识,1为已登录;0为未登录
        login_status = self.j.extract(query='data.item.loginStatus', body=res.text)
        # print(login_status)
        # 判断login_status的值是否是1
        self.assertEqual(login_status, '1')







if __name__ == '__main__':
    unittest.main()
