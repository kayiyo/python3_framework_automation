# _*_ coding: utf-8 _*_
import time
import unittest
import configparser
import os.path
from framework.browser_engine import BrowserEngine
from pageobjects.order_base import OrderBase
# import sys
# sys.path.append('D:\\GitHub\\Python\\py3\\')
config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config_order.ini'
config.read(file_path)

class BossLogin(unittest.TestCase):
    """BOSS登录"""

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_boss_login1(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """

        process = 'bossLogin1'
        user = config.get(process, "user")
        password = config.get(process, "pw")

        orderbase = OrderBase(self.driver)
        orderbase.click(selector='xpath=>//*[@id=\"enlang\"]')
        orderbase.send_username(user)
        orderbase.send_password(password)
        orderbase.click(selector="xpath=>//*[@id=\"go\"]")
        time.sleep(3)
        tips = orderbase.read_value(selector='xpath=>//*[@id=\"loginForm\"]/div[2]/p[1]')
        self.assertEqual(tips, 'Wrong password')

    def test_boss_login2(self):
        process = 'bossLogin2'
        user = config.get(process, "user")
        password = config.get(process, "pw")

        orderbase = OrderBase(self.driver)
        orderbase.click(selector='xpath=>//*[@id=\"zhlang\"]')
        orderbase.send_username(user)
        orderbase.send_password(password)
        orderbase.login()
        tips = orderbase.read_value(selector='xpath=>//*[@id=\"loginForm\"]/div[2]/p[1]')
        self.assertEqual(tips, '密码错误')

    def test_boss_login3(self):
        process = 'bossLogin3'
        user = config.get(process, "user")
        password = config.get(process, "pw")

        orderbase = OrderBase(self.driver)
        orderbase.send_username(user)
        orderbase.send_password(password)
        orderbase.login()
        tips = orderbase.read_value(selector='xpath=>//*[@id=\"home\"]/div[1]/div[2]/div[2]/div[2]/p')
        self.assertEqual(tips, '姜洪伟')

if __name__ == '__main__':
    unittest.main()
