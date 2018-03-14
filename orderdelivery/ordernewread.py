#!/usr/bin/env python2
#  coding=utf-8
# order新建订单  __author__ = 'kayiyo'

from framework import webbase
import time
import random
import pymysql
from framework.orderbase import OrderBase

order = webbase.webbase()
order_base = OrderBase()


class ordernew(object):
    def ordernew(self, db_table):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_po = "PO" + order_time + "ddgl"                                # PO号
        order_kjxy = "KJXYH" + order_time + "ddgl"                            # 框架协议号
        order_xsht = "XSHTH" + order_time + "ddgl"                            # 销售合同号
        order_hwxsht = "HWXSHTH" + order_time + "ddgl"                        # 海外销售合同号
        order_wlbjd = "WLBJDH" + order_time + "ddgl"                          # 物流报价单号
        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[2]/ul/li/a")     # 订单列表
        time.sleep(5)
        order.link_text(u"新建")
        time.sleep(3)
        order_base.orderbase(db_table)

        # # # 附件
        # # order.upload_file(file1="D:\\1fortest\\Order\\1orderNew.pdf",
        # #                   xpath=".//*[@id='tt']/div[9]/div[2]/table/tbody/tr/td[1]/p[2]/span")
        # # order.upload_file(link_text=u"传", file="D:\\1fortest\\Order\\1orderNew.pdf")
        #
        time.sleep(5)
        order.link_text(u"提交立项")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        ordernew_status = order.read_info(xpath="//div[contains(text(),u'成功')]")
        print(ordernew_status)
        order.link_text(u"确定")
        time.sleep(3)
        return order_xsht
