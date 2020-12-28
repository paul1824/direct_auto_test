# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 17:17
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : suite.py


# import HTMLTestRunner

from testcases.test_login import TestLogin
from testcases.test_add_analysis_tables import TestAddAnalysisTables
from testcases.test_add_connection import TestAddConnection
from testcases.test_add_gp_package import TestAddGpPackage
from testcases.test_add_sql_tables import TestAddSqlTables
from testcases.test_add_db_tables import TestAddDbTables
from testcases.test_analysis_filter import TestAddAnalysisFilterTables
from testcases.test_analysis_group_summary import TestAddAnalysisGroupSummaryTables
from testcases.test_analysis_add_new_column import TestAddAnalysisAddColumnTables
from testcases.test_analysis_field_settings import TestAddAnalysisFieldSettingsTables
from testcases.test_analysis_merge_left_right import TestAddAnalysisMergeLeftRightTables
from testcases.test_analysis_merge_up_down import TestAddAnalysisMergeUpDownTables
import BeautifulReport
import unittest
suite = unittest.TestSuite()
# 第三种 通过loader来加载用例  通过测试类名来加载用例
loader = unittest.TestLoader()  # 用例的加载器
suite.addTest(loader.loadTestsFromTestCase(TestLogin))
suite.addTest(loader.loadTestsFromTestCase(TestAddConnection))
suite.addTest(loader.loadTestsFromTestCase(TestAddGpPackage))
suite.addTest(loader.loadTestsFromTestCase(TestAddDbTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddSqlTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisFilterTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisGroupSummaryTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisAddColumnTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisFieldSettingsTables))
# suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisFieldSettingsTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisMergeLeftRightTables))
suite.addTest(loader.loadTestsFromTestCase(TestAddAnalysisMergeUpDownTables))
# 执行用例--unittest版本
# with open('test.txt','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
#     runner.run(suite)

# 执行并生成html测试报告--HTMLTestRunnerNew
# with open('test.html','wb') as file:
#     runner=HTMLTestRunner.HTMLTestRunner(
#         stream=file,
#         verbosity=2,
#         title='20201010测试报告',
#         description='这是登录和获取数据连接列表功能验证的测试报告',
#
#     )#创建一个对象来执行用例
#     runner.run(suite)#这一行没有任何改变

# 使用BeautifulReport生成测试报告
result= BeautifulReport.BeautifulReport(suite)
result.report(description='测试报告',filename='report',report_dir='reports')
