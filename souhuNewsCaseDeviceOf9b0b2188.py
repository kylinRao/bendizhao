# coding=utf-8

from testCasBase import *
import souhuNewsBase
import adbUtil
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)


class sigleTestsdevice02(souhuNewsBase.souhuNewsBase):
    def setUp(self):
        # deviceName = "9b0b2188"
        # 白皮
        deviceName = "9b0b2188"
        desired_caps = {}
        au = adbUtil.AdbUtil(deviceName, "15504407547")
        au.reloadAccount()
        # time.sleep(5)
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = 'com.sohu.infonews'
        desired_caps['appActivity'] = 'com.sohu.quicknews.homeModel.activity.HomeActivity'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['udid'] = deviceName

        self.driver = webdriver.Remote('http://127.0.0.1:5723/wd/hub', desired_caps)
        self.deviceResolution = self.driver.get_window_size()
        loggerInner.info("self.deviceMaxX:")
        loggerInner.info(self.deviceResolution)




    def test_viewPhoneRelatedNews(self):
        # self.driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.widget.RelativeLayout[10]").click()

        scrollTab = self.driver.find_element_by_xpath("//android.widget.HorizontalScrollView[@index='0']")
        loggerInner.info("position of ele:")
        loggerInner.info(scrollTab.location)
        scrollTabPos = scrollTab.location
        args = {'end_x': int(scrollTabPos['x']) + 1, 'end_y': int(scrollTabPos['y']) + 1,
                'start_x': int(self.deviceResolution['width'] - 1), 'start_y': int(scrollTabPos['y']) + 1,
                'duration': 1000}
        self.driver.swipe(**args)
        time.sleep(1)
        # tabOfPhoneTitle = self.driver.find_element_by_partial_link_text("手机")
        tabOfPhoneTitle = self.driver.find_element_by_xpath(
            "//android.widget.HorizontalScrollView[@index='0']/android.widget.LinearLayout[@index='0']/android.widget.RelativeLayout[@index='10']")
        tabOfPhoneTitle.click()

        # 读取新闻内容
        swipeContentsCount = 20
        while (swipeContentsCount > 0):
            loggerInner.info("swipeContentsCount is {swipeContentsCount}".format(swipeContentsCount=swipeContentsCount))
            swipeContentsCount = swipeContentsCount - 1
            content = self.driver.find_element_by_xpath(
                    "//android.widget.TextView[@resource-id='com.sohu.infonews:id/article_mediaName']")
            content.click()
            time.sleep(1)
            readingPageTimeCount = 15
            while (readingPageTimeCount > 0):

                loggerInner.info(
                        "readingPageTimeCount is {readingPageTimeCount}".format(
                            readingPageTimeCount=readingPageTimeCount))
                readingPageTimeCount = readingPageTimeCount - 1
                if self.isElement("partial link text", "全部评论"):
                    loggerInner.info("找到全部评论字样，退出当前循环")
                    args = {'end_x': int(self.deviceResolution['width'] / 2), 'end_y': 1,
                            'start_x': int(self.deviceResolution['width'] / 2),
                            'start_y': int(self.deviceResolution['height'] / 2), 'duration': 5000}
                    self.driver.swipe(**args)
                    break
                # time.sleep(1)
                args = {'end_x': int(self.deviceResolution['width'] / 2), 'end_y': 1,
                        'start_x': int(self.deviceResolution['width'] / 2),
                        'start_y': int(self.deviceResolution['height'] / 2), 'duration': 5000}
                self.driver.swipe(**args)

            # 点击返回键两次，因为担心第一次收取奖励的时候，会弹出探矿提示信息
            # self.driver.keyevent(4)
            self.driver.back()
            time.sleep(1)
            self.driver.back()
            # 页面下翻一点儿，准备看另外一篇文章
            args = {'end_x': int(self.deviceResolution['width'] / 2), 'end_y': 1,
                    'start_x': int(self.deviceResolution['width'] / 2),
                    'start_y': int(self.deviceResolution['height'] / 2), 'duration': 1000}
            self.driver.swipe(**args)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(sigleTestsdevice02)
    unittest.TextTestRunner(verbosity=2).run(suite)
