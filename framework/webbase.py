#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# web 基类
# __author__ = 'kayiyo'

import random
import os.path
import time
# import SendKeys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class webbase(object):

    driver_switch = 'on'
    chrome_driver_path = os.path.dirname(os.path.abspath('.')) + '/tools/chromedriver.exe'
    if driver_switch == 'off':
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        # driver = webdriver.Chrome('D:\\GitHub\\Python\\python_framework_automation\\tools\\chromedriver.exe')
        # driver = webdriver.Chrome(chrome_driver_path)
        driver = webdriver.Chrome()

    def load_web(self, url):        # 打开浏览器
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(1)

    def quit_web(self):     # 退出浏览器
        self.driver.quit()

    def input_username(self, user, xpath=".//*[@id='inputEmail']"):     # 输入用户名
        input_box = self.driver.find_element_by_xpath(xpath)
        input_box.clear()
        input_box.send_keys(user)
        time.sleep(0.3)

    def input_password(self, pw, xpath=".//*[@id='inputPassword']"):        # 输入密码
        input_box = self.driver.find_element_by_xpath(xpath)
        input_box.clear()
        input_box.send_keys(pw)
        time.sleep(0.3)

    def input_code(self, code, xpath=".//*[@id='inputCode']"):      # 输入验证码
        try:
            input_box = self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            pass
        else:
            input_box.clear()
            input_box.send_keys(code)
            time.sleep(1)

    def login(self, loginbutton=".//*[@id='loginSubmit']"):     # 登录系统Login
        time.sleep(0.3)
        self.driver.find_element_by_xpath(loginbutton).click()
        time.sleep(1)

    def login1(self):       # 点击登录按钮进入系统Login
        time.sleep(0.3)
        self.driver.find_element_by_partial_link_text(u"登").click()
        time.sleep(1)

    def logout(self, logoutbutton="html/body/div[2]/div/div[2]/p[2]/a"):        # 登出系统Logout
        self.driver.find_element_by_xpath(logoutbutton).click()
        time.sleep(1)

    def logout1(self):
        time.sleep(0.3)
        self.driver.find_element_by_partial_link_text(u"退").click()
        time.sleep(1)

    # 输入框输入字符
    def send_key(self, key1, xpath):
        input_box = self.driver.find_element_by_xpath(xpath)
        input_box.clear()
        input_box.send_keys(key1)
        time.sleep(0.3)

    # 输入框输入字符
    def send_key1(self, key1, xpath):
        input_box = self.driver.find_element_by_xpath(xpath)
        input_box.send_keys(key1)
        time.sleep(0.3)

    # 点击按钮
    def click_button(self, xpath):
        try:
            button = self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            # print e
            pass
        else:
            button.click()
        time.sleep(1)

    def link_text(self, link_text):
        self.driver.find_element_by_partial_link_text(link_text).click()

    # 上传文件
    def upload_file1(self, file1, xpath = "//*[@id='file']"):
        self.driver.find_element_by_xpath(xpath).send_keys(file1)

    # # 上传文件/ 打开界面上传文件
    # def upload_file(self, file1, xpath):
    #     upload = self.driver.find_element_by_xpath(xpath)
    #     upload.click()
    #     time.sleep(1)
    #     # SendKeys
    #     SendKeys.SendKeys(file1)
    #     time.sleep(1)
    #     SendKeys.SendKeys("{ENTER}")
    #     time.sleep(1)
    #
    # def upload_file2(self, link_text, file):
    #     self.driver.find_element_by_partial_link_text(link_text).click()
    #     time.sleep(1)
    #     SendKeys.SendKeys(file)
    #     time.sleep(1)
    #     SendKeys.SendKeys("{ENTER}")
    #     time.sleep(1)

    # 下拉框数据选择
    def select_list(self, key1, xpath):
        select = self.driver.find_element_by_xpath(xpath)
        select.click()
        for key1 in range(1, random.randint(2, key1)):
            select.send_keys(Keys.DOWN)
        select.send_keys(Keys.ENTER)
        time.sleep(0.3)

    def select(self, key1, xpath):
        select = self.driver.find_element_by_xpath(xpath)
        select.click()
        for key1 in range(1, key1):
            select.send_keys(Keys.DOWN)
        select.send_keys(Keys.ENTER)
        time.sleep(0.3)

    def select_text(self, text, xpath):
        select_text = self.driver.find_element_by_xpath(xpath)
        Select(select_text).select_by_visible_text(text)

    def search_button(self):
        self.driver.find_element_by_xpath(".//*[@id='su']").click()

    def click_img(self):
        self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").click()

    def date_input(self, date, xpath):
        js = "document.getElementByXpath(" + xpath + ").removeAttribute('readonly')"  # 1.原生js，移除属性
        # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
        # js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
        # js = "$('input[id=txtBeginDate]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath(xpath).send_keys(date)

    def read_info(self, xpath):
        try:
            info = self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            pass
        else:
            return info

    def read_text(self, xpath):
        info = self.driver.find_element_by_xpath(xpath).text
        return info

    def read_no(self, class_name):
        no = self.driver.find_element_by_class_name(class_name).text
        return no

    def switch_window(self, xpath):
        now_handle = self.driver.current_window_handle  # 获取当前窗口句柄
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(3)
        all_handles = self.driver.window_handles  # 获取所有窗口句柄

        for handle in all_handles:

            if handle == now_handle:
                self.driver.close()
            elif handle != now_handle:
                self.driver.switch_to_window(handle)
                time.sleep(1)

    def switch_alert(self):
        self.driver.switch_to_alert()
        time.sleep(1)

    def switch_default(self):
        self.driver.switch_to_default_content()
        time.sleep(1)

    def key_enter(self, xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)

    def key_tab(self, xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(Keys.TAB)

    def left_click(self, xpath):
        ActionChains(self.driver).click(self.driver.find_element_by_xpath(xpath)).perform()
        time.sleep(1)

    def move(self, xpath):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(xpath)).click().perform()

    def moveto(self, xpath, xoffset, yoffset):
        ActionChains(self.driver).move_to_element_with_offset(
            self.driver.find_element_by_xpath(xpath), xoffset, yoffset).perform()
        ActionChains(self.driver).click().perform()

    def choose(self, button, search_key, search, move, wait=2):
        # button 搜索按钮， search_key 搜索值， search 搜索框位置, move 锚点
        self.driver.find_element_by_xpath(button).click()
        # order.switch_alert()
        # time.sleep(2)
        # self.driver.find_element_by_partial_link_text(u" 清 空 ").click()
        time.sleep(wait)
        self.driver.find_element_by_xpath(search).send_keys(search_key)
        self.driver.find_element_by_partial_link_text(u" 搜 索 ").click()
        time.sleep(wait)
        ActionChains(self.driver).move_to_element_with_offset(self.driver.find_element_by_xpath(move), 38, 38).perform()
        ActionChains(self.driver).click().perform()
        time.sleep(1)
        self.driver.find_element_by_partial_link_text(u"确定").click()
        time.sleep(0.3)

    def test_Untitled(self):
        now_handle = self.driver.current_window_handle  # 获取当前窗口句柄

        self.driver.switch_to_window(now_handle)  # 返回主窗口

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        self.driver.switch_to.window(handles[1])
        time.sleep(10)
