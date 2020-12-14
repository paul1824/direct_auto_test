# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 11:32
# @Author  : paul
# @Email   : pp_xiachedan@163.com
# @File    : handle_send_mail.py.py

import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.handle_path import REPORT_DIR


def send_report(report_name):
    """通过qq邮箱发送测试报告给指定的用户"""
    # 第1步：连接qq smtp服务器，模拟登录
    # 1.1 连接到qq  smtp服务器 —— smtp.qq.com
    smtp = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
    # dtmvdiznhytdbbci 是开启smtp的时候，qq给的授权码
    smtp.login(user='1311046186@qq.com', password='dc691cb1')

    # 第2步：构建一封邮件对象， 写邮件
    msg = MIMEMultipart()
    msg['Subject'] = report_name[:-5]  # 邮件标题
    msg['To'] = '1311046186@qq.com'
    msg['From'] = 'paul.zhang@fanruan.com'

    text = MIMEText('您好，附件是测试报告，请查收！', _charset='utf8')  # 构建发送内容
    msg.attach(text)  # 把内容添加到邮件中

    # 上传附件
    # 读取附件内容，bytes格式
    report_file = os.path.join(REPORT_DIR, report_name)
    with open(report_file, mode='rb') as f:
        content = f.read()
        report = MIMEApplication(content)  # 构造附件对象
        report.add_header('content-disposition', 'attachment', filename=report_name)  # 指定附件格式
        msg.attach(report)  # 把构造的附件添加到邮件中

    # 第3步：发送邮件
    smtp.send_message(msg, from_addr='paul.zhang@fanruan.com', to_addrs=['1311046186@qq.com'])


if __name__ == '__main__':
    send_report(report_name='invest.html')
