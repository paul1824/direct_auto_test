# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 14:52
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_gp_package.py

from testcases.BaseTestcase import *


class TestAddGpPackage(BaseTestcase):
    global group_id
    global package_id

    def test_001(self):
        """gp添加分组"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/__root_group__'
        resp = requests.request("post",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package']['group_add'],
                                headers=headers)
        # print(json.loads(resp.text)['data']['id'])
        print(resp.text)
        globals()['group_id'] = json.loads(resp.text)['data']['id']
        if GetDict(resp.text).getdict()['data']['name'] == '分组':
            self.assertEqual(GetDict(resp.text).getdict()['data']['id'], group_id, msg='添加分组不成功')

    def test_002(self):
        """判断分组重名"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/__root_group__/names?_=1605669506968'
        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_name'], headers=headers)
        print(resp.text)
        self.assertIn('分组', GetDict(resp.text).getdict()['data'], msg='判断分组重名有问题')

    def test_003(self):
        """改名为GP分组"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/' + group_id
        payload = {"id": group_id, "name": "GP"}
        resp = requests.request("put", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_rename'] + group_id, headers=headers, json=payload)
        print(resp.text)
        # self.assertIn('success', resp.text,msg='重命名有问题')
        self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='重命名有问题')

    def test_004(self):
        """查看分组情况"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups?_=1607930150655'
        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_info'], headers=headers)
        print(resp.text)
        for i, ele in enumerate(GetDict(resp.text).getdict()['data']):
            if ele['id'] == group_id:
                self.assertEqual(ele['name'], 'GP')

    def test_005(self):
        """gp添加业务包"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/{{gp_group}}/packs'
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'pack_add_1'] + group_id + handle_config.conf['package']['pack_add_2'], headers=headers)
        # print(json.loads(resp.text)['data']['id'])
        print(resp.text)
        globals()['package_id'] = json.loads(resp.text)['data']['id']
        # self.assertEqual(GetDict(resp.text).getdict()['data']['name'], '业务包', msg='添加业务包不成功')
        if GetDict(resp.text).getdict()['data']['name'] == '业务包':
            self.assertEqual(GetDict(resp.text).getdict()['data']['id'], package_id, msg='添加业务包不成功')

    def test_006(self):
        """判断业务包重名请求"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/pack/names?_=1605679085534'
        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'pack_name'], headers=headers)
        print(resp.text)
        self.assertIn('业务包', GetDict(resp.text).getdict()['data'], msg='判断业务包重名有问题')

    def test_007(self):
        """改名为GP业务包"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/' + package_id
        payload = {"id": package_id, "name": "GP"}
        resp = requests.request("put", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'pack_rename'] + package_id, headers=headers, json=payload)
        print(resp.text)
        # self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='重命名有问题')
        if GetDict(resp.text).getdict()['data']['id'] == package_id:
            self.assertEqual(GetDict(resp.text).getdict()['data']['name'], 'GP', msg='重命名有问题')
