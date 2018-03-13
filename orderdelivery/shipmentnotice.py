#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order新增报检单  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class shipmentnotice(object):
    def shipmentnotice(self, order_ckfh="CKFH"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_cghth = "XZBJDBZ" + order_time + "-ddgl"                                # 新增报检单备注

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"看货通知管理")  # 物流管理看货通知管理列表
        time.sleep(5)
        order.link_text(u"新建看货通知")
        time.sleep(5)

        # 下单时间
        xpath = ".//*[@id='logistics_deliveryAdd']/div/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 出口发货通知到单号
        button = ".//*[@id='logistics_deliveryAdd']/div/form/div[1]/div[2]/table/tbody/tr[2]/td[1]/span/a/span"
        search_key = order_ckfh
        search = "//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[3]/div/span[1]"
        order.choose(button, search_key, search, move)

        # 紧急程度
        order.select(key1=3, xpath=".//*[@id='logistics_deliveryAdd']/div/form/div[1]/div[2]/table/tbody/tr[4]/td[2]/select")
        time.sleep(3)

        # 备货信息
        # 备货要求
        order.send_key(key1=u"备货要求-ddgl",
        xpath=".//*[@id='logistics_deliveryAdd']/div/form/div[5]/div[2]/div/table/tbody/tr[1]/td/span/textarea")
        # 包装要求
        order.send_key(key1=u"包装要求-ddgl",
        xpath=".//*[@id='logistics_deliveryAdd']/div/form/div[5]/div[2]/div/table/tbody/tr[2]/td/span/textarea")

        # # 附件信息
        # order.upload_file(file1="D:\\1fortest\\Order\\10shipmentNotice.pdf",
        # xpath=".//*[@id='logistics_deliveryAdd']/div/form/div[7]/div[2]/table/tbody/tr[2]/td[1]/p[2]/span")

        order.link_text(u"提")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
