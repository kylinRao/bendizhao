# -* - coding: UTF-8 -* -
import os
import urllib


import ConfigParser

from multiprocessing import Process
from urllib2 import URLError


class AppiumServer:

    def __init__(self):
        global appiumPath, baseUrl
        conf = ConfigParser.ConfigParser()
        conf.read("server.cfg")
        appiumPath = conf.get("appserver","appiumPath")
        baseUrl = conf.get("appserver","baseUrl")

    def startServer(self):
        """start the appium server
        :return:
        """
        cmd = self.getCmd()
        t1 = runServer(cmd)
        p = Process(target=t1.start())
        p.start()

    def stopServer(self):
        """stop the appium server
        :return:
        """
        #kill myServer
        os.system('taskkill /f /im node.exe')

    def reStartServer(self):
        """reStart the appium server
        :arg:
        :return:
        """
        self.stopServer()
        self.startServer()

    def isRunnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        url = baseUrl+"/status"
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()

    def getCmd(self):
        """get the cmd of start appium server
        :return:cmd
        """
        rootDirectory = appiumPath[:2]
        startCMD = "node node_modules\\appium\\bin\\appium.js"


        cmd =rootDirectory+"&"+"cd "+appiumPath+"&"+startCMD
        print cmd

        return cmd

import threading


class runServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)

if __name__ == "__main__":
    oo = AppiumServer()
    oo.getCmd()