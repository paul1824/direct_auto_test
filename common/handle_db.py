# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 19:50
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_db.py.py

"""
需要安装pymysql:  pip install jaydebeapi
"""

import jaydebeapi
from common import handle_config


class GPHandle():
    """操作gp数据库的类"""

    def __init__(self):
        """初始化方法中，连接到数据库"""
        # 建立连接
        self.con = jaydebeapi.connect(handle_config.result_db['gp']['driver'], handle_config.result_db['gp']['url'],
                                      [handle_config.result_db['gp']['user'],
                                       handle_config.result_db['gp']['password']],
                                      handle_config.result_db['gp']['jarFile'])
        # 创建一个游标对象
        self.cur = self.con.cursor()

    def find_all(self, sql):
        """
        查询sql语句返回的所有数据
        :param sql: 查询的sql
        :return: 查询到的所有数据
        """
        self.con.commit()  # 提交事务， 为了同步数据。
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_one(self, sql):
        """
        查询sql语句返回的第一条数据
        :param sql: 查询的sql
        :type sql:str
        :return: sql语句查询到的第一条数据
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_count(self, sql):
        """
        sql语句查询到的数据条数
        :param sql: 查询的sql
        :return:查询到的数据条数
        """
        self.con.commit()
        sql = sql
        res = self.cur.execute(sql)
        return res

    def update(self, sql):
        """
        增删改操作的方法
        :param sql: 增删改的sql语句
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        """断开游标，关闭连接"""
        self.cur.close()
        self.con.close()


class RedshiftHandle():
    """操作redshift数据库的类"""

    def __init__(self):
        """初始化方法中，连接到数据库"""
        # 建立连接
        self.con = jaydebeapi.connect(handle_config.result_db['redshift']['driver'],
                                      handle_config.result_db['redshift']['url'],
                                      [handle_config.result_db['redshift']['user'],
                                       handle_config.result_db['redshift']['password']],
                                      handle_config.result_db['redshift']['jarFile'])
        # 创建一个游标对象
        self.cur = self.con.cursor()

    def find_all(self, sql):
        """
        查询sql语句返回的所有数据
        :param sql: 查询的sql
        :return: 查询到的所有数据
        """
        self.con.commit()  # 提交事务， 为了同步数据。
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_one(self, sql):
        """
        查询sql语句返回的第一条数据
        :param sql: 查询的sql
        :type sql:str
        :return: sql语句查询到的第一条数据
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_count(self, sql):
        """
        sql语句查询到的数据条数
        :param sql: 查询的sql
        :return:查询到的数据条数
        """
        self.con.commit()
        sql = sql
        res = self.cur.execute(sql)
        return res

    def update(self, sql):
        """
        增删改操作的方法
        :param sql: 增删改的sql语句
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        """断开游标，关闭连接"""
        self.cur.close()
        self.con.close()

# if __name__ == '__main__':
#     db = RedshiftHandle()
#     sql = 'SELECT * FROM public.销售明细'
#     print(sql)
#     res = db.find_all(sql)  # 看有几个类别为1的记录
#     print(res)
#     db.close()
