#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 17:02
# @Author  : Weiqiang.long
# @Site    : 
# @File    : xjx_dr_borrowMoney_testcase.py
# @Software: PyCharm
import json
import unittest
from utils.client import HTTPClient
from testCase.public_testCase.xjx_login_testcase import Test_Xjx_login
from utils.config import JsonConfig, Config
from utils.dbconfig import database
from utils.extractor import JMESPathExtractor
from utils.log import logger
import requests


class Test_Xjx_Dr_BorrowMoney(unittest.TestCase):
    base_url = Config().get('URL')
    bm_url = Config().get('before_borrowMoney_url')
    url = base_url + bm_url
    logger.info('请求的URL为:{0}'.format(url))
    # 调用公共参数
    data = JsonConfig().get_jsondata()
    # test_Xjx_Dr_borrowMoney1调用测试参数
    test_data = JsonConfig(path='wholesale', jsonpath='borrowMoney.json').get_jsondata(element='before_borrowMoney')
    logger.info("测试数据为:{0}".format(test_data))

    # test_Xjx_Dr_borrowMoney2调用测试参数
    borrowMoney_test_data = JsonConfig(path='wholesale', jsonpath='borrowMoney.json').get_jsondata(element='borrowMoney')
    logger.info("测试数据为:{0}".format(borrowMoney_test_data))

    def setUp(self):
        self.j = JMESPathExtractor()
        logger.info('开始执行测试前准备的数据,调用test_Xjx_login方法')
        self.xjx_login = Test_Xjx_login().test_Xjx_login()
        self.data['sessionid'] = self.xjx_login
        logger.info('123测试前准备的数据为:{0}'.format(self.data))
        # 获取json测试数据
        self.jsondata = self.test_data
        # 获取headers数据
        self.j = JMESPathExtractor()
        self.test_headers = JsonConfig(path='wholesale', jsonpath='borrowMoney.json').get_jsondata(element='headers')
        # self.headers = self.j.addextract(query='headers', body=test_headers)
        self.test_headers['sessionid'] = self.xjx_login
        logger.info("123测试前准备的headers为:{0}".format(self.test_headers))

        self.get_dbdata = database()
        select_userBankCardId = "SELECT id FROM user_card_info WHERE user_id = '768093098' ORDER BY id DESC LIMIT 1"
        logger.info('查询数据库数据的sql为:{0}'.format(select_userBankCardId))
        db_userBankCardId_id = self.get_dbdata.fetch_one(select_userBankCardId)
        logger.info('查询数据库的数据,返回的order_id为:{0}'.format(db_userBankCardId_id))
        json_str = json.dumps(db_userBankCardId_id)
        self.one_db_userBankCardId_id = self.j.extract(query='id', body=json_str)
        logger.info('one_db_userBankCardId_id的数据为:{0}'.format(self.one_db_userBankCardId_id))
        self.jsondata['userBankCardId'] = self.one_db_userBankCardId_id
        logger.info('123data数据为:{0}'.format(self.jsondata))



    def test_Xjx_Dr_borrowMoney1(self):
        '''
        大额借款前置方法(请求江西银行存管查询接口)
        :return:
        '''
        before_url = self.url
        # 在测试参数前后追加双引号
        str_test_data = "%s" % self.test_data
        client = HTTPClient(url=before_url, method='POST', headers=self.test_headers)
        res = client.send(data=str_test_data, params=self.data)
        logger.info('123client返回的参数:{0}'.format(res.text))
        # 获取traceNo参数
        self.traceNo = self.j.extract(query='data.traceNo', body=res.text)
        self.borrowMoney_test_data['traceNo'] = self.traceNo
        # 获取userBankCardId参数
        select_orderid = "select id from asset_borrow_order where user_id = '768093098' ORDER BY id DESC LIMIT 1"
        logger.info('查询数据库数据的sql为:{0}'.format(select_orderid))
        db_order_id = self.get_dbdata.fetch_one(select_orderid)
        self.userBankCardId = self.j.extract(query='data.traceNo', body=res.text)
        # 断言
        # 获取borrowMoney.json文件中的assertlist数据
        self.assertlist = JsonConfig(path='wholesale', jsonpath='borrowMoney.json').get_jsondata(element='before_borrowMoney_assertlist')
        logger.info('assertlist数据为:{0}'.format(self.assertlist))
        # 断言rsq_code
        rsq_code = self.j.extract(query='code', body=res.text)
        self.assertEqual(rsq_code, self.j.addextract(query='code', body=self.assertlist))
        # 断言rsq_message
        rsq_message = self.j.extract(query='message', body=res.text)
        self.assertEqual(rsq_message, self.j.addextract(query='message', body=self.assertlist))
        # 断言rsq_orderAmount
        rsq_orderAmount = self.j.extract(query='data.orderAmount', body=res.text)
        self.assertEqual(rsq_orderAmount, self.j.addextract(query='orderAmount', body=self.assertlist))
        # 断言rsq_bankName
        rsq_bankName = self.j.extract(query='data.bankName', body=res.text)
        self.assertEqual(rsq_bankName, self.j.addextract(query='bankName', body=self.assertlist))
        # 断言rsq_cardNoLastFour
        rsq_cardNoLastFour = self.j.extract(query='data.cardNoLastFour', body=res.text)
        self.assertEqual(rsq_cardNoLastFour, self.j.addextract(query='cardNoLastFour', body=self.assertlist))



    def test_Xjx_Dr_borrowMoney2(self):
        '''
        大额借款方法
        :return:
        '''
        borrowMoney_url = Config().get('borrowMoney_url')
        url = self.base_url + borrowMoney_url
        logger.info('大额借款的接口地址为:{0}'.format(url))

        client = HTTPClient(url=url, method='POST', headers=self.test_headers)
        #set相关参数到测试参数中
        self.borrowMoney_test_data['userBankCardId'] = self.one_db_userBankCardId_id
        # 在测试参数前后追加双引号
        # test_data = self.borrowMoney_test_data.encode("utf-8")
        str_test_data = "%s" %self.borrowMoney_test_data

        logger.info('321参数:{0}'.format(str_test_data))
        res = client.send(data=str_test_data, params=self.data)
        logger.info('123456client返回的参数:{0}'.format(res.text))












if __name__ == '__main__':
    unittest.main()