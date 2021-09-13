# -*- coding:utf-8 -*-
import email
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 邮件主题
mail_title = '主题：测试报告'


# 读取html文件内容
f = open('../report.html', 'rb')
mail_body = f.read()
f.close()


# 邮件内容, 格式, 编码
message = MIMEText(mail_body, 'html', 'utf-8')
'''来源,去向,主题'''
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')


try:
    smtp = smtplib.SMTP()
    # 连接
    smtp.connect(smtpserver)
    # 登录
    smtp.login(username, password)
    # 发送邮件
    smtp.sendmail(sender, receiver, message.as_string())
    print("发送邮件成功！！！")
    # 退出
    smtp.quit()

except smtplib.SMTPException:
    print("发送邮件失败！！！")

