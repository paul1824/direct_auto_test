# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 13:59
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_sql_tables.py

from common.handle_db import *
from testcases.BaseTestcase import *
import urllib.parse

global gp_connection
global redshift_connection
global group_id
global package_id


class TestAddDbTables(BaseTestcase):
    def setUp(self) -> None:
        """获取数据连接列表"""
        res = requests.request("get",
                               url=handle_config.conf['BI_API']['dec'] + handle_config.conf['connection']['list'],
                               headers=headers)
        for i, ele in enumerate(GetDict(res.text).getdict()['data']):
            if ele['connectionName'] == 'gp':
                globals()['gp_connection'] = GetDict(res.text).getdict()['data'][i]['connectionName']
            elif ele['connectionName'] == 'redshift':
                globals()['redshift_connection'] = GetDict(res.text).getdict()['data'][i]['connectionName']

        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['package'][
            'group_info'], headers=headers)
        # print(resp.text)
        for i, ele_g in enumerate(GetDict(resp.text).getdict()['data']):
            if ele_g['name'] == 'GP':
                globals()['group_id'] = ele_g['id']
                for j, ele_p in enumerate(ele_g['packs']):
                    if ele_p['name'] == 'GP':
                        globals()['package_id'] = ele_p['id']

    def test_001(self):
        """添加sql数据集"""
        payload = '{"fields":[],"operatorBeans":[],"paramSetting":[],"memorize":false,"initTime":0,' \
                  '"lastUpdateTime":0,"editable":false,"selected":0,"type":2,"engineType":0,' \
                  '"pack":"' + package_id + '","name":"合同事实表",' \
                                            '"sql":"0DWkpLqaCG5BozNbdl3UYYJZZMfxPzf3wLzBkAW9LXYc8osNpsGcavle+9IdFTI0' \
                                            '","connectionName":"gp",' \
                                            '"operators":[],"transferName":"合同事实表"}'
        resp = requests.request("post",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                    'sql_add_table'],
                                headers=headers, json=json.loads(payload))
        print(resp.text)
        self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='添加sql数据集不成功')

    def test_002(self):
        """修改sql里面预览sql数据集"""
        payload_param = '{"sql":"0DWkpLqaCG5BozNbdl3UYYJZZMfxPzf3wLzBkAW9LXblq16IkCHv990AjoHIkCl1"}'
        resp_param = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'sql_param'], headers=headers, json=json.loads(payload_param))
        print(resp_param.text)
        self.assertEqual(GetDict(resp_param.text).getdict()['message'], 'success', msg='获取sql数据集参数失败')
        self.assertEqual(len(GetDict(resp_param.text).getdict()['data']['params']), 0, msg='获取参数个数正确')
        payload_preview = '{"pack":"' + package_id + '",' \
                                                     '"sql' \
                                                     '":"0DWkpLqaCG5BozNbdl3UYYJZZMfxPzf3wLzBkAW9LXblq16IkCHv990AjoHIkCl1",' \
                                                     '"connectionName":"gp","paramSetting":[]} '
        resp_preview = requests.request("post",
                                        url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                            'sql_preview'], headers=headers, json=json.loads(payload_preview))
        # print(resp_preview.text)
        sql_str = 'select * from demo.合同事实表 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp_preview.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='sql数据集外面预览结果不正确')

    def test_003(self):
        """外面预览sql数据集"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/packs/{{gp_package}}/tables'
        payload = '{"tableName":"合同事实表","pageIndex":1,"limit":5000,"keyword":""}'
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'db_view_1'] + urllib.parse.quote('合同事实表') + handle_config.conf['tables']['db_view_2'], headers=headers,
                                json=json.loads(payload))
        # print(resp.text)
        sql_str = 'select * from demo.合同事实表 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='sql数据集外面预览结果不正确')

    def test_004(self):
        """编辑里面预览sql数据集"""
        payload = '{"table":{"pack":"'+package_id+'","name":"合同事实表","type":2,"selected":0,' \
                  '"operators":[{"type":12,"value":{"合同签约时间":{"id":"合同事实表_[5408][540c][7b7e][7ea6][65f6][95f4]",' \
                  '"type":48,"usable":true},"注册时间":{"id":"合同事实表_[6ce8][518c][65f6][95f4]","type":48,"usable":true},' \
                  '"合同付款类型":{"id":"合同事实表_[5408][540c][4ed8][6b3e][7c7b][578b]","type":16,"usable":true},' \
                  '"合同id":{"id":"合同事实表_[5408][540c]id","type":16,"usable":true},"合同类型":{"id":"合同事实表_[5408][540c][' \
                  '7c7b][578b]","type":16,"usable":true},"客户id":{"id":"合同事实表_[5ba2][6237]id","type":16,' \
                  '"usable":true},"是否已经交货":{"id":"合同事实表_[662f][5426][5df2][7ecf][4ea4][8d27]","type":16,' \
                  '"usable":true},"购买的产品":{"id":"合同事实表_[8d2d][4e70][7684][4ea7][54c1]","type":32,"usable":true},' \
                  '"购买数量":{"id":"合同事实表_[8d2d][4e70][6570][91cf]","type":32,"usable":true},"合同金额":{"id":"合同事实表_[5408][' \
                  '540c][91d1][989d]","type":32,"usable":true}}}]},"limit":{"pageIndex":1}} '
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'data_view'],headers=headers,json=json.loads(payload))
        sql_str = 'select * from demo.合同事实表 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='结果不正确')

    def test_005(self):
        """测试字段类型，转义"""
        pass
