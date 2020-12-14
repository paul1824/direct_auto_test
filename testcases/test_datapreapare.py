# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 14:52
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_datapreapare.py

from testcases.BaseTestcase import *

headers = {'Authorization': BaseTestcase().get_token(), 'Content-Type': 'application/json'}


class TestPreapare(BaseTestcase):
    global id

    def test_001(self):
        '''gp添加分组'''
        url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/__root_group__'
        resp = requests.request("post", url=url, headers=headers)
        print(json.loads(resp.text)['data']['id'])
        globals()['id'] = json.loads(resp.text)['data']['id']
        self.assertIn('data', resp.text)

    def test_002(self):
        '''判断分组重名'''
        url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/__root_group__/names?_=1605669506968'
        resp = requests.request("get", url=url, headers=headers)
        print(resp.text)
        # globals()['id'] = json.loads(resp.text)['data']['id']
        self.assertIn('data', resp.text)

    def test_003(self):
        '''改名为GP分组'''
        url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/' + id
        payload = {"id": id, "name": "GP1"}
        resp = requests.request("put", url=url, headers=headers, json=payload)
        print(resp.text)
        print(url)
        # globals()['id'] = json.loads(resp.text)['data']['id']
        self.assertIn('data', resp.text)

    def test_004(self):
        '''查看分组情况'''
        url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups?_=1607930150655'
        resp = requests.request("get", url=url, headers=headers)
        print(resp.text)
        # print(url)
        # globals()['id'] = json.loads(resp.text)['data']['id']
        self.assertIn('data', resp.text)
