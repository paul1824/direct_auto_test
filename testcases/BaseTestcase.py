# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 16:39
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : BaseTestcase.py
import requests
import json
import unittest
from common import handle_config


class BaseTestcase(unittest.TestCase):

    def get_token(self):
        '''获取token'''
        res = requests.request("post", url=handle_config.conf['BI']['url'],
                               json=json.loads(handle_config.conf['BI']['username_password']))
        # print(res.text)
        text = json.loads(res.text)
        Authorization = 'Bearer ' + text['data']['accessToken']
        return Authorization

