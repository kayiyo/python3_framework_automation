#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import configparser
import os.path

from orderdelivery.ordernew import ordernew
from orderdelivery.projectmanager import projectmanager
from orderdelivery.projectexecute import projectexecute
from orderdelivery.exportnotice import exportnotice
from orderdelivery.purchaserequest import purchaserequest
from orderdelivery.purchaseorder import purchaseorder
from orderdelivery.declarationnew import declarationnew
from orderdelivery.checkin import checkin
from orderdelivery.operationin import operationin
from orderdelivery.shipmentnotice import shipmentnotice
from orderdelivery.checksubmit import checksubmit
from orderdelivery.checkout import checkout
from orderdelivery.operationout import operationout
from orderdelivery.logisticstrack import logisticstrack
from orderdelivery.financialpayment import financialpayment
from framework.webbase import webbase
from framework.logger import Logger

project = "orderProcess"  # 用于读取配置文件和日志输出控制
mylogger = Logger(logger=project + "Log").getlog()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/order_config.ini'
config = configparser.ConfigParser()
config.read(file_path)
order = webbase()

url = config.get("order", "url")        # 读取配置文件
testtime = int(config.get("order", "testtime"))

mylogger.info("The test server url is: %s" % url)
mylogger.info("TestTask : " + project)
mylogger.info("Test Time : %s" % testtime)

order.load_web(url)  # 浏览器载入url

for num in range(1, testtime+1):

    order_process_list = ['orderNew',
                     'projectManager',
                     'projectExecute',
                     'exportNotice',
                     'purchaseRequest',
                     'purchaseOrder',
                     'declarationNew',
                     'checkIn',
                     'operationIn',
                     'shipmentNotice',
                     'checkSubmit',
                     'checkOut',
                     'operationOut',
                     'logisticsTrack',
                     'financialPayment',
                     ]
    for order_process in order_process_list:
        mylogger.info(order_process + " is executing. Please wait...")
        user = config.get(order_process, "user")
        pw = config.get(order_process, "pw")
        order.input_username(user, xpath=".//*[@id='username']")  # 用户名
        order.input_password(pw, xpath=".//*[@id='password']")  # 密码
        order.login1()  # 登录系统
        if order_process == 'orderNew':  # 1新建订单
            orderNew = ordernew()
            order_xsht = orderNew.ordernew()
            mylogger.info("OrderXSHT NO: %s" % order_xsht)
        elif order_process == 'projectManager':  # 2管理项目
            projectManager = projectmanager()
            projectManager.projectmanager(order_xsht)
        elif order_process == 'projectExecute':  # 3执行项目
            projectExecute = projectexecute()
            projectExecute.projectexecute(order_xsht)
        elif order_process == 'exportNotice':  # 4出口通知
            exportNotice = exportnotice()
            order_ckfh = exportNotice.exportnotice(order_xsht)
            mylogger.info("OrderCKFH NO: %s" % order_ckfh)
        elif order_process == 'purchaseRequest':  # 5采购申请
            purchaseRequest = purchaserequest()
            order_xmh = purchaseRequest.purchaserequest(order_xsht)
            mylogger.info("OrderXMH NO: %s" % order_xmh)
        elif order_process == 'purchaseOrder':  # 6采购订单
            purchaseOrder = purchaseorder()
            order_xmh = order_xmh
            purchaseOrder.purchaseorder(order_xmh)
        elif order_process == 'declarationNew':  # 7新增报检单
            declarationNew = declarationnew()
            declarationNew.declarationnew(order_xsht)
        elif order_process == 'checkIn':  # 8入库质检
            checkIn = checkin()
            checkIn.checkin(order_xsht)
        elif order_process == 'operationIn':  # 9办理入库
            operationIn = operationin()
            operationIn.operationin(order_xsht)
        elif order_process == 'shipmentNotice':  # 10新建看货通知
            shipmentNotice = shipmentnotice()
            shipmentNotice.shipmentnotice(order_ckfh)
        elif order_process == 'checkSubmit':  # 11提交质检
            checkSubmit = checksubmit()
            checkSubmit.checksubmit(order_xsht)
        elif order_process == 'checkOut':  # 12出库质检
            checkOut = checkout()
            checkOut.checkout(order_xsht)
        elif order_process == 'operationOut':  # 13办理出库
            operationOut = operationout()
            operationOut.operationout(order_xsht)
        elif order_process == 'logisticsTrack':  # 14物流跟踪
            logisticsTrack = logisticstrack()
            logisticsTrack.logisticstrack(order_xsht)
        elif order_process == 'financialPayment':  # 15财务收款
            financialPayment = financialpayment()
            financialPayment.financialpayment(order_xsht)
        order.logout1()  # 退出系统
        mylogger.info(order_process + " completed")

    mylogger.info("Test Finished : %s" % num)

order.quit_web()  # 退出浏览器
mylogger.info("All Test Done!")
