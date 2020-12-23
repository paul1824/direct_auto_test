# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 17:05
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_analysis_merge_up_down.py

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
        """添加自助数据集"""
        payload = '{"name":"gp_自助数据集_上下合并","myAnalysis":false,"operators":[{"type":1,"value":[{"field":"gp[5f]合同事实表[' \
                  '5f]D_[8d2d][4e70][7684][4ea7][54c1]","tableName":"gp_合同事实表_D",' \
                  '"pack":{"id":"'+package_id+'"},"path":[],"commonTable":["gp_合同事实表_D"],' \
                  '"selectFieldId":"自助数据集_[8d2d][4e70][7684][4ea7][54c1]","group":0},{"field":"gp[5f]合同事实表[5f]D_[' \
                  '8d2d][4e70][6570][91cf]","tableName":"gp_合同事实表_D","pack":{' \
                  '"id":"'+package_id+'"},"path":[],"commonTable":["gp_合同事实表_D"],' \
                  '"selectFieldId":"自助数据集_[8d2d][4e70][6570][91cf]","group":0},{"field":"gp[5f]合同事实表[5f]D_[5408][' \
                  '540c][91d1][989d]","tableName":"gp_合同事实表_D","pack":{"id":"'+package_id+'"},' \
                  '"path":[],"commonTable":["gp_合同事实表_D"],"selectFieldId":"自助数据集_[5408][540c][91d1][989d]",' \
                  '"group":0},{"field":"gp[5f]合同事实表[5f]D_[5408][540c]id","tableName":"gp_合同事实表_D",' \
                  '"pack":{"id":"'+package_id+'"},"path":[],"commonTable":["gp_合同事实表_D"],' \
                  '"selectFieldId":"自助数据集_[5408][540c]id","group":0},{"field":"gp[5f]合同事实表[5f]D_[5408][540c][4ed8][' \
                  '6b3e][7c7b][578b]","tableName":"gp_合同事实表_D","pack":{"id":"'+package_id+'"},' \
                  '"path":[],"commonTable":["gp_合同事实表_D"],"selectFieldId":"自助数据集_[5408][540c][4ed8][6b3e][7c7b][' \
                  '578b]","group":0},{"field":"gp[5f]合同事实表[5f]D_[5408][540c][7c7b][578b]","tableName":"gp_合同事实表_D",' \
                  '"pack":{"id":"'+package_id+'"},"path":[],"commonTable":["gp_合同事实表_D"],' \
                  '"selectFieldId":"自助数据集_[5408][540c][7c7b][578b]","group":0},{"field":"gp[5f]合同事实表[5f]D_[5ba2][' \
                  '6237]id","tableName":"gp_合同事实表_D","pack":{"id":"'+package_id+'"},"path":[],' \
                  '"commonTable":["gp_合同事实表_D"],"selectFieldId":"自助数据集_[5ba2][6237]id","group":0},{"field":"gp[' \
                  '5f]合同事实表[5f]D_[662f][5426][5df2][7ecf][4ea4][8d27]","tableName":"gp_合同事实表_D",' \
                  '"pack":{"id":"'+package_id+'"},"path":[],"commonTable":["gp_合同事实表_D"],' \
                  '"selectFieldId":"自助数据集_[662f][5426][5df2][7ecf][4ea4][8d27]","group":0},{"field":"gp[5f]合同事实表[' \
                  '5f]D_[5408][540c][7b7e][7ea6][65f6][95f4]","tableName":"gp_合同事实表_D",' \
                  '"pack":{"id":"'+package_id+'"},"path":[],"commonTable":["gp_合同事实表_D"],' \
                  '"selectFieldId":"自助数据集_[5408][540c][7b7e][7ea6][65f6][95f4]","group":0},{"field":"gp[5f]合同事实表[' \
                  '5f]D_[6ce8][518c][65f6][95f4]","tableName":"gp_合同事实表_D","pack":{' \
                  '"id":"'+package_id+'"},"path":[],"commonTable":["gp_合同事实表_D"],' \
                  '"selectFieldId":"自助数据集_[6ce8][518c][65f6][95f4]","group":0}],"routersMap":{}},{"type":3,' \
                  '"customName":"上下合并","comment":"","value":{"tables":[{"name":"__current_table__",' \
                  '"transferName":"__current_table__","type":4,"fields":[{"id":"自助数据集_[8d2d][4e70][7684][4ea7][' \
                  '54c1]","name":"购买的产品","transferName":"购买的产品","type":32,"enable":true,"usable":true},{"id":"自助数据集_[' \
                  '8d2d][4e70][6570][91cf]","name":"购买数量","transferName":"购买数量","type":32,"enable":true,' \
                  '"usable":true},{"id":"自助数据集_[5408][540c][91d1][989d]","name":"合同金额","transferName":"合同金额",' \
                  '"type":32,"enable":true,"usable":true},{"id":"自助数据集_[5408][540c]id","name":"合同id",' \
                  '"transferName":"合同id","type":16,"enable":true,"usable":true},{"id":"自助数据集_[5408][540c][4ed8][' \
                  '6b3e][7c7b][578b]","name":"合同付款类型","transferName":"合同付款类型","type":16,"enable":true,"usable":true},' \
                  '{"id":"自助数据集_[5408][540c][7c7b][578b]","name":"合同类型","transferName":"合同类型","type":16,' \
                  '"enable":true,"usable":true},{"id":"自助数据集_[5ba2][6237]id","name":"客户id","transferName":"客户id",' \
                  '"type":16,"enable":true,"usable":true},{"id":"自助数据集_[662f][5426][5df2][7ecf][4ea4][8d27]",' \
                  '"name":"是否已经交货","transferName":"是否已经交货","type":16,"enable":true,"usable":true},{"id":"自助数据集_[' \
                  '5408][540c][7b7e][7ea6][65f6][95f4]","name":"合同签约时间","transferName":"合同签约时间","type":48,' \
                  '"enable":true,"usable":true},{"id":"自助数据集_[6ce8][518c][65f6][95f4]","name":"注册时间",' \
                  '"transferName":"注册时间","type":48,"enable":true,"usable":true}],"fieldsMap":{"自助数据集_[8d2d][4e70][' \
                  '7684][4ea7][54c1]":"购买的产品","自助数据集_[8d2d][4e70][6570][91cf]":"购买数量","自助数据集_[5408][540c][91d1][' \
                  '989d]":"合同金额","自助数据集_[5408][540c]id":"合同id","自助数据集_[5408][540c][4ed8][6b3e][7c7b][578b]":"合同付款类型",' \
                  '"自助数据集_[5408][540c][7c7b][578b]":"合同类型","自助数据集_[5ba2][6237]id":"客户id","自助数据集_[662f][5426][5df2][' \
                  '7ecf][4ea4][8d27]":"是否已经交货","自助数据集_[5408][540c][7b7e][7ea6][65f6][95f4]":"合同签约时间","自助数据集_[6ce8][' \
                  '518c][65f6][95f4]":"注册时间"}},{"name":"gp_合同事实表_D","transferName":"gp_合同事实表","type":1,"fields":[{' \
                  '"id":"gp[5f]合同事实表[5f]D_[5408][540c][7b7e][7ea6][65f6][95f4]","name":"合同签约时间",' \
                  '"transferName":"合同签约时间","type":48,"enable":true,"usable":true},{"id":"gp[5f]合同事实表[5f]D_[6ce8][' \
                  '518c][65f6][95f4]","name":"注册时间","transferName":"注册时间","type":48,"enable":true,"usable":true},' \
                  '{"id":"gp[5f]合同事实表[5f]D_[5408][540c][4ed8][6b3e][7c7b][578b]","name":"合同付款类型",' \
                  '"transferName":"合同付款类型","type":16,"enable":true,"usable":true},{"id":"gp[5f]合同事实表[5f]D_[5408][' \
                  '540c]id","name":"合同id","transferName":"合同id","type":16,"enable":true,"usable":true},' \
                  '{"id":"gp[5f]合同事实表[5f]D_[5408][540c][7c7b][578b]","name":"合同类型","transferName":"合同类型","type":16,' \
                  '"enable":true,"usable":true},{"id":"gp[5f]合同事实表[5f]D_[5ba2][6237]id","name":"客户id",' \
                  '"transferName":"客户id","type":16,"enable":true,"usable":true},{"id":"gp[5f]合同事实表[5f]D_[662f][5426][' \
                  '5df2][7ecf][4ea4][8d27]","name":"是否已经交货","transferName":"是否已经交货","type":16,"enable":true,' \
                  '"usable":true},{"id":"gp[5f]合同事实表[5f]D_[8d2d][4e70][7684][4ea7][54c1]","name":"购买的产品",' \
                  '"transferName":"购买的产品","type":32,"enable":true,"usable":true},{"id":"gp[5f]合同事实表[5f]D_[8d2d][' \
                  '4e70][6570][91cf]","name":"购买数量","transferName":"购买数量","type":32,"enable":true,"usable":true},' \
                  '{"id":"gp[5f]合同事实表[5f]D_[5408][540c][91d1][989d]","name":"合同金额","transferName":"合同金额","type":32,' \
                  '"enable":true,"usable":true}],"fieldsMap":{"gp[5f]合同事实表[5f]D_[5408][540c][7b7e][7ea6][65f6][' \
                  '95f4]":"合同签约时间","gp[5f]合同事实表[5f]D_[6ce8][518c][65f6][95f4]":"注册时间","gp[5f]合同事实表[5f]D_[5408][540c][' \
                  '4ed8][6b3e][7c7b][578b]":"合同付款类型","gp[5f]合同事实表[5f]D_[5408][540c]id":"合同id","gp[5f]合同事实表[5f]D_[' \
                  '5408][540c][7c7b][578b]":"合同类型","gp[5f]合同事实表[5f]D_[5ba2][6237]id":"客户id","gp[5f]合同事实表[5f]D_[662f][' \
                  '5426][5df2][7ecf][4ea4][8d27]":"是否已经交货","gp[5f]合同事实表[5f]D_[8d2d][4e70][7684][4ea7][54c1]":"购买的产品",' \
                  '"gp[5f]合同事实表[5f]D_[8d2d][4e70][6570][91cf]":"购买数量","gp[5f]合同事实表[5f]D_[5408][540c][91d1][' \
                  '989d]":"合同金额"}}],"basis":[["自助数据集_[8d2d][4e70][7684][4ea7][54c1]","自助数据集_[8d2d][4e70][6570][' \
                  '91cf]","自助数据集_[5408][540c][91d1][989d]","自助数据集_[5408][540c]id","自助数据集_[5408][540c][4ed8][6b3e][' \
                  '7c7b][578b]","自助数据集_[5408][540c][7c7b][578b]","自助数据集_[5ba2][6237]id","自助数据集_[662f][5426][5df2][' \
                  '7ecf][4ea4][8d27]","自助数据集_[5408][540c][7b7e][7ea6][65f6][95f4]","自助数据集_[6ce8][518c][65f6][95f4]"],' \
                  '["gp[5f]合同事实表[5f]D_[8d2d][4e70][7684][4ea7][54c1]","gp[5f]合同事实表[5f]D_[8d2d][4e70][6570][91cf]",' \
                  '"gp[5f]合同事实表[5f]D_[5408][540c][91d1][989d]","gp[5f]合同事实表[5f]D_[5408][540c]id","gp[5f]合同事实表[5f]D_[' \
                  '5408][540c][4ed8][6b3e][7c7b][578b]","gp[5f]合同事实表[5f]D_[5408][540c][7c7b][578b]","gp[5f]合同事实表[' \
                  '5f]D_[5ba2][6237]id","gp[5f]合同事实表[5f]D_[662f][5426][5df2][7ecf][4ea4][8d27]","gp[5f]合同事实表[5f]D_[' \
                  '5408][540c][7b7e][7ea6][65f6][95f4]","gp[5f]合同事实表[5f]D_[6ce8][518c][65f6][95f4]"]],"result":[{' \
                  '"type":32,"name":"购买的产品","transferName":"购买的产品"},{"type":32,"name":"购买数量","transferName":"购买数量"},' \
                  '{"type":32,"name":"合同金额","transferName":"合同金额"},{"type":16,"name":"合同id","transferName":"合同id"},' \
                  '{"type":16,"name":"合同付款类型","transferName":"合同付款类型"},{"type":16,"name":"合同类型",' \
                  '"transferName":"合同类型"},{"type":16,"name":"客户id","transferName":"客户id"},{"type":16,"name":"是否已经交货",' \
                  '"transferName":"是否已经交货"},{"type":48,"name":"合同签约时间","transferName":"合同签约时间"},{"type":48,' \
                  '"name":"注册时间","transferName":"注册时间"}],"selectFieldMap":{"自助数据集_[8d2d][4e70][7684][4ea7][' \
                  '54c1]":"自助数据集_[8d2d][4e70][7684][4ea7][54c1]","自助数据集_[8d2d][4e70][6570][91cf]":"自助数据集_[8d2d][' \
                  '4e70][6570][91cf]","自助数据集_[5408][540c][91d1][989d]":"自助数据集_[5408][540c][91d1][989d]",' \
                  '"自助数据集_[5408][540c]id":"自助数据集_[5408][540c]id","自助数据集_[5408][540c][4ed8][6b3e][7c7b][' \
                  '578b]":"自助数据集_[5408][540c][4ed8][6b3e][7c7b][578b]","自助数据集_[5408][540c][7c7b][578b]":"自助数据集_[' \
                  '5408][540c][7c7b][578b]","自助数据集_[5ba2][6237]id":"自助数据集_[5ba2][6237]id","自助数据集_[662f][5426][5df2][' \
                  '7ecf][4ea4][8d27]":"自助数据集_[662f][5426][5df2][7ecf][4ea4][8d27]","自助数据集_[5408][540c][7b7e][7ea6][' \
                  '65f6][95f4]":"自助数据集_[5408][540c][7b7e][7ea6][65f6][95f4]","自助数据集_[6ce8][518c][65f6][' \
                  '95f4]":"自助数据集_[6ce8][518c][65f6][95f4]"}}}],"transferName":"gp_自助数据集_上下合并","usedSpace":0,' \
                  '"editable":false,"selected":0,"initTime":0,"movable":false,"comment":null,' \
                  '"inheritPermissionAndRelation":false,"extractDataSetting":3,"extractData":false,' \
                  '"dataAnalysis":false,"shareBy":"","shared":false,"shareToMe":false,"resultToIdentifyNameMap":{},' \
                  '"type":4,"engineType":1,"previewCalLimit":2,"pack":"'+package_id+'",' \
                  '"fieldsMap":{"自助数据集_[8d2d][4e70][7684][4ea7][54c1]":"购买的产品","自助数据集_[8d2d][4e70][6570][' \
                  '91cf]":"购买数量","自助数据集_[5408][540c][91d1][989d]":"合同金额","自助数据集_[5408][540c]id":"合同id","自助数据集_[5408][' \
                  '540c][4ed8][6b3e][7c7b][578b]":"合同付款类型","自助数据集_[5408][540c][7c7b][578b]":"合同类型","自助数据集_[5ba2][' \
                  '6237]id":"客户id","自助数据集_[662f][5426][5df2][7ecf][4ea4][8d27]":"是否已经交货","自助数据集_[5408][540c][7b7e][' \
                  '7ea6][65f6][95f4]":"合同签约时间","自助数据集_[6ce8][518c][65f6][95f4]":"注册时间"},"validStatus":"VALID"} '
        resp = requests.request("post",
                                url=handle_config.conf['BI_API']['finebi'] + handle_config.conf['tables'][
                                    'analysis_add_table'],
                                headers=headers, json=json.loads(payload))
        print(resp.text)
        self.assertEqual(GetDict(resp.text).getdict()['message'], 'success', msg='自助数据集上下合并有问题')