# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 16:39
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : BaseTestcase.py
import requests
import json
import unittest
from common import handle_config
from common.handle_tools import *


class BaseTestcase(unittest.TestCase):

    def get_token(self):
        """获取token"""
        res = requests.request("post", url=handle_config.conf['BI']['url'],
                               json=json.loads(handle_config.conf['BI']['username_password']))
        # print(res.text)
        text = json.loads(res.text)

        authorization = 'Bearer ' + text['data']['accessToken']
        return authorization


headers = {'Authorization': BaseTestcase().get_token(), 'Content-Type': 'application/json'}

