# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 15:17
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : resetcode.py.py
import os

"""需要执行完init后，重启工程完成后执行此文件，执行完后再次重启工程"""
fp = open("E:\\FineBIhh\\webapps\\webroot\\WEB-INF\\embed\\finedb\\db.log", 'a+')
sql_1 = r"""DELETE FROM FINE_CONF_ENTITY WHERE ID='SecurityConfig.frontSeed'"""
sql_2 = r"""DELETE FROM FINE_CONF_ENTITY WHERE ID='SecurityConfig.sm4Key'"""
sql_3 = r"""INSERT INTO FINE_CONF_ENTITY VALUES('SecurityConfig.frontSeed','XfNsQaYJvsUuwKBH')"""
sql_4 = r"""INSERT INTO FINE_CONF_ENTITY VALUES('SecurityConfig.sm4Key','56f011dd86bf70af7687314fd129851b')"""
fp.write(sql_1)
fp.write('\n')
fp.write(sql_2)
fp.write('\n')
fp.write(sql_3)
fp.write('\n')
fp.write(sql_4)
fp.write('\n')
fp.write('COMMIT')
fp.close()
p = os.listdir('E:\\FineBIhh\\webapps\\webroot\\WEB-INF\\embed\\finedb\\')
