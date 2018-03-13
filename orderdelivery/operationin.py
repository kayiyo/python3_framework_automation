#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order办理入库  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class operationin(object):
    def operationin(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"入库管理")  # 仓库管理入库管理列表
        time.sleep(5)
        # 销售合同号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='入库管理']/div/div[1]/div/form/table/tbody/tr[1]/td[2]/span/input[1]")
        order.link_text(u"搜")  # 搜索
        time.sleep(5)
        order.link_text(u"办理")
        time.sleep(5)

        # 入库日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[1]/div[2]/table/tbody/tr/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 货物存放地
        order.send_key(key1=u"青岛",
                       xpath=".//*/td[18]/div/table/tbody/tr/td/span/input[1]")

        # 其他信息备注
        order.send_key(key1=u"备注-仓储物流部-ddgl",
                       xpath=".//*/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr/td/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\9operationIn.pdf",
        #                   xpath=".//*/div[2]/div[3]/div/div/form/div[7]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        time.sleep(5)
        order.link_text(u"确认入库")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
