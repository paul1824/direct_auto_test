# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 20:17
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_analysis_tables.py

from common.handle_db import *
from testcases.BaseTestcase import *
import urllib.parse

global gp_connection
global redshift_connection
global group_id
global package_id


class TestAddAnalysisTables(BaseTestcase):
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
        """添加自助数据集"""
        payload = handle_config.analysis_payload['gp_analysis_tables']['gp_add_analysis_table']
        resp = requests.request("post",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                    'analysis_add_table'],
                                headers=headers, json=json.loads(payload.replace("'+package_id+'", package_id)))
        print(resp.text)
        # self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='添加自助数据集不成功')

    def test_002(self):
        """编辑里面预览自助数据集"""
        payload = handle_config.analysis_payload['gp_analysis_tables']['gp_edit_view_analysis_table_contract']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'analysis_view'], headers=headers, json=json.loads(payload.replace("'+package_id+'", package_id)))
        sql_str = 'select "购买的产品" , "购买数量" , "合同金额" , "合同id" , "合同付款类型" , "合同类型" , "客户id" , "是否已经交货" , "合同签约时间" , ' \
                  '"注册时间" from "demo"."合同事实表"'
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        # print([[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in result])
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='结果不正确')

    def test_003(self):
        """外面预览自助数据集"""
        # url = 'http://localhost:37799/webroot/decision/v5/direct/conf/packs/{{gp_package}}/tables'
        payload = handle_config.analysis_payload['gp_analysis_tables']['gp_view_analysis_table_contract']
        resp = requests.request("post", url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
            'db_view_1'] + urllib.parse.quote('gp_自助数据集') + handle_config.conf['tables']['db_view_2'], headers=headers,
                                json=json.loads(payload.replace("'+package_id+'", package_id)))
        sql_str = 'select "购买的产品" , "购买数量" , "合同金额" , "合同id" , "合同付款类型" , "合同类型" , "客户id" , "是否已经交货" , "合同签约时间" , ' \
                  '"注册时间" from "demo"."合同事实表"'
        conn = GPHandle()
        result = list_str(to_list(conn.find_all(sql_str)))
        conn.close()
        d = GetDict(resp.text).getdict()['data']['data']
        self.assertIs(all(elem in result for elem in d), True, msg='自助数据集外面预览结果不正确')
