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
