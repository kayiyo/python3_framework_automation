# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
from framework.logger import Logger
from pageobjects.order_base import OrderBase
# import sys
# sys.path.append('D:\\GitHub\\Python\\py3\\')
from testsuites.test_boss_login import BossLogin

logger = Logger(logger="HTMLReport").getlog()
# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# report_path = 'D:\\GitHub\\Python\\py3\\test_report\\'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
ReportName = now + "HTMLReport.html"
HtmlFile = report_path + ReportName
fp = open(HtmlFile, "wb")

# 定义测试用例的目录为当前目录
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

# 构建suite
suite_path = os.path.dirname(os.path.abspath('.')) + '/testsuites/'
suite = unittest.TestSuite()

suite.addTest(BossLogin("test_boss_login1"))
suite.addTest(BossLogin("test_boss_login2"))
suite.addTest(BossLogin("test_boss_login3"))

if __name__ == '__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"BOSS系统测试报告", description=u"用例测试情况", verbosity=2)
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    logger.info("Now, The HTML report is generated.Plz check in %s" % HtmlFile)
