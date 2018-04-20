# _*_ coding: utf-8 _*_
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
import random
from framework.logger import Logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from imp import reload
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')  # 如果不添加以上三行代码，xpath如果表达式包括中文，就会报错，python 2.x 默认
# string 类型是assic类型，在xpath拆分的时候，报codec can't decode byte 0xe4 in position 17: ordinal not in range(128)

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 点击弹窗上确定按钮
    def alert_accept(self):
        alert = self.driver.switch_to_alert()
        alert.accept()

    # 点击弹窗的取消按钮
    def alert_dismiss(self):
        alert = self.driver.switch_to_alert()
        alert.dismiss()

    # 获取弹窗上的文本文字内容
    def alert_get_text(self):
        alert = self.driver.switch_to_alert()
        alert_get_text = alert.getText()
        return alert_get_text

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            self.driver.get_screenshot_as_base64()
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()   # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                                "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            logger.info("The element \' %s \' is clicking." % el.text)
            el.click()
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取元素值
    def get_value(self, selector):

        el = self.find_element(selector)
        value = el.get_attribute('value')
        return value

    # 读取文本
    def read_value(self, selector):

        el = self.find_element(selector)
        value = el.text()
        return value

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 输入键盘回车键
    def keys_enter(self, selector):
        el = self.find_element(selector)
        el.send_keys(Keys.ENTER)

    # 选择下拉列表选项
    def select(self, selector, count):

        el = self.find_element(selector)
        try:
            el.click()
            # logger.info("The element \' %s \' was clicked." % el.text)
            for count in range(1, count):
                el.send_keys(Keys.DOWN)
            el.send_keys(Keys.ENTER)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 随机选择下拉列表选项
    def select_random(self, selector, count):

        el = self.find_element(selector)
        try:
            el.click()
            # logger.info("The element \' %s \' was clicked." % el.text)
            for count in range(1, random.randint(2, count)):
                el.send_keys(Keys.DOWN)
            el.send_keys(Keys.ENTER)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 选择列表菜单
    def choose(self, search_button, search_value, search_bar, move, wait=2):

        el = self.find_element(search_button)
        try:
            el.click()
            # logger.info("The element \' %s \' was clicked." % el.text)
            time.sleep(wait)
            el = self.find_element(search_bar)
            el.send_keys(search_value)
            search = "partial_link_text=>搜"
            self.click(search)
            time.sleep(wait)
            moveto = self.find_element(move)
            ActionChains(self.driver).move_to_element_with_offset(moveto, 38, 38).perform()
            ActionChains(self.driver).click().perform()
            time.sleep(1)
            sure = "partial_link_text=>确"
            self.click(sure)
            time.sleep(0.3)

        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
