#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import configparser
import os.path

from framework.logger import Logger
from framework.webbase import webbase
from orderdelivery.checkin import checkin


project = "checkIn"  # 用于读取配置文件和日志输出控制
mylogger = Logger(logger=project + "Log").getlog()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/order_config.ini'
config = configparser.ConfigParser()
config.read(file_path)
order = webbase()
checkIn = checkin()


url = config.get(project, "url")        # 读取配置文件
user = config.get(project, "user")
pw = config.get(project, "pw")
# code = config.get(project, "code")
# testtime = int(config.get(project, "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : " + project + "new")
# mylogger.info("Test Time : %s" % testtime)

order.load_web(url)  # 浏览器载入url

# for num in range(1, testtime+1):
#     order.input_username(user, xpath=".//*[@id='username']")  # 用户名
#     order.input_password(pw, xpath=".//*[@id='password']")  # 密码
#     order.login1()  # 登录系统
#     checkIn.checkin()
#     order.logout1()  # 退出系统
#     mylogger.info("Test Finished : %s" % num)
# order.quit_web()  # 退出浏览器
# mylogger.info("All Test Done!")

order.input_username(user, xpath=".//*[@id='username']")  # 用户名
order.input_password(pw, xpath=".//*[@id='password']")  # 密码
order.login1()  # 登录系统
checkIn.checkin()
