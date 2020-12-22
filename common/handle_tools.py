# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:39
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_tools.py
import json
from collections import Counter
from jpype import java


class GetDict():
    """转json格式"""

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


def count_subset(list1, list2):
    """判断list1中的元素是否属于list2，考虑重复的元素，但是此函数不支持多维数据结构"""
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    for k, v in counter1.items():
        if v > counter2[k]:
            return False
    return True


def to_list(list1):
    """将list中的tuple转成list,用于处理数据库查询出的数据"""
    return [list(item) for item in list1]


def list_str(list1):
    """处理数据库中的结果为str类型，方便与json数据做比对"""
    # return [[str(j) for j in i] for i in list1]
    return [[format(j, ',') if type(j) == java.lang.Integer else j for j in i] for i in list1]
