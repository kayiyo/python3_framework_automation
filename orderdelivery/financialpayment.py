#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order新增报检单  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class financialpayment(object):
    def financialpayment(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_cghth = "XZBJDBZ" + order_time + "-ddgl"                                # 新增报检单备注

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"收款管理")  # 财务管理收款管理列表
        time.sleep(5)
        # 销售合同号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='收款管理']/div/div[1]/div/form/table/tbody/tr[1]/td[1]/span/input[1]")
        # 跟踪状态待执行搜索
        order.select(key1=2,
                     xpath=".//*[@id='收款管理']/div/div[1]/div/form/table/tbody/tr[2]/td[2]/span/input[1]")
        order.link_text(u"搜")  # 搜索
        time.sleep(5)
        order.link_text(u"办理")
        time.sleep(5)

        # 添加一条收款记录
        account = random.randint(1, 10) * 10000
        order.link_text(u"添加一条收款记录")
        time.sleep(5)
        # 回款时间
        xpath = ".//*[@id='ff']/table/tbody/tr[4]/td/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)
        # 发货时间
        xpath = ".//*[@id='ff']/table/tbody/tr[6]/td/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)
        # 描述
        order.send_key(key1=u"收到客户款项", xpath=".//*[@id='ff']/table/tbody/tr[1]/td/span/input[1]")
        # 回款金额
        order.send_key(key1=account, xpath=".//*[@id='ff']/table/tbody/tr[2]/td/span/input[1]")
        # 发货金额
        order.send_key(key1=account, xpath=".//*[@id='ff']/table/tbody/tr[5]/td/span/input[1]")
        order.link_text(u"确定")
        time.sleep(3)

        # 添加一条收款记录
        account = random.randint(1, 10) * 10000
        order.link_text(u"添加一条收款记录")
        time.sleep(5)
        # 回款时间
        xpath = ".//*[@id='ff']/table/tbody/tr[4]/td/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)
        # 发货时间
        xpath = ".//*[@id='ff']/table/tbody/tr[6]/td/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)
        # 描述
        order.send_key(key1=u"收到客户款项", xpath=".//*[@id='ff']/table/tbody/tr[1]/td/span/input[1]")
        # 回款金额
        order.send_key(key1=account, xpath=".//*[@id='ff']/table/tbody/tr[2]/td/span/input[1]")
        # 发货金额
        order.send_key(key1=account, xpath=".//*[@id='ff']/table/tbody/tr[5]/td/span/input[1]")
        order.link_text(u"确定")
        time.sleep(3)

        order.link_text(u"确认全部收款完成")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
