#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# order办理入库  __author__ = 'kayiyo'

from framework.webbase import webbase
import time
import random

order = webbase()


class checksubmit(object):
    def checksubmit(self, order_xsht="ddgl"):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())         # 所有用到的编号

        # order.click_button(xpath=".//*[@id='sider']/div/div[1]/div[1]/div[1]")      # 订单管理
        order.link_text(u"出库管理")  # 仓库管理入库管理列表
        time.sleep(5)
        # 项目号搜索
        order.send_key(key1=order_xsht,
                       xpath=".//*[@id='出库管理']/div/div[1]/div/form/table/tbody/tr[1]/td[2]/span/input[1]")
        # 出库状态未质检搜索
        order.select(key1=2, xpath=".//*[@id='出库管理']/div/div[1]/div/form/table/tbody/tr[3]/td[1]/span/input[1]")
        order.link_text(u"搜")  # 搜索
        time.sleep(5)
        order.link_text(u"办理")
        time.sleep(5)

        # 开单日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[1]/div[2]/table/tbody/tr/td[1]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # 总包装件数
        order.send_key(key1="1",
                       xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[4]/span/input[1]")

        # 运输信息

        # 承运单位名称
        order.send_key(key1=u"承运单位名称ddgl",
        xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[8]/div[2]/div/table/tbody/tr[1]/td[1]/span/input[1]")
        # 司机姓名
        order.send_key(key1=u"司机姓名ddgl",
        xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[8]/div[2]/div/table/tbody/tr[1]/td[2]/span/input[1]")
        # 车牌号码
        order.send_key(key1="CPHM232345",
        xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[8]/div[2]/div/table/tbody/tr[2]/td[1]/span/input[1]")
        # 提货日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[8]/div[2]/div/table/tbody/tr[2]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)
        # 联系电话
        order.send_key(key1="76543534",
        xpath=".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[8]/div[2]/div/table/tbody/tr[3]/td[1]/span/input[1]")

        # 人员信息

        # 经办部门
        button = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[10]/div[2]/div/table/tbody/tr[1]/td[2]/span/a/span"
        search_key = u"易瑞国际"
        search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[1]/span/input[1]"
        move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        order.choose(button, search_key, search, move)
        # # 发运人员
        # button = ".//*[@id='mainTabs']/div[2]/div[4]/div/div/form/div[10]/div[2]/div/table/tbody/tr[2]/td[1]/span/a/span"
        # search_key = u"美国压缩机技术服务公司"
        # search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        # move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        # order.choose(button, search_key, search, move)
        # # 协办/复核人
        # button = ".//*[@id='mainTabs']/div[2]/div[4]/div/div/form/div[10]/div[2]/div/table/tbody/tr[3]/td/span/a/span"
        # search_key = u"美国压缩机技术服务公司"
        # search = ".//*[@id='dialog']/div/div[1]/div/form/table/tbody/tr/td[2]/span/input[1]"
        # move = ".//*[@id='dialog']/div/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td/div/span[1]"
        # order.choose(button, search_key, search, move)
        # 发运日期
        xpath = ".//*[@id='mainTabs']/div[2]/div[3]/div/div/form/div[10]/div[2]/div/table/tbody/tr[2]/td[2]/span/input[1]"
        order.click_button(xpath)
        order.key_enter(xpath)

        # # 其他信息备注
        # order.send_key(key1=u"备注-仓储物流部-ddgl",
        #                xpath=".//*/div[2]/div[3]/div/div/form/div[5]/div[2]/div/table/tbody/tr/td/span/textarea")

        # # 附件
        # order.upload_file(file1="D:\\1fortest\\Order\\11checkSubmit.pdf",
        #                   xpath=".//*/div[2]/div[3]/div/div/form/div[7]/div[2]/table/tbody/tr/td[1]/p[2]/span")

        time.sleep(5)
        order.link_text(u"提交质检")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
        order.link_text(u"确定")
        time.sleep(3)
