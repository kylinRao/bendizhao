#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 19:49
# @Author  : Aries
# @Site    : 
# @File    : adbUtil.py
# @Software: PyCharm
import os
from conf.globalFacts import loggerInner


class AdbUtil:
    dataPath = "datas"
    comsohuinfonewsPackageName = "com.sohu.infonews"
    stopApkCmd = "adb  -s {deviceName} shell  am force-stop {packageName}"
    clearApkContentscmd = "adb -s {deviceName} shell pm clear {packageName}"
    packageCommands = {
        comsohuinfonewsPackageName: {
            "saveAccountAdbCommandList": [
                "adb -s {deviceName} root",

                "adb -s {deviceName}  pull /data/data/{packageName}/cache {dataPath}/{deviceName}/{accountName}",

                "adb -s {deviceName}  pull /data/data/{packageName}/files {dataPath}/{deviceName}/{accountName}",

                "adb -s {deviceName}  pull /data/data/{packageName}/shared_prefs {dataPath}/{deviceName}/{accountName}",
                 # "adb -s {deviceName}  pull /data/data/{packageName}/.jiagu {dataPath}/{deviceName}/{accountName}",
                 "adb -s {deviceName}  pull /data/data/{packageName}/databases {dataPath}/{deviceName}/{accountName}",
            ],
            "reloadAccountAdbCommandList": [
                "adb -s {deviceName} root",
                "adb -s {deviceName}  shell rm -rf /data/data/{packageName}/*",
                "adb -s {deviceName}  shell rm -rf /data/data/{packageName}/.jiagu",
                "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/cache /data/data/{packageName}",
                "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/files /data/data/{packageName}",
                "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/shared_prefs /data/data/{packageName}",
                # "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/.jiagu /data/data/{packageName}",
                "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/databases /data/data/{packageName}",
                "adb -s {deviceName}  shell chmod -R 777 /data/data/{packageName}/*",
            ]
        },
    }

    # packageCommands = {
    #     comsohuinfonewsPackageName: {
    #         "saveAccountAdbCommandList": [
    #             "adb -s {deviceName}  pull /data/data/{packageName}/app_textures {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/app_webview {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/cache {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/databases {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/files {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/lib {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/shared_prefs {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/.jiagu {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/shared_prefs {dataPath}/{deviceName}/{accountName}",
    #             "adb -s {deviceName}  pull /data/data/{packageName}/shared_prefs {dataPath}/{deviceName}/{accountName}", ],
    #         "reloadAccountAdbCommandList": [
    #             "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/app_textures /data/data/{packageName}",
    #             "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/app_webview /data/data/{packageName}",
    #             "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/cache /data/data/{packageName}",
    #             "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/databases /data/data/{packageName}",
    #             "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/files /data/data/{packageName}",
    #             "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/lib /data/data/{packageName}",
    #             "adb -s {deviceName}  push {dataPath}/{deviceName}/{accountName}/shared_prefs /data/data/{packageName}"]
    #     },
    # }

    def __init__(self, deviceName, accountName, packageName="com.sohu.infonews"):
        self.deviceName = deviceName
        self.accountName = accountName
        self.packageName = packageName
        self.storeAccountAdbCommandList = [
            cmd.format(deviceName=self.deviceName, accountName=self.accountName, dataPath=AdbUtil.dataPath,
                       packageName=self.packageName) for cmd in
            AdbUtil.packageCommands[self.packageName]["saveAccountAdbCommandList"]]
        self.reloadAccountAdbCommandList = [
            cmd.format(deviceName=self.deviceName, accountName=self.accountName, dataPath=AdbUtil.dataPath,
                       packageName=self.packageName) for cmd in
            AdbUtil.packageCommands[self.packageName]["reloadAccountAdbCommandList"]]
        if not os.path.isdir(os.path.join(AdbUtil.dataPath,deviceName)):
            os.makedirs(os.path.join(AdbUtil.dataPath,deviceName))


    def clearApkContent(self):
        loggerInner.info("clearApkContent method")
        loggerInner.info(AdbUtil.clearApkContentscmd.format(deviceName=self.deviceName, packageName=self.packageName))

        os.system(AdbUtil.clearApkContentscmd.format(deviceName=self.deviceName, packageName=self.packageName))

    def stopApk(self):
        loggerInner.info("stopApk method")
        loggerInner.info(AdbUtil.stopApkCmd.format(deviceName=self.deviceName, packageName=self.packageName))
        os.system(AdbUtil.stopApkCmd.format(deviceName=self.deviceName, packageName=self.packageName))

    def saveAccount(self):
        loggerInner.info("storeAccount method")

        for cmd in self.storeAccountAdbCommandList:
            loggerInner.info(cmd)
            os.system(cmd)

    def reloadAccount(self):
        loggerInner.info("reloadAccount method")
        self.stopApk()
        self.clearApkContent()
        for cmd in self.reloadAccountAdbCommandList:
            os.system(cmd.format())
            loggerInner.info(cmd)


if __name__ == '__main__':
    # 白条
    # au = AdbUtil("49d6e368", "17366163470")
    # au = AdbUtil("49d6e368", "18551789470")
    # au = AdbUtil("49d6e368", "18507945612")
    # au = AdbUtil("49d6e368", "15543642810")
    # au = AdbUtil("49d6e368", "15543645823")
    #
    # au = AdbUtil("9b0b2188", "18551789470")
    # au = AdbUtil("9b0b2188", "17366163470")
    # au = AdbUtil("9b0b2188", "18507945612")
    au = AdbUtil("9b0b2188", "13282076453")
    # au.clearApkContent()


    # au.saveAccount()
    au.reloadAccount()
    # au.clearApkContent()
