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
    def setUp(self):
        deviceName = "A10EBMM2D6XV"
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['udid'] = deviceName

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.deviceResolution = self.driver.get_window_size()
        loggerInner.info("self.deviceMaxX:")
        loggerInner.info(self.deviceResolution)

    def test_01_register(self):
        self.clickWxAds(u"ad4kylin")

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterAccount)
    unittest.TextTestRunner(verbosity=2).run(suite)
