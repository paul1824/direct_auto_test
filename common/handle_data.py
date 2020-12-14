# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 11:17
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_data.py.py

import re

from common.handle_config import conf


class EnvData():
    """用来保存动态环境变量数据"""
    loan_id = None
    member_id = None
    token = None


def replace(data):
    """把测试用例中如#phone#、#pwd#等数据替换成conf.ini中对应的数据
    配置文件中没有的数据，从内存中取
    """
    matches = re.finditer('#(.*?)#', data)
    for match in matches:
        s1 = match.group()  # 获取匹配到的整体值 如 #phone#
        try:
            key = match.groups()[0]  # 获取匹配到的第一个组的值  如phone
            s2 = conf['test_data'][key]  # 从配置文件中获取关键字的值，如获取phone的值
        except KeyError as e:
            # 配置文件中没有loan_id，则从EnvData中获取
            s2 = getattr(EnvData, key)
        data = data.replace(s1, str(s2))  # 替换数据，如将测试用例中的 #phone#（s1） 替换成从配置文件读取的phone的值--即s2的值
    return data


if __name__ == '__main__':
    EnvData.loan_id = '1533'
    data = '{"mobile_phone":"#phone#","pwd":"#loan_id#"}'
    print(replace(data))
