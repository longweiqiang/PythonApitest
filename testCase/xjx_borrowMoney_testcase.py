#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 15:25
# @Author  : Weiqiang.long
# @Site    : 
# @File    : xjx_borrowMoney_testcase.py
# @Software: PyCharm
import json

import requests

from testCase.xjx_login_testcase import Test_Xjx_login
from utils.client import HTTPClient
from utils.config import Config, JsonConfig
import unittest

from utils.extractor import JMESPathExtractor
from utils.log import logger




# BorrowMoney_URL = Config().get('borrowMoney_url')

# get_jsondata = JsonConfig(jsonpath='borrowMoney.json')
# borrow_money = get_jsondata.get_jsondata()
# # print(borrow_money)

class Test_Xjx_BorrowMoney(unittest.TestCase):
    URL = Config().get('URL')
    logger.info('请求的URL为:{0}'.format(URL))
    BorrowMoney_URL = Config().get('borrowMoney_url')

    get_jsondata = Config(config='borrowMoney.yml')
    borrow_money = get_jsondata.get('borrowMoney')
    period = get_jsondata.get('period')




    def setUp(self):
        logger.info('开始执行测试前准备的数据,调用test_Xjx_login方法')
        self.xjx_login = Test_Xjx_login().test_Xjx_login()
        logger.debug('测试前准备的数据为:{0}'.format(self.xjx_login))
        # 获取json配置文件数据
        self.jsondata = self.xjx_login
        self.j = JMESPathExtractor()
        self.jsondata['money'] = self.borrow_money
        self.jsondata['period'] = self.period

    # def test_test1(self):
    #     print(type(self.jsondata))


    def test_xjx_borrowMoney1(self):
        BorrowMoney = self.URL + self.BorrowMoney_URL
        logger.info('开始执行app借款接口,caseName:test_xjx_borrowMoney1')
        self.client = HTTPClient(url=BorrowMoney, method='POST')
        logger.info('请求的api路径为:{0}'.format(self.BorrowMoney_URL))
        logger.info('拼接后的请求路径为:{0}'.format(BorrowMoney))

        res = self.client.send(data=self.jsondata)
        # res = requests.post(url=BorrowMoney, data=self.jsondata)
        logger.info('返回的参数为:{0}'.format(res.text))
        logger.info('接口入参为:query--{0}'.format(self.jsondata))
        self.assertIn('中国农业银行', res.text)
        self.assertIn('成功', res.text)
        # data.item.card_no_lastFour的值为该测试用户的银行卡最后四位
        card_no_lastFour = self.j.extract(query='data.item.card_no_lastFour', body=res.text)
        # # 判断card_no_lastFour的值是否一致
        self.assertEqual(card_no_lastFour, '0002')

if __name__ == '__main__':
    unittest.main()



