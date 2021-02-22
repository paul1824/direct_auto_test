# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 15:22
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : test_add_connection.py
from testcases.BaseTestcase import *

global gp_connection
global redshift_connection


class TestAddConnection(BaseTestcase):
    def test_001(self):
        """获取数据连接列表"""
        res = requests.request("get",
                               url=handle_config.conf['BI_API']['dec'] + handle_config.conf['connection']['list'],
                               headers=headers)
        # data = json.dumps(res.text)
        data = eval(res.text)
        print('预期结果是：', [])
        print('实际结果是：', data['data'])
        self.assertEqual(data['data'], [], msg='获取数据连接列表失败')

    def test_002(self):
        """添加数据连接_gp"""
        payload_add = r"""{"connectionType":"jdbc","connectionId":"gp","connectionName":"gp","connectionData":"{\"database\":\"pivotal-greenplum-database\",\"connectionName\":\"gp\",\"driver\":\"com.pivotal.jdbc.GreenplumDriver\",\"url\":\"jdbc:pivotal:greenplum://221.228.203.3:5432;DatabaseName=lance\",\"user\":\"gpadmin\",\"password\":\"gX0Ujo3FI0gddX2OWhqLOg==\",\"queryType\":\"\",\"newCharsetName\":\"\",\"originalCharsetName\":\"\",\"schema\":\"demo\",\"host\":\"221.228.203.3\",\"authType\":\"\",\"creator\":\"1\",\"principal\":\"\",\"keyPath\":\"\",\"connectionPoolAttr\":{\"initialSize\":\"0\",\"maxActive\":\"50\",\"maxIdle\":\"10\",\"minIdle\":\"0\",\"maxWait\":\"10000\",\"validationQuery\":\"\",\"testOnBorrow\":true,\"testOnReturn\":false,\"testWhileIdle\":false,\"timeBetweenEvictionRunsMillis\":\"-1\",\"numTestsPerEvictionRun\":\"3\",\"minEvictableIdleTimeMillis\":\"1800\"}}","creator":"1"}"""
        payload_test = r"""{"connectionType":"jdbc","connectionName":"gp","connectionData":"{\"connectionId\":null,\"database\":\"pivotal-greenplum-database\",\"connectionName\":null,\"driver\":\"com.pivotal.jdbc.GreenplumDriver\",\"url\":\"jdbc:pivotal:greenplum://221.228.203.3:5432;DatabaseName=lance\",\"user\":\"gpadmin\",\"password\":\"********\",\"newCharsetName\":\"\",\"originalCharsetName\":\"\",\"schema\":\"demo\",\"options\":null,\"port\":0,\"authType\":\"\",\"creator\":\"1\",\"principal\":\"\",\"keyPath\":\"\",\"connectionPoolAttr\":{\"initialSize\":0,\"maxActive\":50,\"maxIdle\":10,\"minIdle\":0,\"maxWait\":10000,\"validationQuery\":\"\",\"testOnBorrow\":true,\"testOnReturn\":false,\"testWhileIdle\":false,\"timeBetweenEvictionRunsMillis\":-1,\"numTestsPerEvictionRun\":3,\"minEvictableIdleTimeMillis\":1800},\"privilegeDetailBeanList\":null}","connectionId":null,"creator":"1","privilegeDetailBeanList":null}"""
        res_add = requests.request("post",
                                   url=handle_config.conf['BI_API']['dec'] + handle_config.conf['connection']['add'],
                                   headers=headers, data=payload_add)
        res_test = requests.request("post",
                                    url=handle_config.conf['BI_API']['dec'] + handle_config.conf['connection']['test'],
                                    headers=headers,data= payload_test)
        data_add = eval(res_add.text)
        data_test = eval(res_test.text)
        print(data_test)
        print(data_add)
        self.assertEqual(data_add['data'], 'success', msg='添加gp数据连接失败')
        self.assertIn('data', data_test, msg='gp测试连接失败')

    def test_003(self):
        """添加数据连接_redshift"""
        payload_add = r"""{"connectionType":"jdbc","connectionId":"redshift","connectionName":"redshift","connectionData":"{\"database\":\"amazon-redshift\",\"connectionName\":\"redshift\",\"driver\":\"com.amazon.redshift.jdbc41.Driver\",\"url\":\"jdbc:redshift://bi.c7dujbchptgb.cn-north-1.redshift.amazonaws.com.cn:5439/bi\",\"user\":\"awuser\",\"password\":\"Em0SxuBfrc7Xjtxs8JjqsQ==\",\"queryType\":\"\",\"newCharsetName\":\"\",\"originalCharsetName\":\"\",\"host\":\"bi.c7dujbchptgb.cn-north-1.redshift.amazonaws.com.cn\",\"authType\":\"\",\"creator\":\"1\",\"principal\":\"\",\"keyPath\":\"\",\"connectionPoolAttr\":{\"initialSize\":\"0\",\"maxActive\":\"50\",\"maxIdle\":\"10\",\"minIdle\":\"0\",\"maxWait\":\"10000\",\"validationQuery\":\"\",\"testOnBorrow\":true,\"testOnReturn\":false,\"testWhileIdle\":false,\"timeBetweenEvictionRunsMillis\":\"-1\",\"numTestsPerEvictionRun\":\"3\",\"minEvictableIdleTimeMillis\":\"1800\"}}","creator":"1"}"""
        payload_test = r"""{"connectionType":"jdbc","connectionName":"redshift","connectionData":"{\"connectionId\":null,\"database\":\"amazon-redshift\",\"connectionName\":null,\"driver\":\"com.amazon.redshift.jdbc41.Driver\",\"url\":\"jdbc:redshift://bi.c7dujbchptgb.cn-north-1.redshift.amazonaws.com.cn:5439/bi\",\"user\":\"awuser\",\"password\":\"********\",\"newCharsetName\":\"\",\"originalCharsetName\":\"\",\"schema\":\"\",\"options\":null,\"port\":0,\"authType\":\"\",\"creator\":\"1\",\"principal\":\"\",\"keyPath\":\"\",\"connectionPoolAttr\":{\"initialSize\":0,\"maxActive\":50,\"maxIdle\":10,\"minIdle\":0,\"maxWait\":10000,\"validationQuery\":\"\",\"testOnBorrow\":true,\"testOnReturn\":false,\"testWhileIdle\":false,\"timeBetweenEvictionRunsMillis\":-1,\"numTestsPerEvictionRun\":3,\"minEvictableIdleTimeMillis\":1800},\"privilegeDetailBeanList\":null}","connectionId":null,"creator":"1","privilegeDetailBeanList":null}"""
        res_add = requests.request("post",
                                   url=handle_config.conf['BI_API']['dec'] + handle_config.conf['connection']['add'],
                                   headers=headers, data=payload_add)
        res_test = requests.request("post",
                                    url=handle_config.conf['BI_API']['dec'] + handle_config.conf['connection']['test'],
                                    headers=headers, data=payload_test)
        data_add = eval(res_add.text)
        data_test = eval(res_test.text)
        print(data_test)
        self.assertEqual(data_add['data'], 'success', msg='添加redshift数据连接失败')
        self.assertIn('data', data_test, msg='redshift测试连接失败')

    def test_004(self):
        """获取数据连接列表"""
        res = requests.request("get",
                               url=handle_config.conf['BI_API']['dec'] + handle_config.conf['connection']['list'],
                               headers=headers)
        print(res.text)
        for i, ele in enumerate(GetDict(res.text).getdict()['data']):
            if ele['connectionName'] == 'gp':
                globals()['gp_connection'] = GetDict(res.text).getdict()['data'][i]['connectionName']
            elif ele['connectionName'] == 'redshift':
                globals()['redshift_connection'] = GetDict(res.text).getdict()['data'][i]['connectionName']

        print(gp_connection)
        print(redshift_connection)

        self.assertEqual(len(GetDict(res.text).getdict()['data']), 2)

    def test_005(self):
        '''添加数据连接_redshift'''

    pass

    def test_006(self):
        '''添加数据连接_redshift'''

    pass

    def test_007(self):
        '''添加数据连接_redshift'''

    pass

    def test_008(self):
        '''添加数据连接_redshift'''

    pass

    def test_009(self):
        '''添加数据连接_redshift'''

    pass
