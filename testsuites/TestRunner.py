# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
# import sys
# sys.path.append('D:\\GitHub\\Python\\py3\\')


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# report_path = 'D:\\GitHub\\Python\\py3\\test_report\\'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 定义测试用例的目录为当前目录
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

# 构建suite
suite_path = os.path.dirname(os.path.abspath('.')) + '/testsuites/'
suite = unittest.TestLoader().discover(suite_path)

if __name__ == '__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"订单交付系统测试报告", description=u"用例测试情况", verbosity=2)
    # 开始执行测试套件
    runner.run(suite)
