# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 15:51
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_config.py.py

from configparser import ConfigParser
from direct_auto_test.common.handle_path import CONF_FILE
from direct_auto_test.common.handle_path import DB_INFO
from direct_auto_test.common.handle_path import DB_PAYLOAD
from direct_auto_test.common.handle_path import SQL_PAYLOAD
from direct_auto_test.common.handle_path import ANALYSIS_PAYLOAD


class ConfigRead(ConfigParser):
    """用于读取配置文件的处理程序"""

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding='utf8')


conf = ConfigRead(CONF_FILE)
db_info = ConfigRead(DB_INFO)
db_payload = ConfigRead(DB_PAYLOAD)
sql_payload = ConfigRead(SQL_PAYLOAD)
analysis_payload = ConfigRead(ANALYSIS_PAYLOAD)
# if __name__ == '__main__':
#     print(db_info['gp']['url'])
# conf = ConfigHandler(CONF_FILE)
# print(conf['mysql']['port'])
# print(conf['mysql']['user'])
# print(conf['test_data']['phone'])
