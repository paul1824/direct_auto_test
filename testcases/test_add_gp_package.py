# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 14:52
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_gp_package.py

from testcases.BaseTestcase import *
from common.handle_tools import *


class Test_Add_Gp_Package(BaseTestcase):
    global group_id
    global package_id

    def test_001(self):
        '''gp添加分组'''
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/__root_group__'
        resp = requests.request("post",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package']['group_add'],
                                headers=headers)
        print(json.loads(resp.text)['data']['id'])
        print(resp.text)
        globals()['group_id'] = json.loads(resp.text)['data']['id']
        self.assertEqual(GetDict(resp.text).getdict()['data']['name'], '分组', msg='添加分组不成功')

    def test_002(self):
        '''判断分组重名'''
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/__root_group__/names?_=1605669506968'
        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_name'], headers=headers)
        print(resp.text)
        # globals()['id'] = json.loads(resp.text)['data']['id']
        self.assertIn('data', resp.text)

    def test_003(self):
        '''改名为GP分组'''
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/' + group_id
        payload = {"id": group_id, "name": "GP"}
        resp = requests.request("put", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_rename'] + group_id, headers=headers, json=payload)
        print(resp.text)
        # print(url)
        # globals()['id'] = json.loads(resp.text)['data']['id']
        self.assertIn('data', resp.text)

    def test_004(self):
        '''查看分组情况'''
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups?_=1607930150655'
        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_info'], headers=headers)
        print(resp.text)
        # print(url)
        # globals()['id'] = json.loads(resp.text)['data']['id']
        self.assertIn('data', resp.text)

    def test_005(self):
        '''gp添加业务包'''
        pass
