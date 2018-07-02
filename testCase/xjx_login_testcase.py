#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 11:44
# @Author  : Weiqiang.long
# @Site    : 
# @File    : xjx_login_testcase.py
# @Software: PyCharm

import unittest
from utils.config import Config, JsonConfig
from utils.extractor import JMESPathExtractor
from utils.log import logger
from utils.client import HTTPClient


class Test_Xjx_login(unittest.TestCase):
    URL = Config().get('URL')
    logger.info('请求的URL为:{0}'.format(URL))
    LOGIN_URL = Config().get('login_url')

    LOGIN = URL + LOGIN_URL

    def test_Xjx_login(self):
        self.j = JMESPathExtractor()
        self.jsondata = JsonConfig()
        # 获取json配置文件数据
        jsondata = JsonConfig().get_jsondata()
        logger.info('开始执行app登录接口,caseName:test_Xjx_Login')
        self.client = HTTPClient(url=self.LOGIN, method='POST')
        logger.info('请求的api路径为:{0}'.format(self.LOGIN_URL))
        logger.info('拼接后的请求路径为:{0}'.format(self.LOGIN))
        res = self.client.send(data=jsondata)
        logger.info('接口入参为:{0}'.format(jsondata))
        self.assertIn('登录成功', res.text)
        self.sessionid = self.j.extract(query='data.item.sessionid', body=res.text)
        jsondata['sessionid'] = self.sessionid
        logger.debug('该用户的sessionid为:{0}'.format(self.sessionid))
        print('该用户的sessionid为:{0}'.format(self.sessionid))
        return jsondata



if __name__ == '__main__':
    unittest.main()




