#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :utils_sendmail.py
# @Time      :2021/5/16 14:07
# @author    :Harry
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.base_path import REPORT_PATH

''''邮件发送
1、实例化SMTP对象
2、登录链接
3、邮件发送
4、关闭链接
'''

def send_mail(file_name):
    #构建邮件内容
    msg = MIMEMultipart()
    msg['Subject'] = "自动化测试报告"
    msg['From'] = '931665795@qq.com'
    msg['To']  = '1987232003@qq.com'
    msg['Date'] = '2021-05-16'

    #添加附件
    file = os.path.join(REPORT_PATH, file_name)
    att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)

    # 邮件发送
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 25)  # smtp 默认端口号25
    smtp.login(user='931665795@qq.com', password='daurpzkyneribeeb')  #password 值为邮箱的授权码
    smtp.sendmail(from_addr='931665795@qq.com',to_addrs='1987232003@qq.com',msg=msg.as_string())
    smtp.quit()

send_mail('report.html')


