# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 17:17
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : suite.py


# import HTMLTestRunner
from testcases.test_login import *
import BeautifulReport

suite = unittest.TestSuite()
# 第三种 通过loader来加载用例  通过测试类名来加载用例
loader = unittest.TestLoader()  # 用例的加载器
suite.addTest(loader.loadTestsFromTestCase(TestLogin))

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
