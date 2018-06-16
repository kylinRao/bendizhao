#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 21:27
# @Author  : Aries
# @Site    : 
# @File    : sendMail.py
# @Software: PyCharm
#!/usr/bin/python
# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
import BeautifulSoup as bs
import requests
import time
import json
class IpContent():
    session = requests.Session()
    loginOaUrl = 'http://192.168.1.1'
    statusUrl = 'http://192.168.1.1/userRpm/StatusRpm.htm'
    userName = 'xxx'
    passWord= 'XXx'

    def login(self):
        data = {'userid': self.userName, 'linkpage': '', 'userName': self.userName, 'j_username': self.userName,
                'password': self.passWord, 'j_password': self.passWord}
        headers = {'Cookie': 'Authorization=Basic%20YWRtaW46emJyMTU5NzUz'}
        r = self.session.get(url=self.loginOaUrl, data=data,headers = headers)
        # print("登陆结果：")
        # print(r)
        # print(r.text)
    def getIp(self):

        headers = {'Cookie': 'Authorization=Basic%20YWRtaW46emJyMTU5NzUz; ChgPwdSubTag=','Referer':'http://192.168.1.1/userRpm/StatusRpm.htm'}
        r = self.session.get(url=self.statusUrl,headers=headers)
        # print(r.text)
        soup = bs.BeautifulSoup(r.text)
        ips = soup.findAll('script')
        # print ips[3].text.split(',')
        ipNow = ips[3].text.split(',')[2].strip()
        return ipNow






def sendMail(subject,content,from_addr='hwtest0001@163.com',usr_passwd='Hw123456789',to_addr=['hwtest0001@163.com','975168367@qq.com'],smtp_server = 'smtp.163.com'):
    # 第一个为文本内容,第二个设置文本格式,第三个编码格式
    msg = MIMEText(content,'plain','utf-8')
    # 显示于发件人
    msg['From'] = from_addr
    # 显示与收件人,这个不重要可以省略
    msg['To'] =','.join(to_addr)
    msg['Subject'] =subject


    import smtplib
    # server = smtplib.SMTP(smtp_server,25)
    # 使用了ssl模式
    server = smtplib.SMTP_SSL(smtp_server,465)
    # 设置为调试模式
    server.set_debuglevel(1)
    # 登陆ssl服务器
    server.login(from_addr,usr_passwd)
    # 发送邮件
    server.sendmail(from_addr,to_addr,msg.as_string())
    # 退出
    server.quit()
if __name__ == '__main__':
    # ipLast = ''
    # ic = IpContent()
    # ipNow = ic.getIp()
    # subject = '主人，属下为您提供最新Ip'
    # content = '当前IP是{ip},请查收'.format(ip=ipNow)
    # sendMail(subject,content)
    # ipLast = ipNow

    subject = u'赚钱机执行结果报告'
    content = u'任务执行结束，或者任务异常终止，请主人前去查看'
    sendMail(subject,content)





