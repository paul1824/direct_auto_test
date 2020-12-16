# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 10:42
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_login.py

from testcases.BaseTestcase import *

# headers = {'Authorization': BaseTestcase().get_token(),'Content-Type': 'application/json'}


class TestLogin(BaseTestcase):
    def test_001(self):
        '''测试登录是否成功'''
        Authorization = self.get_token()
        print(Authorization)
        self.assertTrue(Authorization)
    def test_002(self):
        '''测试获取数据连接信息'''
        url = 'http://localhost:37799/webroot/decision/v10/config/connection/list'
        # headers = {'Authorization': self.get_token()}
        resp = requests.request("get", url, headers=headers)
        print(resp.text)
        self.assertIn('data', resp.text)

    # def test_003(self):
    #     '''测试数据连接_gp'''
    #     url = 'http://localhost:37799/webroot/decision/v10/config/connection/test'
    #     payload = r"""{"connectionType":"jdbc","connectionName":"GP","connectionData":"{\"connectionId\":null,\"database\":\"pivotal-greenplum-database\",\"connectionName\":null,\"driver\":\"com.pivotal.jdbc.GreenplumDriver\",\"url\":\"jdbc:pivotal:greenplum://221.228.203.3:5432;DatabaseName=lance\",\"user\":\"gpadmin\",\"password\":\"********\",\"newCharsetName\":\"\",\"originalCharsetName\":\"\",\"schema\":\"demo\",\"options\":null,\"port\":0,\"authType\":\"\",\"creator\":\"1\",\"principal\":\"\",\"keyPath\":\"\",\"connectionPoolAttr\":{\"initialSize\":0,\"maxActive\":50,\"maxIdle\":10,\"minIdle\":0,\"maxWait\":10000,\"validationQuery\":\"\",\"testOnBorrow\":true,\"testOnReturn\":false,\"testWhileIdle\":false,\"timeBetweenEvictionRunsMillis\":-1,\"numTestsPerEvictionRun\":3,\"minEvictableIdleTimeMillis\":1800},\"privilegeDetailBeanList\":null}","connectionId":null,"creator":"1","privilegeDetailBeanList":null}"""
    #     resp = requests.request("post", url=url,  headers=headers,data=payload)
    #     print(resp.text)
    #     self.assertIn('data', resp.text)
    #
    # def test_004(self):
    #     '''gp添加分组'''
    #     url = 'http://localhost:37799/webroot/decision/v5/direct/conf/groups/__root_group__'
    #     resp = requests.request("post",url=url,headers=headers)
    #     print(json.loads(resp.text)['data'])
    #     self.assertIn('data',resp.text)

{"connectionType":"jdbc","connectionId":"gp","connectionName":"gp","connectionData":"{\"database\":\"pivotal-greenplum-database\",\"connectionName\":\"gp\",\"driver\":\"org.postgresql.Driver\",\"url\":\"jdbc:postgresql://221.228.203.3:5432/lance\",\"user\":\"lance_admin\",\"password\":\"j4it3itufV5syoIs+ivkOQ==\",\"queryType\":\"\",\"newCharsetName\":\"\",\"originalCharsetName\":\"\",\"schema\":\"demo\",\"host\":\"221.228.203.3\",\"authType\":\"\",\"creator\":\"1\",\"principal\":\"\",\"keyPath\":\"\",\"connectionPoolAttr\":{\"initialSize\":\"0\",\"maxActive\":\"50\",\"maxIdle\":\"10\",\"minIdle\":\"0\",\"maxWait\":\"10000\",\"validationQuery\":\"\",\"testOnBorrow\":true,\"testOnReturn\":false,\"testWhileIdle\":false,\"timeBetweenEvictionRunsMillis\":\"-1\",\"numTestsPerEvictionRun\":\"3\",\"minEvictableIdleTimeMillis\":\"1800\"}}","creator":"1"}
