#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order入库质检  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class checkin(object):
    def checkin(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_ncr = "NCRBH" + order_time + "ddgl"                                # NCR编号

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"入库质检")  # 品控管理入库质检列表
        time.sleep(5)
        # 销售合同号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='入库质检']/div/div[1]/div/form/table/tbody/tr[1]/td[2]/span/input[1]")
        # 采购状态进行中搜索
        order.select(key1=2, xpath=".//*[@id='入库质检']/div/div[1]/div/form/table/tbody/tr[2]/td[4]/span/input[1]")
        order.link_text(u"搜")  # 搜索
        time.sleep(5)
        order.link_text(u"办理")
        time.sleep(5)

        # NCR编码
        order.send_key(key1= order_ncr,
                       xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[1]/div[2]/table/tbody/tr[1]/td[3]/span/input[1]")

        # 检验日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[1]/div[2]/table/tbody/tr[2]/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 检验完成日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 质检部门
        button = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/span/a/span"
        search_key = u"美国压缩机技术服务公司"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)

        # 抽样数
        order.send_key(key1="30",
                       xpath=".//*/td[10]/div/table/tbody/tr/td/span/input[1]")

        # 其他信息备注
        order.send_key(key1=u"备注-品控部-ddgl",
        xpath=".//*/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr/td/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\8checkIn.pdf",
        #                   xpath=".//*/div[2]/div[3]/div/div/form/div[7]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        time.sleep(5)
        order.link_text(u"提")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
