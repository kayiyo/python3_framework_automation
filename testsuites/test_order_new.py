# _*_ coding: utf-8 _*_
import time
import unittest
import configparser
import os.path
from framework.browser_engine import BrowserEngine
from pageobjects.order_base import OrderBase
# import sys
# sys.path.append('D:\\GitHub\\Python\\py3\\')


class OrderNew(unittest.TestCase):
    """新建订单"""

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

    # @unittest.skip
    def test_order_new(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config_order.ini'
        config.read(file_path)

        process = 'orderNew'
        user = config.get(process, "user")
        password = config.get(process, "pw")
        db_table = process

        orderbase = OrderBase(self.driver)
        orderbase.send_username(user)
        orderbase.send_password(password)
        orderbase.login()
        time.sleep(2)
        orderbase.get_windows_img()

        orderbase.order_execute(db_table)

        orderbase.get_windows_img()
        orderbase.logout()

if __name__ == '__main__':
    unittest.main()
