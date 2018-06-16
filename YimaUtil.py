#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 19:49
# @Author  : Aries
# @Site    :
# @File    : adbUtil.py
# @Software: PyCharm
import os

import time

import re

from conf.globalFacts import loggerInner
import requests

class YimaUtil:
    def __init__(self):
        self.TOKEN = "0055120932f7763797f3d1c1a5329ebd2c53d632"
        self.EXCLUDEPHONEDUAL = "160"
        self.PROJECTCODE = '11093'

        self.getPhoneNumUrl = "http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token="+self.TOKEN+"&itemid="+self.PROJECTCODE+"&excludeno="+self.EXCLUDEPHONEDUAL
        self.getSmsUrl = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=" + self.TOKEN + "&itemid=" + self.PROJECTCODE + "&mobile={phoneNum}&release=1"
        self.releasePhoneUrl = "http://api.fxhyd.cn/UserInterface.aspx?action=release&token="+self.TOKEN+"&itemid="+self.PROJECTCODE+"&mobile={phoneNum}"
        self.addIgnorePhoneUrl = "http://api.fxhyd.cn/UserInterface.aspx?action=addignore&token="+self.TOKEN+"&itemid="+self.PROJECTCODE+"&mobile={phoneNum}"

    session = requests.Session()
    def getPhoneNum(self,phoneNum=None):
        loggerInner.info("method getPhoneNum:")
        if phoneNum:
            r = self.session.post(url=self.getPhoneNumUrl+"&mobile="+phoneNum)
        else:
            r = self.session.post(url=self.getPhoneNumUrl)
        print(r.text)
        pattern1 = re.compile("[0-9]+")
        matcher1 = re.search(pattern1,r.text)

        return matcher1.group(0)

    def getPhoneValidMsg(self,phoneNum):
        loggerInner.info("method getPhoneValidMsg:")
        r = self.session.post(url=self.getSmsUrl.format(phoneNum=phoneNum))
        return r.text
    def releasePhone(self,phoneNum):
        loggerInner.info("method releasePhone:")
        r = self.session.post(url=self.releasePhoneUrl.format(phoneNum=phoneNum))
        return r.text
    def addignorePhone(self,phoneNum):
        loggerInner.info("method addignorePhone:")
        r = self.session.post(url=self.releasePhoneUrl.format(phoneNum=phoneNum))
        return r.text
    def getPhoneValidMsgUtilTimeout(self,phoneNum,timeout=150):
        loggerInner.info("method getPhoneValidMsgUtilTimeout:")
        timeout = int(timeout)
        while(timeout >= 0):
            resText = self.getPhoneValidMsg(phoneNum)
            if "success" in resText:
                loggerInner.info("wo got a message below:")
                loggerInner.info(resText)
                pattern1 = re.compile("[0-9]+")
                matcher1 = re.search(pattern1,resText)
                self.releasePhone(phoneNum=phoneNum)
                return matcher1.group(0)
            timeout = timeout - 5
            time.sleep(5)
        self.releasePhone(phoneNum=phoneNum)
        return "timeout"









if __name__ == '__main__':
    ym = YimaUtil()
    phoneNum=ym.getPhoneNum()
    ym.getPhoneValidMsgUtilTimeout(phoneNum=phoneNum)

