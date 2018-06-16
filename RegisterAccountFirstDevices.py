# coding=utf-8
import random
import time
import unittest

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
    def setUp(self):

        self.inviteCode = random.sample(["A4844613", "A4851172"], 1)[0]
        self.ym = YimaUtil()
        self.phoneNum = self.ym.getPhoneNum()
        # deviceName = "9b0b2188"
        # 白皮
        deviceName = "49d6e368"
        desired_caps = {}
        self.au = adbUtil.AdbUtil(deviceName, self.phoneNum)
        self.au.clearApkContent()

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = 'com.sohu.infonews'
        desired_caps['appActivity'] = 'com.sohu.quicknews.homeModel.activity.HomeActivity'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['udid'] = deviceName

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.deviceResolution = self.driver.get_window_size()
        loggerInner.info("self.deviceMaxX:")
        loggerInner.info(self.deviceResolution)

    def test_01_register(self):

        #
        self.loginForNewComer(phoneNum=self.phoneNum)
        if not self.checkNotBeInvited():
            return
        self.enterInviteCode(inviteCode=self.inviteCode)
        self.readNews(inviteCode=self.inviteCode)


    def tearDown(self):
        try:
            self.ym.releasePhone(phoneNum=self.phoneNum)
        except:
            pass
        # 保存该用户状态信息
        # self.au.saveAccount()
        self.driver.quit()


        loggerInner.info("---------------------cases execurated!!----------------------")



if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    count = 40
    while (count > 0):
        count = count - 1
        suite.addTest(RegisterAccount("test_01_register"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
