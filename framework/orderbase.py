#!/usr/bin/env python3
#  coding=utf-8
# orderbase  __author__ = 'kayiyo'

from framework.webbase import webbase
import time
import pymysql

order = webbase()


class OrderBase(object):
    def orderbase(self, db_table):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 所有用到的编号
        db = pymysql.connect(host = 'localhost', user = 'order', passwd = 'order',
                             db = 'orderdelivery', charset = 'utf8')
        cursor = db.cursor()
        sql = 'select * from ' + db_table
        cursor.execute(sql)
        db.close()
        results = cursor.fetchall()
        order_write_dict = {}
        order_read_dict = {}
        for row in results:
            order_id = row[0]
            order_name = row[1]
            order_type = row[2]
            order_key = row[3]
            order_xpath = row[4]
            order_search_area = row[5]
            order_move_point = row[6]
            # print("id = %s, name = %s, type = %s, key = %s, xpath= %s, search_area = %s, move_point = %s" %
            #       (order_id, order_name, order_type, order_key, order_xpath, order_search_area, order_move_point))
            if order_type == 'Z':
                order.send_key(key1="%s%s" % (order_key, order_time), xpath=order_xpath)
            if order_type == 'A':
                order.send_key(key1=order_key, xpath=order_xpath)
            elif order_type == 'B':
                order.select_list(key1=int(order_key), xpath=order_xpath)
            elif order_type == 'C':
                order.select(key1=int(order_key), xpath=order_xpath)
            elif order_type == 'D':
                order.click_button(xpath=order_xpath)
                order.key_enter(xpath=order_xpath)
            elif order_type == 'E':
                order.choose(order_xpath, order_key, order_search_area, order_move_point)
            else:
                pass
            print(order_name)
            print(order.read_value(order_xpath))
            order_write_dict[order_id] = order.read_value(order_xpath)
            order_read_dict[order_name] = order.read_value(order_xpath)
        print(order_write_dict)
        print(len(order_write_dict), len(order_read_dict))
