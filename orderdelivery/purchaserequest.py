#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order采购申请  __author__ = 'kayiyo'

from framework import webbase
import time
import random

order = webbase.webbase()


class purchaserequest(object):
    def purchaserequest(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号
        order_xmh = "XMH" + order_time + "ddgl"                           # 项目号
        order.click_button(".//*[@id='sider']/div/div[2]/div[1]/div[1]")       # 项目管理
        order.link_text(u"项目列表")        # 订单列表
        time.sleep(5)
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='project_list']/div[1]/div[1]/div/div[2]/span/input[1]")     # 销售合同号搜索
        order.select(key1=3,
                     xpath=".//*[@id='project_list']/div[3]/div[1]/div/div[2]/span/input[1]")     # 项目状态正常执行搜索
        order.link_text(u"搜索")      # 搜索
        time.sleep(3)
        order.link_text(u"生成采购申请")      # 办理
        time.sleep(5)

        xpath = ".//*/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/input[1]"
        order.click_button(xpath)  # 下发日期
        order.key_enter(xpath)

        # 项目号
        order.send_key(key1=order_xmh,
                       xpath=".//*/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span/input[1]")
        order.select(key1=2,  # 贸易方式
                     xpath=".//*/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/span/input[1]")
        order.select(key1=2,  # 是否厂家直接发货
                     xpath=".//*/div[1]/div[2]/div/div[4]/div[1]/div/div[2]/span/input[1]")
        order.send_key(key1=u"烟台",      #交付地点
                       xpath=".//*/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/span/input[1]")
        order.send_key(key1=u"客户文件要求无",  # 客户文件要求
                       xpath=".//*/div[1]/div[2]/div/div[5]/div/div/div[2]/span/input[1]")

        # 商品信息
        order.select(key1=2,  # 产品分类
                     xpath=".//*/td[2]/div/span/input[1]")

        # 其他信息
        order.send_key(key1=u"备注-商务技术-ddgl",
                       xpath=".//*/div[5]/div[2]/div/div/div/div[2]/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\5purchaseRequest.pdf",
        #                   xpath=".//*/div[7]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        time.sleep(1)
        order.link_text(u"提交")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        return order_xmh
