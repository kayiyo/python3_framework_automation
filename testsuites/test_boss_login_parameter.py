# _*_ coding: utf-8 _*_
import time
import unittest
import configparser
import os.path
from framework.browser_engine import BrowserEngine
from pageobjects.order_base import OrderBase
from parameterized import parameterized
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

    @parameterized.expand([
        ("user_null", '', "123", "密码错误"),
        ("pwd_null", "user", '', "密码错误"),
        ("login_error", "error", "error", "密码错误"),
        ("login_success", "016416", "123456", "姜洪伟"),
    ])
    def test_boss_login(self, name, username, password, assert_text):
        orderbase = OrderBase(self.driver)
        orderbase.send_username(username)
        orderbase.send_password(password)
        orderbase.login()
        if name == "login_success":
            tips = orderbase.read_value(selector='xpath=>//*[@id=\"home\"]/div[1]/div[2]/div[2]/div[2]/p')
            self.assertEqual(tips, assert_text)
        else:
            tips = orderbase.read_value(selector='xpath=>//*[@id=\"loginForm\"]/div[2]/p[1]')
            self.assertEqual(tips, assert_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
