# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 14:52
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_gp_package.py

from testcases.BaseTestcase import *


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
        self.assertIn('分组', GetDict(resp.text).getdict()['data'], msg='判断分组重名有问题')

    def test_003(self):
        '''改名为GP分组'''
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/' + group_id
        payload = {"id": group_id, "name": "GP"}
        resp = requests.request("put", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_rename'] + group_id, headers=headers, json=payload)
        print(resp.text)
        # self.assertIn('success', resp.text,msg='重命名有问题')
        self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='重命名有问题')

    def test_004(self):
        '''查看分组情况'''
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups?_=1607930150655'
        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_info'], headers=headers)
        # data_group_id=''
        print(resp.text)
        # for i in GetDict(resp.text).getdict()['data']:
        #     for j in GetDict(resp.text).getdict()['data']['name']:
        #         if GetDict(resp.text).getdict()['data'][i][j]== 'GP':
        #             data_group_id=GetDict(resp.text).getdict()['data'][i][j]

        self.assertEqual(GetDict(resp.text).getdict()['data'][0]['id'], group_id)
        # self.assertEqual(data_group_id, group_id)
    def test_005(self):
        '''gp添加业务包'''
        pass
