# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 15:17
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : resetcode.py.py
import os
import shutil
import zipfile

"""重置配置文件"""
shutil.rmtree(r"E:\\FineBIhh\\webapps\\webroot\\WEB-INF\\embed\\finedb")


def unzip_file(zip_src, dst_dir):
    """ src_dir：你要压缩的文件夹的路径
        zip_name：压缩后zip文件的路径及名称"""
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


unzip_file(r"E:\pp\PycharmProjects\direct_auto_test\file\finedb.zip",
           r"E:\\FineBIhh\\webapps\\webroot\\WEB-INF\\embed")

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
print(p)
