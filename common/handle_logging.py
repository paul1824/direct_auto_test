# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 19:16
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_logging.py.py

"""
用于返回定制好的的日志
"""
import os
import logging
from common.handle_config import conf
from common.handle_path import LOG_DIR

log_filepath = os.path.join(LOG_DIR, conf.get("log", "filename"))


def create_my_logger():
    """
    创建日志收集器
    :return: 定制好的日志收集器
    """
    log = logging.getLogger("wuji")  # 1. 获取日志收集器对象
    log.setLevel(conf.get("log", "level"))  # 2. 为日志收集器对象设置收集等级
    fh = logging.FileHandler(log_filepath, encoding="utf8")  # 3.1 设置输出渠道以及输出渠道的等级
    fh.setLevel(conf.get("log", "fh_level"))

    sh = logging.StreamHandler()  # 3.2 创建流Handler
    sh.setLevel(conf.get("log", "sh_level"))  # 为流Handler设置等级
    log.addHandler(sh)  # 4.1 把流handler添加到日志收集器对象中
    log.addHandler(fh)  # 4.2 把文件管道handler添加到日志收集器对象中
    # 创建一个输出格式对象
    formats = '%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    formatter = logging.Formatter(formats)
    # 将输出格式添加到输出渠道
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    return log


log = create_my_logger()

if __name__ == '__main__':
    logger = create_my_logger()
    logger.debug('debug')
    logger.info('info..')
    logger.warning('warning..')
    logger.error('error')
    logger.critical('critical')
