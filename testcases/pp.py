# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 14:11
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : pp.py
import json
from common.handle_tools import *

# t=r"""{"success":true,"code":"200","message":"success","data":{"id":"b023c8b6e8f34121b96bd822a4cb530d","name":"分组","initTime":1607669735959,"packs":[],"editable":true,"myAnalysis":false,"groups":[]},"errorCode":null,"detailErrorMsg":null,"errorMsg":null}"""
# pp = json.loads(t)
# print(type(pp))
# print(pp['data']['id'])

t='{"success":true,"code":"200","message":"success","data":[{"id":"21ac9f7a128c4c32a0d693adfcaa285b","name":"GP","initTime":1608110615646,"packs":[],"editable":true,"myAnalysis":false,"groups":[]},{"id":"__my_analysis_group__16f93da3-4d86-4a88-b130-532885da966c1","name":"我的自助数据集","initTime":1608085829544,"packs":[{"id":"__share_me__16f93da3-4d86-4a88-b130-532885da966c1","name":"分享给我的自助数据集","createBy":"1","timeStamp":1608085829616,"usedSpace":0.0,"myAnalysis":true,"tables":[],"editable":true,"shareAnalysis":true,"tableCount":0},{"id":"__my_analysis__16f93da3-4d86-4a88-b130-532885da966c1","name":"1的业务包","createBy":"1","timeStamp":1608085829554,"usedSpace":0.0,"myAnalysis":true,"tables":[],"editable":true,"shareAnalysis":false,"tableCount":0}],"editable":true,"myAnalysis":true,"groups":[]},{"id":"__no_group__d","name":"未分组","initTime":1608085476542,"packs":[],"editable":true,"myAnalysis":false,"groups":[]}],"errorCode":null,"detailErrorMsg":null,"errorMsg":null}'

# for i in GetDict(t).getdict()['data']:
#     if GetDict(t).getdict()['data'][1]['name']=='GP':
#
#         print(GetDict(t).getdict()['data'][i]['id'])
# print(GetDict(t).getdict()['data'][1]['name'])
print(type(GetDict(t).getdict()['data']))