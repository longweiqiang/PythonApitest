#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 15:25
# @Author  : Weiqiang.long
# @Site    : 
# @File    : xjx_borrowMoney_testcase.py
# @Software: PyCharm

from testCase.public_testCase.xjx_login_testcase import Test_Xjx_login
from utils.client import HTTPClient
from utils.config import Config, JsonConfig
import unittest
from utils.dbconfig import database
from utils.extractor import JMESPathExtractor
from utils.log import logger




# BorrowMoney_URL = Config().get('borrowMoney_url')

# get_jsondata = JsonConfig(jsonpath='borrowMoney.wholesale')
# borrow_money = get_jsondata.get_jsondata()
# # print(borrow_money)

class Test_Xjx_BorrowMoney(unittest.TestCase):
    URL = Config().get('URL')
    logger.info('请求的URL为:{0}'.format(URL))
    BorrowMoney_URL = Config().get('borrowMoney_url')
    addBorrowMoney_URL = Config().get('addBorrowMoney_url')

    data = JsonConfig().get_jsondata()
    logger.info('data数据为:{0}'.format(data))

    get_jsondata = Config(path='driblet', config='borrowMoney.yml')
    borrow_money = get_jsondata.get('borrowMoney')
    period = get_jsondata.get('period')






    def setUp(self):
        self.j = JMESPathExtractor()
        logger.info('开始执行测试前准备的数据,调用test_Xjx_login方法')
        self.xjx_login = Test_Xjx_login().test_Xjx_login()
        self.data['sessionid'] = self.xjx_login
        logger.debug('测试前准备的数据为:{0}'.format(self.data))
        # 获取json配置文件数据
        self.jsondata = self.data
        self.j = JMESPathExtractor()
        self.get_dbdata = database()
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

    def test_xjx_borrowMoney2(self):
        addBorrowMoney = self.URL + self.addBorrowMoney_URL
        logger.info('开始执行新增app借款接口,caseName:test_xjx_borrowMoney2')
        self.client = HTTPClient(url=addBorrowMoney, method='POST')
        logger.info('请求的api路径为:{0}'.format(self.addBorrowMoney_URL))
        logger.info('拼接后的请求路径为:{0}'.format(addBorrowMoney))
        self.jsondata['speedStatus'] = ''
        self.jsondata['pay_password'] = '000000'

        res = self.client.send(data=self.jsondata)
        logger.info('返回的参数为:{0}'.format(res.text))
        logger.info('接口入参为:query--{0}'.format(self.jsondata))

        self.assertIn('成功', res.text)

        item_message = self.j.extract(query='data.item.message', body=res.text)
        self.assertEqual(item_message, '申请成功')
        order_id = self.j.extract(query='data.item.order_id', body=res.text)
        logger.info('页面返回的order_id为:{0}'.format(order_id))
        select_orderid = "select id from asset_borrow_order where user_id = '768093098' ORDER BY id DESC LIMIT 1"
        logger.info('查询数据库数据的sql为:{0}'.format(select_orderid))
        db_order_id = self.get_dbdata.fetch_one(select_orderid)
        logger.info('查询数据库的数据,返回的order_id为:{0}'.format(db_order_id))


if __name__ == '__main__':
    unittest.main()



