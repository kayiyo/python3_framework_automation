#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order项目管理  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class projectmanager(object):
    def projectmanager(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_xmmc = "XMMC" + order_time + "ddgl"                           # 项目名称
        order_xmgl_bz = "XMGLBZ" + order_time + "ddgl"                      # 项目备注

        order.click_button(".//*[@id='sider']/div/div[2]/div[1]/div[1]")       # 项目管理
        order.link_text(u"项目列表")        # 订单列表
        time.sleep(5)
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='project_list']/div[1]/div[1]/div/div[2]/span/input[1]")     # 销售合同号搜索
        order.select(key1=2,
                     xpath=".//*[@id='project_list']/div[3]/div[1]/div/div[2]/span/input[1]")     # 项目状态未执行搜索
        order.link_text(u"搜索")      # 搜索
        time.sleep(3)
        order.link_text(u"办理")      # 办理
        time.sleep(3)

        xpath = ".//*/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 项目开始时间
        order.key_enter(xpath)
        xpath = ".//*/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 执行单约定交付时间
        order.key_enter(xpath)
        # xpath = ".//*/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]"
        # order.click_button(xpath)  # 执行单变更后日期
        # order.key_enter(xpath)
        xpath = ".//*/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 要求采购到货时间
        order.key_enter(xpath)

        order.send_key(key1=order_xmmc,  # 项目名称
                       xpath=".//*/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/span/input[1]")
        order.send_key(key1=(random.randint(1, 10) * 100000),  # 利润额
                       xpath=".//*/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/span/input[1]")
        order.select_list(key1=4,  # 币种
                          xpath=".//*/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/span/input[1]")
        order.send_key(key1=(random.randint(1, 10) * 10),  # 初步利润
                       xpath=".//*/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]")
        order.select(key1=2,  # 有无项目经理
                     xpath=".//*/div[1]/div[2]/div/div[3]/div[3]/div/div[2]/span/input[1]")
        button = ".//*/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/span/a/span"
        search_key = u"钻装事业部"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)  # 下发部门

        # 项目成员
        # 交付配送中心项目经理
        button = ".//*/div[3]/div[2]/div[2]/div[1]/div/div[2]/span/a/span"
        search_key = u"姜凯涛"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)
        # 备注信息
        order.send_key(key1=order_xmgl_bz,
                       xpath=".//*/div[5]/div[2]/div[1]/div/div/div[2]/span/textarea")
        time.sleep(1)
        order.link_text(u"提交到项目经理")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
