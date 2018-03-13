#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order新增报检单  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class declarationnew(object):
    def declarationnew(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_cghth = "XZBJDBZ" + order_time + "-ddgl"                                # 新增报检单备注

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"采购订单列表")  # 采购订单列表
        time.sleep(5)
        # 销售合同号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='purchase_list']/div[2]/div[1]/div/div[2]/span/input[1]")
        # 采购状态进行中搜索
        order.select(key1=3, xpath=".//*[@id='purchase_list']/div[2]/div[4]/div/div[2]/span/input[1]")
        order.link_text(u"搜索")  # 搜索
        time.sleep(5)
        order.link_text(u"新增报检单")
        time.sleep(5)

        # 报检时间
        xpath = ".//*/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 是否厂家直接发货
        order.select(key1=3, xpath=".//*/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]")
        time.sleep(3)

        # # 是否外检
        # order.select(key1=2, xpath=".//*/div/div[2]/span/input[1]")

        # 报检数量
        order.send_key(key1="300", xpath=".//*/td[12]/div/span/input[1]")

        # 重量kg
        order.send_key(key1="50", xpath=".//*/td[17]/div/span/input[1]")
        # 长宽高cm
        order.send_key(key1="5*6*10", xpath=".//*/td[18]/div/span/input[1]")

        # 其他信息备注
        order.send_key(key1=order_cghth, xpath=".//*/div[6]/div[2]/div/div/div/div[2]/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\7declarationNew.pdf",
        #                   xpath=".//*/div[7]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        time.sleep(5)
        order.link_text(u"提交")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
