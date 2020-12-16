# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 14:11
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : pp.py
import json


# t=r"""{"success":true,"code":"200","message":"success","data":{"id":"b023c8b6e8f34121b96bd822a4cb530d","name":"分组","initTime":1607669735959,"packs":[],"editable":true,"myAnalysis":false,"groups":[]},"errorCode":null,"detailErrorMsg":null,"errorMsg":null}"""
# pp = json.loads(t)
# print(type(pp))
# print(pp['data']['id'])
def getEvent(data):
    try:
        jsonDic = json.loads(data)
    except json.decoder.JSONDecodeError:
        jsonDic = {}
    try:
        dic = dict(jsonDic)
    except TypeError:
        dic = {}
    try:
        event = dic["event"]
    except KeyError:
        event = None
    return dic
t = getEvent('{"success":true,"code":"200","message":"success","data":{"id":"e8a6d5540e414711983cedebd3dba0b7","name":"分组","initTime":1608103532107,"packs":[],"editable":true,"myAnalysis":false,"groups":[]},"errorCode":null,"detailErrorMsg":null,"errorMsg":null}')
print(type(t))