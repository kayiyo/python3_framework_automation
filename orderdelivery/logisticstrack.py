#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order新增报检单  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class logisticstrack(object):
    def logisticstrack(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_wlfph = "WLFPH" + order_time + "-ddgl"                                # 新增报检单备注

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"物流跟踪管理")  # 物流管理物流跟踪管理列表
        time.sleep(5)
        # 销售合同号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='物流跟踪管理']/div/div[1]/div/form/table/tbody/tr[1]/td[1]/span/input[1]")
        # 跟踪状态待执行搜索
        order.select(key1=2,
                     xpath=".//*[@id='物流跟踪管理']/div/div[1]/div/form/table/tbody/tr[2]/td[3]/span/input[1]")
        order.link_text(u"搜")  # 搜索
        time.sleep(5)
        order.link_text(u"办理")
        time.sleep(5)

        # 经办时间
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 跟踪信息

        # 物流发票号
        order.send_key(key1=order_wlfph,
        xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[1]/td[2]/span/input[1]")

        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[1]/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)  # 下发订舱时间
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[2]/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)  # 通知市场箱单时间
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[3]/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)  # 船期或航班
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[4]/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)  # 实际离港时间
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[2]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)  # 离厂时间
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[3]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)  # 报关放行时间
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[4]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)  # 预计抵达时间

        # 动态描述
        order.send_key(key1=u"动态描述-ddgl",
         xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[5]/td/span/textarea")

        # 备注
        order.send_key(key1=u"备注-ddgl",
         xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr[6]/td/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\14logisticsTrack.pdf",
        #                   xpath=".//*/div[2]/div[3]/div/div/form/div[7]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        order.link_text(u"项目完结")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)