# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:39
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_tools.py
import json


class GetDict():
    def __init__(self, data):
        self.data = data

    def getdict(self):
        try:
            jsonDic = json.loads(self.data)
        except json.decoder.JSONDecodeError:
            jsonDic = {}
        try:
            dic = dict(jsonDic)
        except TypeError:
            dic = {}
        return dic

t=GetDict('{"success":true,"code":"200","message":"success","data":{"id":"e8a6d5540e414711983cedebd3dba0b7","name":"分组","initTime":1608103532107,"packs":[],"editable":true,"myAnalysis":false,"groups":[]},"errorCode":null,"detailErrorMsg":null,"errorMsg":null}').getjson()
print(t)