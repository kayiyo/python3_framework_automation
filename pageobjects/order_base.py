# _*_ coding: utf-8 _*_
import time
import pymysql
# import MySQLdb
from framework.logger import Logger
from framework.base_page import BasePage
# import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf8')

logger = Logger(logger="OrderBase").getlog()


class OrderBase(BasePage):

    input_username = "xpath=>//*[@id='username']"
    input_password = "xpath=>//*[@id='password']"
    button_login = "partial_link_text=>登"
    button_logout = "partial_link_text=>退"

    def send_username(self, text):
        self.type(self.input_username, text)

    def send_password(self, text):
        self.type(self.input_password, text)

    def login(self):
        self.click(self.button_login)
        self.sleep(1)

    def logout(self):
        self.click(self.button_logout)
        self.sleep(1)

    @staticmethod
    def sql_write(field, value):
        db = pymysql.connect(host='localhost', user='orderuser', passwd='order',
                             db='orderdelivery', charset='utf8')
        cursor = db.cursor()
        sql = "update" + " temporary " + "set " + field + " = '" + value + "' WHERE temporary_id = 1;"
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        db.close()

    @staticmethod
    def sql_read(key='temporary_sales_num'):
        temporary_id = 1
        temporary_sales_num = 'XSHTH2018'
        temporary_projects_num = 'XMH2018'
        db = pymysql.connect(host='localhost', user='orderuser', passwd='order',
                             db='orderdelivery', charset='utf8')
        cursor = db.cursor()
        sql = 'select * from ' + 'temporary'
        cursor.execute(sql)
        db.close()
        results = cursor.fetchall()
        for row in results:
            temporary_id = row[0]
            temporary_sales_num = row[1]
            temporary_projects_num = row[2]
        if key == 'temporary_id':
            return temporary_id
        elif key == 'temporary_sales_num':
            return temporary_sales_num
        elif key == 'temporary_projects_num':
            return temporary_projects_num

    def order_execute(self, db_table):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 所有用到的编号
        db = pymysql.connect(host='localhost', user='orderuser', passwd='order',
                             db='orderdelivery', charset='utf8')
        cursor = db.cursor()
        sql = 'select * from ' + db_table
        cursor.execute(sql)
        db.close()
        results = cursor.fetchall()
        # order_write_dict = {}
        # order_read_dict = {}
        for row in results:
            order_id = row[0]
            order_name = row[1]
            order_type = row[2]
            order_key = row[3]
            order_xpath = row[4]
            order_search_area = row[5]
            order_move_point = row[6]
            logger.info("The current operation：[%d] %s" % (order_id, order_name))

            if order_type == 'TYPE_DATE' or order_type == 'Z':
                self.type(selector=order_xpath, text="%s%s" % (order_key, order_time))
            elif order_type == 'TYPE' or order_type == 'A':
                self.type(selector=order_xpath, text=order_key)
            elif order_type == 'SEARCH' or order_type == 'S':
                value = self.sql_read(key=order_key)
                if value == '':
                    self.type(selector=order_xpath, text="%s" % '')
                else:
                    self.type(selector=order_xpath, text="%s" % value)
            elif order_type == 'SELECT_RANDOM' or order_type == 'B':
                self.select_random(selector=order_xpath, count=int(order_key))
            elif order_type == 'SELECT' or order_type == 'C':
                self.select(selector=order_xpath, count=int(order_key))
            elif order_type == 'DATE' or order_type == 'D':
                self.click(selector=order_xpath)
                self.keys_enter(selector=order_xpath)
            elif order_type == 'CHOOSE' or order_type == 'E':
                if 'temporary' in order_key:
                    order_key = self.sql_read(key=order_key)
                self.choose(search_button=order_xpath,
                            search_value=order_key,
                            search_bar=order_search_area,
                            move=order_move_point)
            elif order_type == 'CLICK' or order_type == 'F':
                self.click(selector=order_xpath)
                time.sleep(int(order_key))
            elif order_type == 'READ_VALUE' or order_type == "G":
                code = self.read_value(selector=order_xpath)
                return code
            else:
                pass
            # print('%s : %s' % (order_name, order.read_value(order_xpath)))
            # order_write_dict[order_id] = self.get_value(order_xpath)
            # order_read_dict[order_name] = self.get_value(order_xpath)
        # print(order_write_dict)
        # print(order_read_dict)
        # print(len(order_write_dict), len(order_read_dict))
        # print(order_write_dict[1])
        # return order_write_dict[1]
