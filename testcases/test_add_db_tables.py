# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 13:58
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_db_tables.py

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
        """进入添加db表入口"""
        resp = requests.request("get",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables']['db_conn'],
                                headers=headers)
        print(resp.text)
        if len(GetDict(resp.text).getdict()['data']['connections']) >= 1:
            self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='添加分组不成功')

    def test_002(self):
        """获取数据库的表信息"""
        resp = requests.request("get",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                    'db_get_table_1'] + gp_connection + handle_config.conf['tables']['db_get_table_2'],
                                headers=headers)
        print(resp.text)
        if len(GetDict(resp.text).getdict()['data']) >= 1:
            self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='获取数据库的表信息失败')

    def test_003(self):
        """添加db表"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/packs/{{gp_package}}/tables'
        payload = handle_config.db_payload['gp_db_tables']['gp_add_db_table']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'db_add_table_1'] + package_id + handle_config.conf['tables']['db_add_table_2'], headers=headers,
                                json=json.loads(payload))
        print(resp.text)
        d = GetDict(resp.text).getdict()['data']['tableAddInfos']
        # print(d)
        for i, ele in enumerate(d):
            if ele['originName'] == 'gp_合同事实表_D':
                # print(ele['info']['dbTableName'])
                self.assertEqual(ele['info']['dbTableName'], '合同事实表', msg='加表有问题')
            elif ele['originName'] == 'gp_销售明细_D':
                self.assertEqual(ele['info']['dbTableName'], '销售明细', msg='加表有问题')

    def test_004(self):
        """查看业务包内表信息"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/packs/{{gp_package}}?_=1605679085595'
        resp = requests.request("get", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'db_get_info_1'] + package_id + handle_config.conf['tables']['db_get_info_2'], headers=headers)
        print(resp.text)
        d = GetDict(resp.text).getdict()['data']['tables']
        for i, ele in enumerate(GetDict(resp.text).getdict()['data']['tables']):
            if ele['name'] == 'gp_合同事实表_D':
                self.assertEqual(ele['pack'], package_id, msg='表信息有误')
            elif ele['name'] == 'gp_销售明细_D':
                self.assertEqual(ele['pack'], package_id, msg='表信息有误')

    def test_005(self):
        """预览合同事实表"""
        payload = handle_config.db_payload['gp_db_tables']['gp_view_db_table_contract']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'db_view_1'] + urllib.parse.quote('gp_合同事实表_D') + handle_config.conf['tables']['db_view_2'],
                                headers=headers,
                                json=json.loads(payload))
        sql_str = 'select * from demo.合同事实表 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='结果不正确')
        # print(all(elem in result for elem in d))

    def test_006(self):
        """预览销售明细表"""
        payload = handle_config.db_payload['gp_db_tables']['gp_view_db_table_sales']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'db_view_1'] + urllib.parse.quote('gp_销售明细_D') + handle_config.conf['tables']['db_view_2'], headers=headers,
                                json=json.loads(payload))
        sql_str = 'select * from demo.销售明细 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='结果不正确')
        # print(all(elem in result for elem in d))

    def test_007(self):
        """编辑页面预览合同事实表"""
        payload = handle_config.db_payload['gp_db_tables']['gp_edit_view_db_table_contract']
        # print(type(GetDict(payload).getdict()))
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'data_view'], headers=headers, json=json.loads(payload))
        sql_str = 'select * from demo.合同事实表 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='结果不正确')

    def test_008(self):
        """编辑页面预览销售明细表"""
        payload = handle_config.db_payload['gp_db_tables']['gp_edit_view_db_table_sales']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'data_view'], headers=headers, json=json.loads(payload))
        sql_str = 'select * from demo.销售明细 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='结果不正确')

    def test_009(self):
        """测试字段类型，转义"""
        pass
