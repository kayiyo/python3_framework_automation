#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order项目执行  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class projectexecute(object):
    def projectexecute(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_xmgl_bz = "XMGLBZ" + order_time + "ddgl-XMJL"                      # 项目备注

        order.click_button(".//*[@id='sider']/div/div[2]/div[1]/div[1]")       # 项目管理
        order.link_text(u"项目列表")        # 订单列表
        time.sleep(5)
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='project_list']/div[1]/div[1]/div/div[2]/span/input[1]")     # 销售合同号搜索
        order.select(key1=3,
                     xpath=".//*[@id='project_list']/div[3]/div[1]/div/div[2]/span/input[1]")     # 项目状态正常执行搜索
        order.link_text(u"搜索")      # 搜索
        time.sleep(3)
        order.link_text(u"办理")      # 办理
        time.sleep(3)

        xpath = ".//*/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 执行单变更后日期
        order.key_enter(xpath)

        # 项目成员
        # 采购经办人
        button = ".//*/div[3]/div[2]/div[1]/div[1]/div/div[2]/span/a/span"
        search_key = u"孙同伟"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)
        # 品控经办人
        button = ".//*/div[3]/div[2]/div[1]/div[2]/div/div[2]/span/a/span"
        search_key = u"吕全武"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)
        # 国际物流经办人
        button = ".//*/div[3]/div[2]/div[2]/div[2]/div/div[2]/span/a/span"
        search_key = u"郭瑞"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)
        # 仓库经办人
        button = ".//*/div[3]/div[2]/div[2]/div[3]/div/div[2]/span/a/span"
        search_key = u"宗国"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)
        # 备注信息
        order.key_enter(
            xpath=".//*/div[5]/div[2]/div[1]/div/div/div[2]/span/textarea")
        order.send_key(key1=order_xmgl_bz,
                       xpath=".//*/div[5]/div[2]/div[1]/div/div/div[2]/span/textarea")
        time.sleep(1)
        order.link_text(u"执行项目")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
