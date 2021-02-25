# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 13:59
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_sql_tables.py

from direct_auto_test.common.handle_db import *
from direct_auto_test.testcases.BaseTestcase import *
import urllib.parse

global gp_connection
global redshift_connection
global group_id
global package_id


class TestAddSqlTables(BaseTestcase):
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
        payload = handle_config.sql_payload['gp_sql_tables']['gp_add_sql_table']
        resp = requests.request("post",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                    'sql_add_table'],
                                headers=headers, json=json.loads(payload.replace("'+package_id+'", package_id)))
        print(resp.text)
        self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='添加sql数据集不成功')

    def test_002(self):
        """修改sql里面预览sql数据集"""
        payload_param = handle_config.sql_payload['gp_sql_tables']['gp_modify_view_sql_table_contract_param']
        resp_param = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'sql_param'], headers=headers, json=json.loads(payload_param.replace("'+package_id+'", package_id)))
        payload_preview = handle_config.sql_payload['gp_sql_tables']['gp_modify_view_sql_table_contract']
        resp_preview = requests.request("post",
                                        url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                            'sql_preview'], headers=headers,
                                        json=json.loads(payload_preview.replace("'+package_id+'", package_id)))
        print(resp_preview.text)
        sql_str = 'select * from demo.合同事实表 '
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        print(resp_param.text)
        self.assertEqual(GetDict(resp_param.text).getdict()['message'], 'success', msg='获取sql数据集参数失败')
        self.assertEqual(len(GetDict(resp_param.text).getdict()['data']['params']), 0, msg='获取参数个数正确')

        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp_preview.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='sql数据集外面预览结果不正确')

    def test_003(self):
        """外面预览sql数据集"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/packs/{{gp_package}}/tables'
        payload = handle_config.sql_payload['gp_sql_tables']['gp_view_sql_table_contract']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'db_view_1'] + urllib.parse.quote('合同事实表') + handle_config.conf['tables']['db_view_2'], headers=headers,
                                json=json.loads(payload.replace("'+package_id+'", package_id)))
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
        payload = handle_config.sql_payload['gp_sql_tables']['gp_edit_view_sql_table_contract']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'data_view'], headers=headers, json=json.loads(payload.replace("'+package_id+'", package_id)))
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
