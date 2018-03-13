#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order采购订单  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class purchaseorder(object):
    def purchaseorder(self, order_xmh="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_cghth = "CGHTH" + order_time + "ddgl"                                # 采购合同号

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"采购订单列表")  # 采购订单列表
        time.sleep(3)
        order.link_text(u"新建采购订单")
        time.sleep(5)

        # 采购合同号
        order.send_key(key1= order_cghth,
                       xpath=".//*/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]")

        # 采购合同签订日期
        xpath = ".//*/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 合同约定到货日期
        xpath = ".//*/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 合同变更后到货日期
        xpath = ".//*/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 商品信息

        button = ".//*/div[3]/div[2]/div[1]/div[1]/div/div[2]/span/a/span"
        search_key = order_xmh
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move, wait=10)  # 项目号

        button = ".//*/div[3]/div[2]/div[1]/div[2]/div/div[2]/span/a/span"
        search_key = "20180210000021"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr[1]/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)  # 供应商名称

        # 采购数量
        order.send_key(key1="300",
                       xpath=".//*/td[13]/div/span/input[1]")
        order.send_key(key1="500",
                       xpath=".//*/td[14]/div/span/input[1]")

        # 选择币种
        order.select_list(key1=4,
                          xpath=".//*/div[3]/div[2]/div[1]/div[3]/div/div[3]/span/input[1]")

        # 结算信息
        order.select_list(key1=2,
                          xpath=".//*/div[4]/div[2]/div[1]/div[1]/div/div[2]/span/input[1]")

        button = ".//*/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/span/a/span"
        search_key = u"钻装事业部"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)  # 下发部门

        # 其他信息/备注
        order.send_key(key1=u"采购执行部-备注-ddgl",
                       xpath=".//*/div[5]/div[2]/div/div/div/div[2]/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\6purchaseOrder.pdf",
        # xpath=".//*/div[7]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        time.sleep(5)
        order.link_text(u"提交")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
