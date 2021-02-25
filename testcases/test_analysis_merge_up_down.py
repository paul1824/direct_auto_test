# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 17:05
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_analysis_merge_up_down.py

from direct_auto_test.common.handle_db import *
from direct_auto_test.testcases.BaseTestcase import *
import urllib.parse

global gp_connection
global redshift_connection
global group_id
global package_id


class TestAddAnalysisMergeUpDownTables(BaseTestcase):
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
        payload = payload = handle_config.analysis_payload['gp_analysis_merge_up_down'][
            'gp_add_analysis_merge_up_down_table']
        resp = requests.request("post",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                    'analysis_add_table'],
                                headers=headers, json=json.loads(payload.replace("'+package_id+'",package_id)))
        print(resp.text)
        self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='自助数据集上下合并有问题')
