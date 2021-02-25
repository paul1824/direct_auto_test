# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 10:42
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_login.py

from direct_auto_test.testcases.BaseTestcase import *


class TestLogin(BaseTestcase):
    def test_001(self):
        """测试登录是否成功"""
        authorization = self.get_token()
        print(authorization)
        self.assertTrue(authorization)

    def test_002(self):
        """测试获取数据连接信息"""
        url = 'http://localhost:37799/webroot/decision/v10/config/connection/list'
        # headers = {'Authorization': self.get_token()}
        resp = requests.request("get", url, headers=headers)
        print(resp.text)
        self.assertIn('data', resp.text)
