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
    # button_login = "partial_link_text=>登"
    button_login = "xpath=>//span[contains(.,'登录')]"
    button_logout = "partial_link_text=>退"

    # 输入用户名
    def send_username(self, text):
        self.type(self.input_username, text)

    # 输入密码
    def send_password(self, text):
        self.type(self.input_password, text)

    # 登陆系统
    def login(self):
        self.click(self.button_login)
        self.sleep(1)

    # 退出系统
    def logout(self):
        self.click(self.button_logout)
        self.sleep(1)

    # 临时code写入数据库
    @staticmethod
    def sql_write(field, value):
        db = pymysql.connect(host='localhost', user='orderuser', passwd='order',
                             db='orderdelivery', charset='utf8')
        cursor = db.cursor()
        # sql = "update" + " temporary " + "set " + field + " = '" + value + "' WHERE temporary_id = 1;"
        sql = 'insert into' + ' temporary (' + field + ') value ("' + value + '")'
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            logger.info("%s : %s has been successful update." % (field, value))
        except:
            # 如果发生错误则回滚
            db.rollback()
            logger.warn("%s : %s update to DB failed!" % (field, value))
        db.close()

    # 临时code更新数据库
    @staticmethod
    def sql_update(field, value):
        db = pymysql.connect(host='localhost', user='orderuser', passwd='order',
                             db='orderdelivery', charset='utf8')
        cursor = db.cursor()
        sql = "update" + " temporary " + "set " + field + " = '" + value + "' WHERE temporary_id = (SELECT * FROM (SELECT max(temporary_id) FROM temporary) AS TEMP)"
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            logger.info("%s : %s has been successful update." % (field, value))
        except:
            # 如果发生错误则回滚
            db.rollback()
            logger.warn("%s : %s update to DB failed!" % (field, value))
        db.close()

    # 临时code数据库读出
    @staticmethod
    def sql_read(key='temporary_sales_num'):
        temporary_id = 1
        temporary_sales_num = 'XSHTH2018'
        temporary_projects_num = 'XMH2018'
        temporary_exports_num = 'CKFH2018'
        db = pymysql.connect(host='localhost', user='orderuser', passwd='order',
                             db='orderdelivery', charset='utf8')
        cursor = db.cursor()
        # sql = 'select * from ' + 'temporary'
        sql = 'SELECT * FROM ' + 'temporary WHERE temporary_id = (SELECT MAX(temporary_id) FROM temporary)'
        cursor.execute(sql)
        db.close()
        results = cursor.fetchall()
        for row in results:
            temporary_id = row[0]
            temporary_sales_num = row[1]
            temporary_projects_num = row[2]
            temporary_exports_num = row[3]
        if key == 'temporary_id':
            return temporary_id
        elif key == 'temporary_sales_num':
            logger.info("temporary_sales_num: %s From DB" % temporary_sales_num)
            return temporary_sales_num
        elif key == 'temporary_projects_num':
            logger.info("temporary_projects_num: %s From DB" % temporary_projects_num)
            return temporary_projects_num
        elif key == 'temporary_exports_num':
            logger.info("temporary_exports_num: %s From DB" % temporary_exports_num)
            return temporary_exports_num

    # 转化是否是从临时库中取值
    def ensure_temporary_value(self, value):
        if 'temporary' in value:
            value = self.sql_read(key=value)
            logger.info("The value has been converted from the temporary library.")
        else:
            value = value
        return value

    # 按照不同类型执行操作
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
                order_key = self.ensure_temporary_value(value=order_key)
                self.type(selector=order_xpath, text="%s" % order_key)
            elif order_type == 'SELECT_RANDOM' or order_type == 'B':
                self.select_random(selector=order_xpath, count=int(order_key))
            elif order_type == 'SELECT' or order_type == 'C':
                self.select(selector=order_xpath, count=int(order_key))
            elif order_type == 'DATE' or order_type == 'D':
                self.click(selector=order_xpath)
                self.keys_enter(selector=order_xpath)
            elif order_type == 'CHOOSE' or order_type == 'E':
                order_key = self.ensure_temporary_value(value=order_key)
                self.choose(search_button=order_xpath,
                            search_value=order_key,
                            search_bar=order_search_area,
                            move=order_move_point)
            elif order_type == 'CLICK' or order_type == 'F':
                self.click(selector=order_xpath)
                time.sleep(int(order_key))
            elif order_type == 'READ_VALUE' or order_type == "G":
                self.read_value(selector=order_xpath)
            elif order_type == 'WRITE_TEMP' or order_type == 'W':
                code = self.read_value(selector=order_xpath)
                self.sql_write(field=order_key, value=code)
            elif order_type == 'UPDATE_TEMP' or order_type == 'U':
                code = self.read_value(selector=order_xpath)
                self.sql_update(field=order_key, value=code)
            elif order_type == 'SNAPSHOT' or order_type == 'S':
                self.get_windows_img()
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
