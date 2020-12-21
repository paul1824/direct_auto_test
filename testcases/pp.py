# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 14:11
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : pp.py
import json
from common.handle_tools import *
import jaydebeapi

# global group_id
# global package_id
# t = '{"success":true,"code":"200","message":"success","data":[{"id":"__my_analysis_group__16f93da3-4d86-4a88-b130-532885da966c1","name":"我的自助数据集","initTime":1608085829544,"packs":[{"id":"__share_me__16f93da3-4d86-4a88-b130-532885da966c1","name":"分享给我的自助数据集","createBy":"1","timeStamp":1608085829616,"usedSpace":0.0,"myAnalysis":true,"tables":[],"editable":true,"shareAnalysis":true,"tableCount":0},{"id":"__my_analysis__16f93da3-4d86-4a88-b130-532885da966c1","name":"1的业务包","createBy":"1","timeStamp":1608085829554,"usedSpace":0.0,"myAnalysis":true,"tables":[],"editable":true,"shareAnalysis":false,"tableCount":0}],"editable":true,"myAnalysis":true,"groups":[]},{"id":"4dc6004e32d24483baca1f0d47e88cc2","name":"GP","initTime":1608195246199,"packs":[{"id":"1b558faea2ad41bcbc7b9b0ab1877f49","name":"GP","createBy":"1","timeStamp":1608195246373,"usedSpace":0.0,"myAnalysis":false,"tables":[],"editable":true,"shareAnalysis":false,"tableCount":0},{"id":"3247b8489ff14b7c9c8f00f845a1d5ce","name":"GP1","createBy":"1","timeStamp":1608195648434,"usedSpace":0.0,"myAnalysis":false,"tables":[],"editable":true,"shareAnalysis":false,"tableCount":0}],"editable":true,"myAnalysis":false,"groups":[]},{"id":"__no_group__d","name":"未分组","initTime":1608085476542,"packs":[],"editable":true,"myAnalysis":false,"groups":[]}],"errorCode":null,"detailErrorMsg":null,"errorMsg":null}'
# d = GetDict(t).getdict()
# # print(d['data'])
# for i, ele_g in enumerate(GetDict(t).getdict()['data']):
#     if ele_g['name'] == 'GP':
#         globals()['group_id'] = ele_g['id']
#         for j, ele_p in enumerate(ele_g['packs']):
#             if ele_p['name'] == 'GP':
#                 globals()['package_id'] = ele_p['id']
# print(group_id, package_id)

# t = '{"success":true,"code":"200","message":"success","data":{"tableTransCount":2,"fieldTransCount":0,"relationsCount":0,"tableAddInfos":[{"originName":"gp_合同事实表_D","success":true,"tableName":"gp_合同事实表_D","info":{"connectionName":"gp","dbTableName":"合同事实表","type":1}},{"originName":"gp_销售明细_D","success":true,"tableName":"gp_销售明细_D","info":{"connectionName":"gp","dbTableName":"销售明细","type":1}}]},"errorCode":null,"detailErrorMsg":null,"errorMsg":null}'
#
# d = GetDict(t).getdict()['data']['tableAddInfos']
# print(d)
# for i , ele in enumerate(d):
#     if ele['originName'] == 'gp_合同事实表_D':
#         print(ele['info']['dbTableName'])

# t = '{"success":true,"code":"200","message":"success","data":{"name":"GP","editable":true,"tables":[{"name":"gp_合同事实表_D","pack":"1b558faea2ad41bcbc7b9b0ab1877f49","myAnalysis":false,"transferName":"gp_合同事实表","usedSpace":0.0,"createBy":"1","editable":true,"selected":0,"initTime":1608262107511,"movable":false,"comment":null,"memorize":false,"tableName":"合同事实表","connectionName":"gp","type":1,"engineType":1},{"name":"gp_销售明细_D","pack":"1b558faea2ad41bcbc7b9b0ab1877f49","myAnalysis":false,"transferName":"gp_销售明细","usedSpace":0.0,"createBy":"1","editable":true,"selected":0,"initTime":1608262107814,"movable":false,"comment":null,"memorize":false,"tableName":"销售明细","connectionName":"gp","type":1,"engineType":1}],"errorTable":[],"missTable":[]},"errorCode":null,"detailErrorMsg":null,"errorMsg":null}'
# d = GetDict(t).getdict()['data']['tables']
# print(d)
# for i,ele in enumerate(GetDict(t).getdict()['data']['tables']):
#     if ele['name']=='gp_合同事实表_D':
#         print(ele['pack'])

# url = 'jdbc:pivotal:greenplum://221.228.203.3:5432;DatabaseName=lance'
# user = 'gpadmin'
# password = 'admin@12345'
# dirver = 'com.pivotal.jdbc.GreenplumDriver'
# jarFile = 'E:\\FineBI517\\webapps\\webroot\\WEB-INF\\lib\\greenplum.jar'
# sqlStr = 'select * from demo.销售明细'
# # conn=jaydebeapi.connect('oracle.jdbc.driver.OracleDriver','jdbc:oracle:thin:@127.0.0.1:1521/orcl',['hwf_model','hwf_model'],'E:/pycharm/lib/ojdbc14.jar')
# conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
# curs = conn.cursor()
# curs.execute(sqlStr)
# desc = curs.description
# for field in desc:
#     print(field[0])
# result = curs.fetchall()
# print(result)
# print(type(result))
# curs.close()
# conn.close()
from collections import Counter

# def countersubset(list1, list2):
#     counter1 = Counter(list1)
#     counter2 = Counter(list2)
#     for k, v in counter1.items():
#         if v > counter2[k]:
#             return False
#     return True


# a = [["2017-09-22 00:00:00", "51011", "D04470", "1", "2", "253", "1,268"],
#      ["2017-09-22 00:00:00", "51011", "D04470", "1", "2", "172", "8,609"]]
a = [["2017-09-22 00:00:00", "51011", "D04470", 1, 2, 253, 1268],
     ["2017-09-22 00:00:00", "51011", "D04470", 1, 2, 172, 8609]]

print([[format(j, ',') if type(j) == int else j for j in i] for i in a])
# b = [("2017-09-22 00:00:00", "51011", "D04470", "1", "2", "253", "1,268"),
#      ("2017-09-22 00:00:00", "51011", "D04470", "1", "2", "172", "8,609"),
#      ("2017-09-22 00:00:00", "51011", "D04470", "1", "2", "552", "1,062")]


# print(type(a[0][4]))
# print(str(format(123, ',')) == "123")

# print(len(a[0]))
# for j in range(0,len(a)):
#     print([str(i) for i in a[j]])
# b = []
# for j in range(0, len(a)):
#     b.append([str(i) for i in a[j]])
# print(b)

# print([[str(j) for j in i] for i in a])
# print(a)
# print(type(a[0][4]))
# b_list = [list(item)for item in b]
# print(b_list)
# def to_list(list1):
#     return [list(item) for item in list1]
#
#
# print(to_list(b))
# print(all(elem in to_list(b) for elem in a))

# a = [1, 2, 3]
# a = [str(i) for i in a]
# print(a)
