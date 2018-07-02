#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 14:35
# @Author  : Weiqiang.long
# @Site    : 
# @File    : xjx_index_testcase.py
# @Software: PyCharm

import unittest
from utils.config import Config
from utils.extractor import JMESPathExtractor
from utils.log import logger
from utils.client import HTTPClient

from testCase.xjx_login_testcase import Test_Xjx_login

class Test_Xjx_Index(unittest.TestCase):
    URL = Config().get('URL')
    logger.info('请求的URL为:{0}'.format(URL))
    INDEX_URL = Config().get('index_url')

    INDEX = URL + INDEX_URL


    def setUp(self):
        logger.info('开始执行测试前准备的数据,调用test_Xjx_login方法')
        self.xjx_login = Test_Xjx_login().test_Xjx_login()
        logger.debug('测试前准备的数据为:{0}'.format(self.xjx_login))
        # 获取json配置文件数据
        self.jsondata = self.xjx_login


    def test_xjx_http_index1(self):
        self.j = JMESPathExtractor()
        logger.info('开始执行app首页接口,caseName:test_xjx_http_index1')
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