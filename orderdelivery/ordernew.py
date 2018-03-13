#!/usr/bin/env python2
#  coding=utf-8
# order新建订单  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class ordernew(object):
    def ordernew(self):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_po = "PO" + order_time + "ddgl"                                # PO号
        order_kjxy = "KJXYH" + order_time + "ddgl"                            # 框架协议号
        order_xsht = "XSHTH" + order_time + "ddgl"                            # 销售合同号
        order_hwxsht = "HWXSHTH" + order_time + "ddgl"                        # 海外销售合同号
        order_wlbjd = "WLBJDH" + order_time + "ddgl"                          # 物流报价单号
        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[2]/ul/li/a")     # 订单列表
        time.sleep(3)
        order.link_text(u"新建")
        # order.click_button(xpath=".//*[@id='orderList']/div/div[1]/div/div[1]/a[1]/span/span")      # 新建订单
        time.sleep(3)
        order.send_key(key1=order_po,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]")
        order.send_key(key1=order_kjxy,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/span/input[1]")
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]")
        order.send_key(key1=order_hwxsht,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/span/input[1]")
        order.send_key(key1=order_wlbjd,
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]")
        order.select_list(key1=2,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/span/input[1]")     # 订单类型
        order.click_button(
            xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/span/input[1]")     # 签约日期
        order.key_enter(xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/span/input[1]")
        order.click_button(
            xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/span/input[1]")        # 合同交货日期
        order.key_enter(xpath=".//*[@id='tt']/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/span/input[1]")

        # 获取人
        button = ".//*[@id='tt']/div[1]/div[2]/div/div[5]/div[2]/div/div[2]/span/a/span"
        search_key = u"张立才"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)

        order.select_list(key1=13,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[6]/div[1]/div/div[2]/span/input[1]")  # 签约主体公司

        button = ".//*[@id='tt']/div[1]/div[2]/div/div[6]/div[2]/div/div[2]/span/a/span"    # 事业部
        search_key = u"钻装事业部"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)

        button = ".//*[@id='tt']/div[1]/div[2]/div/div[7]/div[1]/div/div[2]/span/a/span"  # 执行分公司
        search_key = u"俄罗斯"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)

        order.select_list(key1=2,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[8]/div[1]/div/div[2]/span/input[1]")  # 分销部

        order.select(key1=8,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[8]/div[2]/div/div[2]/span/input[1]")  # 国家

        button = ".//*[@id='tt']/div[1]/div[2]/div/div[9]/div[1]/div/div[2]/span/a/span"    # CRM客户代码
        search_key = "ERHSK005"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move, wait=10)

        order.select_list(key1=2,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[9]/div[2]/div/div[2]/span/input[1]")      # 客户类型

        order.send_key(key1=u"王回款",
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[10]/div[1]/div/div[2]/span/input[1]")    # 回款责任人

        button = ".//*[@id='tt']/div[1]/div[2]/div/div[10]/div[2]/div/div[2]/span/a/span"    # 商务技术经办人
        search_key = "004658"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)

        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[12]/div/div/div[2]/span/input[1]")     # 授信情况
        order.select_list(key1=2,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[11]/div[1]/div/div[2]/span/input[1]")     # 是否预投
        order.select_list(key1=2,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[11]/div[2]/div/div[2]/span/input[1]")  # 是否融资项目
        order.select_list(key1=12,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[13]/div[1]/div/div[2]/span/input[1]")     # 贸易术语
        order.select_list(key1=6,
                          xpath=".//*[@id='tt']/div[1]/div[2]/div/div[13]/div[2]/div/div[2]/span/input[1]")     # 运输方式
        time.sleep(3)

        order.send_key(key1=(random.randint(1, 10) * 1000000),
                       xpath=".//*[@id='tt']/div[5]/div[2]/div[1]/div[1]/div/div[2]/span/input[1]")     # 合同总价
        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[5]/div[2]/div[1]/div[1]/div/div[3]/span/input[1]")  # 币种
        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[5]/div[2]/div[2]/div[1]/div/div[2]/span/input[1]")      # 收款方式
        order.select_list(key1=3,
                          xpath=".//*[@id='tt']/div[5]/div[2]/div[1]/div[2]/div/div[2]/span/input[1]")     # 是否含税
        order.send_key(key1=(random.randint(1, 10) * 100000),
                       xpath=".//*[@id='tt']/div[5]/div[2]/div[2]/div[2]/div/div[2]/span[1]/input[1]")      # 质保金

        button = ".//*[@id='tt']/div[3]/div[2]/div[3]/input"
        search_key = "Winter coverall"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr[2]/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)  # 添加商品

        order.send_key(key1="300",
                       xpath=".//*[@id='datagrid-row-r4-2-0']/td[4]/div/span/input[1]")     # 合同数量
        order.send_key(key1=u"客户需求描述1",
                       xpath=".//*[@id='datagrid-row-r4-2-0']/td[8]/div/span/input[1]")     # 客户需求描述

        button = ".//*[@id='tt']/div[1]/div[2]/div/div[14]/div[1]/div/div[2]/span/a/span"
        search_key = u"卡塔赫纳"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)  # 起运港
        order.send_key(key1=u"卡塔赫纳1",
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[14]/div[3]/div/div[2]/span/input[1]")    # 发运起始地

        button = ".//*[@id='tt']/div[1]/div[2]/div/div[15]/div[1]/div/div[2]/span/a/span"
        search_key = u"卡亚俄"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[1]/div/span[1]"
        order.choose(button, search_key, search, move)  # 目的港
        order.send_key(key1=u"卡亚俄1",
                       xpath=".//*[@id='tt']/div[1]/div[2]/div/div[15]/div[3]/div/div[2]/span/input[1]")  # 目的地

        order.send_key(key1=u"交货要求描述",
                       xpath=".//*[@id='tt']/div[7]/div[2]/div[1]/div/div/div[2]/span/textarea")        # 交货要求描述
        order.send_key(key1=u"客户及项目背景描述",
                       xpath=".//*[@id='tt']/div[7]/div[2]/div[2]/div/div/div[2]/span/textarea")  # 客户及项目背景描述

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\1orderNew.pdf",
        #                   xpath=".//*[@id='tt']/div[9]/div[2]/table/tbody/tr/td[1]/p[2]/span")
        # order.upload_file(link_text=u"传", file="D:\\1fortest\\Order\\1orderNew.pdf")

        time.sleep(5)
        order.link_text(u"提交立项")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        return order_xsht
