# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 15:51
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_config.py.py

from configparser import ConfigParser
from common.handle_path import CONF_FILE
from common.handle_path import RESULT_FILE


class ConfigRead(ConfigParser):
    """用于读取配置文件的处理程序"""

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding='utf8')


conf = ConfigRead(CONF_FILE)
result_db = ConfigRead(RESULT_FILE)
# if __name__ == '__main__':
#     conf = ConfigHandler(CONF_FILE)
#     print(conf['mysql']['port'])
#     print(conf['mysql']['user'])
#     print(conf['test_data']['phone'])
