#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order入库质检  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class checkout(object):
    def checkout(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"出库质检")  # 品控管理出库质检列表
        time.sleep(5)
        # 销售合同号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='出库质检']/div/div[1]/div/form/table/tbody/tr[1]/td[2]/span/input[1]")
        order.link_text(u"搜")  # 搜索
        time.sleep(5)
        order.link_text(u"办理")
        time.sleep(5)

        # 实物检验结论
        order.select(key1=2,
        xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[12]/div[2]/div/table/tbody/tr[1]/td[1]/select")
        # 资料检验结论
        order.select(key1=2,
        xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[12]/div[2]/div/table/tbody/tr[1]/td[2]/select")

        # 检验日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[12]/div[2]/div/table/tbody/tr[3]/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 放行日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[12]/div[2]/div/table/tbody/tr[4]/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 质检部门
        button = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[12]/div[2]/div/table/tbody/tr[2]/td[2]/span/a/span"
        search_key = u"易瑞国际"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)

        # 特殊放行信息
        # 特殊情况产品放行原因
        order.send_key(key1=u"特殊情况产品放行原因-ddgl",
                       xpath=".//*/div[2]/div[3]/div/div/form/div[14]/div[2]/div/table/tbody/tr[3]/td/span/textarea")

        # 审批意见
        order.send_key(key1=u"审批意见-ddgl",
                       xpath=".//*/div[2]/div[3]/div/div/form/div[14]/div[2]/div/table/tbody/tr[4]/td/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\12checkOut.pdf",
        #                   xpath=".//*/div[2]/div[3]/div/div/form/div[16]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        time.sleep(5)
        order.link_text(u"提")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
