# coding=utf-8
import random
import time
import unittest

import re

from YimaUtil import YimaUtil
from appium import webdriver
import os
from conf.globalFacts import loggerInner
import souhuNewsBase
import adbUtil

# Returns abs path relative to this file and not cwd
from db.dbInit01 import exeSql

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)


class RegisterAccount(souhuNewsBase.souhuNewsBase):

    phoneList =['18473817469', '17097696070', '18774444259', '17175342634', '13186712994', '13262500570', '15584157391',  '15504435842', '17081821041',  '13175714273', '13225147139', '17046374156', '13282058476', '15584140210', '18473814715', '15584285241', '15590570348', '13184400039', '15526839004', '15282881124', '15604416344', '15590577454', '13469487227']
    # phoneList = ["18408186739","17176050312","17088966102","17086363246","17083440398","17079327423","17075688348","17073033044","15590548747","15584404814","15584274960","15584154072","15584121282"]
    def setUp(self):
        self.inviteCode = random.sample(["A4844613", "A4851172"], 1)[0]
        # self.ym = YimaUtil()
        # getPhone = random.sample(RegisterAccount.phoneList,1)[0]
        # RegisterAccount.phoneList.remove(getPhone)
        #
        # self.phoneNum = self.ym.getPhoneNum(phoneNum=getPhone)
        # deviceName = "9b0b2188"
        # 白皮
        deviceName = "ZY223P67ZR"
        desired_caps = {}
        # self.au = adbUtil.AdbUtil(deviceName, self.phoneNum)
        # self.au.clearApkContent()

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = 'com.bdvtt.www'
        desired_caps['appActivity'] = 'com.uzmap.pkg.EntranceActivity'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['udid'] = deviceName

        self.driver = webdriver.Remote('http://127.0.0.1:7723/wd/hub', desired_caps)
        self.deviceResolution = self.driver.get_window_size()
        loggerInner.info("self.deviceMaxX:")
        loggerInner.info(self.deviceResolution)

    def test_01_register(self):

        # c = re.compile("\d{11}")
        # rr = c.match(self.phoneNum)
        # if not rr:
        #     return 0
        # self.loginForOlder(self.phoneNum)
        self.readNews(inviteCode=self.inviteCode)





if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    count = 60
    while (count > 0):
        count = count - 1
        suite.addTest(RegisterAccount("test_01_register"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)