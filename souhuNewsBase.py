# coding=utf-8
import os

from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

from YimaUtil import YimaUtil
from conf.globalFacts import loggerInner
import unittest
import time
from libs.sendMail import sendMail
from appium import webdriver

# Returns abs path relative to this file and not cwd
from db.dbInit01 import exeSql

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)


class souhuNewsBase(unittest.TestCase):
    screenshotParDir = ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(16)))
    ym = YimaUtil()
    startTime = datetime.now()

    def isElement(self, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException, e:
            flag = False
        finally:
            return flag

    def loginForNewComer(self, phoneNum):
        # 清空缓存首次会有权限提示，我们等待10s权限自动消失
        self.phoneNum = phoneNum
        time.sleep(20)
        # 清空缓存首次会有弹出红包，我们点一下返回键

        self.driver.back()

        self.driver.find_element_by_xpath(
                "//android.widget.LinearLayout[@resource-id='com.sohu.infonews:id/footer_view']/android.widget.RelativeLayout[@index='3']").click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element_by_xpath(
                "//android.widget.RelativeLayout[@resource-id='com.sohu.infonews:id/user_head_layout']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.sohu.infonews:id/content_text']").send_keys(self.phoneNum)
        time.sleep(2)
        self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.sohu.infonews:id/verification_prompt_text']").click()
        # 获取验证码
        validCode = self.ym.getPhoneValidMsgUtilTimeout(phoneNum=phoneNum)

        self.driver.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.sohu.infonews:id/verification_number_edit']").send_keys(
                validCode)
        self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.sohu.infonews:id/login_btn']").click()
        # 回到首页
        time.sleep(6)

    def loginForOlder(self, phoneNum):
        # 清空缓存首次会有权限提示，我们等待10s权限自动消失
        self.phoneNum = phoneNum
        time.sleep(20)
        # 清空缓存首次会有弹出红包，我们点一下返回键

        self.driver.back()

        self.driver.find_element_by_xpath(
                "//android.widget.LinearLayout[@resource-id='com.sohu.infonews:id/footer_view']/android.widget.RelativeLayout[@index='3']").click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element_by_xpath(
                "//android.widget.RelativeLayout[@resource-id='com.sohu.infonews:id/user_head_layout']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.sohu.infonews:id/content_text']").send_keys(self.phoneNum)
        time.sleep(2)
        self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.sohu.infonews:id/verification_prompt_text']").click()
        # 获取验证码
        validCode = self.ym.getPhoneValidMsgUtilTimeout(phoneNum=phoneNum)

        self.driver.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.sohu.infonews:id/verification_number_edit']").send_keys(
                validCode)
        self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.sohu.infonews:id/login_btn']").click()
        # 回到首页
        time.sleep(6)

    def checkNotBeInvited(self):
        self.driver.find_element_by_xpath(
            "//android.widget.LinearLayout[@resource-id='com.sohu.infonews:id/footer_view']/android.widget.RelativeLayout[@index='3']").click()
        # 接下来我们去填写邀请码
        self.driver.find_element_by_xpath(
                "//android.widget.RelativeLayout[@resource-id='com.sohu.infonews:id/user_head_layout']").click()
        time.sleep(2)
        notInvitedText = self.driver.find_element_by_xpath(
            "//android.widget.RelativeLayout[@index='6']/android.widget.RelativeLayout[@index='0']/android.widget.RelativeLayout[@index='1']/android.widget.RelativeLayout[@index='0']/android.widget.TextView").text
        print(notInvitedText)
        if notInvitedText == u"去绑定":
            return True
        else:
            return False

    def enterInviteCode(self, inviteCode):
        loggerInner.info("Method enterInviteCode")
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='6']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
                "//android.widget.TextView[@resource-id='com.sohu.infonews:id/hint_invitationcode']").send_keys(
                inviteCode)
        time.sleep(2)
        self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.sohu.infonews:id/btn_invitation_get']").click()
        time.sleep(2)
        self.driver.back()
        # 签到，然会回到推荐首页
        time.sleep(1)
        self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.sohu.infonews:id/task_button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
                "//android.widget.LinearLayout[@resource-id='com.sohu.infonews:id/footer_view']/android.widget.RelativeLayout[@index='0']").click()
        time.sleep(1)
    def checkIfInGroupTalk(self,selectorValue,selectorType="XPATH"):
        try:
            if selectorType=="XPATH":
                # self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-Id='com.tencent.mm:id/gd']")
                self.driver.find_element_by_xpath(selectorValue)
                return True


        except:
            return False


    def clickWxAds(self,adGroupName):
        #adGroupName群名称暂时不支持中文字符
        loggerInner.info("Method clickWxAds start")
        time.sleep(6)
        #点击进入广告微信群
            #如果按照控件来
        self.driver.find_element_by_xpath(
                u"//*[@text='{adGroupName}']".format(adGroupName=adGroupName)).click()
        time.sleep(3)
        #循环many次访问广告
        many = 1000
        while (many > 0):
            time.sleep(3)
            args = {'end_x': int(self.deviceResolution['width'] / 2),
                        'end_y': int(self.deviceResolution['height'] / 3),
                        'start_x': int(self.deviceResolution['width'] / 2),
                        'start_y': int(self.deviceResolution['height']* 8/ 10), 'duration': 1000}
            self.driver.swipe(**args)
            time.sleep(2)
            many = many - 1
            # #点击一条最后面一条新闻
            self.driver.tap([(int(self.deviceResolution['width'] / 2), int(self.deviceResolution['height']*80 /100.0 ))],duration=50)
            time.sleep(10)

            #页面滑动3下出现广告条
            count = 2
            while (count > 0):
                count = count - 1
                time.sleep(2)
                args = {'end_x': int(self.deviceResolution['width'] / 2),
                        'end_y': int(self.deviceResolution['height'] / 3),
                        'start_x': int(self.deviceResolution['width'] / 2),
                        'start_y': int(self.deviceResolution['height']* 8/ 10), 'duration': 3500}
                self.driver.swipe(**args)

            #点击广告条,等5s加载楚广告页面，如果有弹框，我们点掉探矿
            time.sleep(2)
            self.driver.tap([(int(self.deviceResolution['width'] / 2), int(self.deviceResolution['height']*98.0 /100.0 ))],
                            duration=20)
            time.sleep(4)
            #判断是否有取消跳转应用中心的请求框弹出，弹出则点击取消
            if self.checkIfInGroupTalk("//android.widget.Button[@resource-id='com.tencent.mm:id/alk']"):
                self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.tencent.mm:id/alk']").click()
            if self.checkIfInGroupTalk("//android.widget.Button[@resource-id='com.tencent.mm:id/an2']"):
                self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.tencent.mm:id/an2']").click()
            time.sleep(1)
            self.driver.back()
            time.sleep(1)
            #如果发现当前已经在聊天界面了，那么我们不需要第二次点击返回键
            if self.checkIfInGroupTalk("//android.widget.ImageView[@resource-id='com.tencent.mm:id/gd']"):
                pass
            else:
                self.driver.back()
        loggerInner.info("Method clickWxAds end")
    def shareNews2WX(self, inviteCode="aaa", swipeContentsCount=20):
        loggerInner.info("Method readNews start")
        time.sleep(15)
        many = 300
        while (many > 0):
            #点击进入头条TAB
            self.driver.tap(
                    [(int(self.deviceResolution['width'] / 10.0), int(self.deviceResolution['height'] * 95.0 / 100.0))],
                    duration=1000)
            time.sleep(20)
            many = many - 1
            ###滑动首页屏幕
            args = {'end_x': int(self.deviceResolution['width'] / 2), 'end_y': int(self.deviceResolution['height'] - 1),
                    'start_x': int(self.deviceResolution['width'] / 2),
                    'start_y': int(self.deviceResolution['height'] / 2), 'duration': 3500}
            self.driver.swipe(**args)
            time.sleep(6)
            #点击一条新闻，进入新闻详情页面
            self.driver.tap([(int(self.deviceResolution['width'] / 2), int(self.deviceResolution['height'] / 3))],
                            duration=1000)
            time.sleep(3)
            ##分享新闻到粘贴板


            #点击底部分享按钮

            self.driver.tap([(int(self.deviceResolution['width'] * 80.0/ 100.0), int(self.deviceResolution['height'] * 95.0/100.0))],
                            duration=1000)
            time.sleep(2)
            #点击复制图标
            self.driver.tap([(int(self.deviceResolution['width'] / 10.0), int(self.deviceResolution['height']* 82.0/ 100.0))],
                            duration=20)
            time.sleep(2)
            self.driver
            #点击复制链接按钮：
            #如果用控件的话.
            # self.driver.find_element_by_xpath(
            #     "//android.widget.RelativeLayout[@index='2']").click()

            self.driver.tap([(int(self.deviceResolution['width'] / 2), int(self.deviceResolution['height']*40.0/ 100.0))],
                            duration=1000)
            time.sleep(2)
            #点击确认分享
            #如果用控件的话：
            # self.driver.find_element_by_xpath(
            #     "//android.widget.Button[@resource-id='com.tencent.mm:id/an3']").click()
            #
            # self.driver.tap([(int(self.deviceResolution['width'] *75.0/ 100.0), int(self.deviceResolution['height']*69.0/ 100.0))],
            #                 duration=1000)
            # time.sleep(2)
            #点击返回到新闻详情页
            #如果用控件的话：
            self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.tencent.mm:id/an2']").click()

            # self.driver.tap([(int(self.deviceResolution['width'] *53.0/ 100.0), int(self.deviceResolution['height']*62.0/ 100.0))],
            #                 duration=1000)
            time.sleep(3)
            #返回到新闻详情页
            self.driver.back()
            time.sleep(1)
            self.driver.back()
        loggerInner.info("Method readNews end")

    def readNews(self, inviteCode, swipeContentsCount=20):
        loggerInner.info("Method readNews start")
        time.sleep(10)
        many = 10

        while (many > 0):

            # self.driver.find_element_by_xpath(
            #         "//android.view.View[@resource-id='footer-box']").click()
            self.driver.tap(
                    [(int(self.deviceResolution['width'] / 10), int(self.deviceResolution['height'] * 95 / 100))],
                    duration=1000)


            many = many - 1

            ###滑动首页屏幕
            args = {'end_x': int(self.deviceResolution['width'] / 2), 'end_y': int(self.deviceResolution['height'] - 1),
                    'start_x': int(self.deviceResolution['width'] / 2),
                    'start_y': int(self.deviceResolution['height'] / 2), 'duration': 1000}
            self.driver.swipe(**args)

            time.sleep(3)

            self.driver.tap([(int(self.deviceResolution['width'] / 2), int(self.deviceResolution['height'] *25/ 95))],
                            duration=1000)

            count = 7
            while (count > 0):
                count = count - 1
                time.sleep(6)
                args = {'end_x': int(self.deviceResolution['width'] / 2),
                        'end_y': int(self.deviceResolution['height'] / 2) - 10,
                        'start_x': int(self.deviceResolution['width'] / 2),
                        'start_y': int(self.deviceResolution['height'] / 2), 'duration': 3500}
                self.driver.swipe(**args)

            self.driver.back()
            time.sleep(2)

        # 默认都20次新闻后退出
        # 读取新闻内容，阅读新闻前的第一步先把这个账号记录到数据库中，以后如果要获取徒弟账号就从数据库中后去昨天更新时间为昨天的就行了，如果某天这个徒弟账号无法登陆了，那么他的更新时间就会停留在昨天，永远不会更新了
        self.inviteCode = inviteCode
        # exeSql(self.phoneNum,self.inviteCode)
        # 阅读要闻
        # time.sleep(10)
        # self.driver.find_element_by_xpath(
        #         "//android.widget.LinearLayout[@resource-id='com.sohu.infonews:id/footer_view']/android.widget.RelativeLayout[@index='0']").click()
        # time.sleep(1)
        # # self.driver.find_element_by_xpath(
        # #             "//android.widget.HorizontalScrollView[@resource-id='com.sohu.infonews:id/tab_bar']/android.widget.LinearLayout[@index='0']/android.widget.RelativeLayout[@index='1']").click()
        # time.sleep(2)
        # swipeContentsCount = 30
        # while (swipeContentsCount > 0):
        #     loggerInner.info("swipeContentsCount is {swipeContentsCount}".format(swipeContentsCount=swipeContentsCount))
        #     swipeContentsCount = swipeContentsCount - 1
        #     content = self.driver.find_element_by_xpath(
        #             "//android.widget.TextView[@resource-id='com.sohu.infonews:id/article_mediaName']")
        #     content.click()
        #     time.sleep(1)
        #     readingPageTimeCount = 20
        #     while (readingPageTimeCount > 0):
        #         try:
        #             # 如果发现首次的狐币到账提示，推出此次循环，阅读下一章
        #             billButton = self.driver.find_element_by_xpath(
        #                     "//android.widget.Button[@resource-id='com.sohu.infonews:id/normaldlg_onebtn']")
        #             break
        #
        #         except:
        #             pass
        #         try:
        #             # 如果发现相关阅读，推出此次循环，阅读下一章
        #             billButton = self.driver.find_element_by_xpath(
        #             "//android.widget.TextView[@resource-id='com.sohu.infonews:id/refer_articles_tip']")
        #             break
        #
        #         except:
        #             pass
        #         try:
        #             # 如果发现全部评论，推出此次循环，阅读下一章
        #             billButton = self.driver.find_element_by_xpath(
        #             "//android.widget.TextView[@resource-id='com.sohu.infonews:id/hot_comment_tip']")
        #             break
        #
        #         except:
        #             pass
        #
        #         loggerInner.info(
        #                 "readingPageTimeCount is {readingPageTimeCount}".format(
        #                         readingPageTimeCount=readingPageTimeCount))
        #         readingPageTimeCount = readingPageTimeCount - 1
        #
        #         args = {'end_x': int(self.deviceResolution['width'] / 2), 'end_y': 1,
        #                 'start_x': int(self.deviceResolution['width'] / 2),
        #                 'start_y': int(self.deviceResolution['height'] / 2), 'duration': 3500}
        #         self.driver.swipe(**args)
        #
        #     # 点击返回键两次，因为担心第一次收取奖励的时候，会弹出探矿提示信息
        #
        #     self.driver.back()
        #     time.sleep(1)
        #     self.driver.back()
        #     # 页面下翻一点儿，准备看另外一篇文章
        #     args = {'end_x': int(self.deviceResolution['width'] / 2), 'end_y': 1,
        #             'start_x': int(self.deviceResolution['width'] / 2),
        #             'start_y': int(self.deviceResolution['height'] / 2), 'duration': 1000}
        #     self.driver.swipe(**args)
        loggerInner.info("Method readNews end")

    def setUp(self):
        deviceName = "9b0b2188"
        # deviceName = "49d6e368"
        desired_caps = {}
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

    def tearDown(self):
        loggerInner.info("---------------------cases execurated!!----------------------")

        try:
            self.driver.quit()
        except:
            pass
        finally:
            subject = u'赚钱机执行结果报告'
            content = u'有任务执行结束，或者任务异常终止，请主人前去查看,该任务开始时间为{startTime},结束时间为{endTime}'.format(startTime=self.startTime,endTime=datetime.now())
            sendMail(subject,content)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(souhuNewsBase)
    unittest.TextTestRunner(verbosity=2).run(suite)
