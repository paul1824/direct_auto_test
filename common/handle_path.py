import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目跟目录
CASE_DIR = os.path.join(BASE_DIR, 'testcases')  # 用例脚本所在目录
DATA_DIR = os.path.join(BASE_DIR, 'data')  # 用例数据目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')  # 配置文件目录
REPORT_DIR = os.path.join(BASE_DIR, 'reports')  # 测试报告路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')  # 日志目录路径
CONF_FILE = os.path.join(CONF_DIR, 'config.ini')  # 配置文件路径
DB_INFO = os.path.join(DATA_DIR, 'db_info.ini')  # db数据集结果文件路径
ANALYSIS_PAYLOAD = os.path.join(DATA_DIR, 'analysis_payload.ini')  # db数据集结果文件路径
DB_PAYLOAD = os.path.join(DATA_DIR, 'db_payload.ini')  # db数据集结果文件路径
SQL_PAYLOAD = os.path.join(DATA_DIR, 'sql_payload.ini')  # db数据集结果文件路径


if __name__ == '__main__':
    print('项目路径是:', BASE_DIR)
    print('用例脚本保存在：', CASE_DIR)
    print('配置文件保存在：', CONF_DIR)
    print('数据保存在：', DATA_DIR)
    print('报告保存在：', REPORT_DIR)
    print('日志保存在：', LOG_DIR)
