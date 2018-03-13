#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order办理出库  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class operationout(object):
    def operationout(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"出库管理")  # 仓库管理出库管理列表
        time.sleep(5)
        # 销售合同号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='出库管理']/div/div[1]/div/form/table/tbody/tr[1]/td[2]/span/input[1]")
        # 出库状态质检完成搜索
        order.select(key1=4, xpath=".//*[@id='出库管理']/div/div[1]/div/form/table/tbody/tr[3]/td[1]/span/input[1]")
        order.link_text(u"搜")  # 搜索
        time.sleep(5)
        order.link_text(u"办理")
        time.sleep(5)

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\13operationOut.pdf",
        #                   xpath=".//*/div[2]/div[3]/div/div/form/div[16]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        order.link_text(u"确认出库")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
