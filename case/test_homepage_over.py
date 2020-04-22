import unittest
import datetime
import time
import json

from page.basetestcase import Testtodolist
from page import canshu
from pageobject.page_todolist_build import TodolistBuild
from common.dbMysql import *
from common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        首页, 退出
        :return:
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(10)

        result1 = mysql_test.query(action='on_app_session_over', event_time=begin_date)
        print(result1)
        app_session_id =result1[0]['app_session_id']
        end_page_view2 = result1[0]['app']
        end_page_view3 = result1[0]['params']
        serial_id1 = end_page_view2['serial_id']
        params_duration1 = end_page_view3['duration']
        assert app_session_id != ' ', 'app_session_id为空！'
        assert serial_id1 != ' ', 'serial_id为空！'
        assert params_duration1 != ' ', 'params_duration为空！'
        assert len(result1) == 1, f'埋点数量错误，预期为1个，实际为{len(result1)}'


# sql_urban_geographical_location = "select * from maidian_history_data where device_id ='{}' and action = 'urban_geographical_location' order by create_time desc".format(
#             canshu.dev_id)
#         result = canshu.mysql_test.query(sql_urban_geographical_location)
#         end_date_urban_geographical_location = result[0]['create_time']
#         print("urban_geographical_location: %s" % end_date_urban_geographical_location)
#         if begin_date > end_date_urban_geographical_location:
#             self.log.error("urban_geographical_location埋点异常")
#         else:
#             self.log.info("urban_geographical_location埋点正常")
# 
#         time.sleep(10)


if __name__ == '__main__':
    unittest.main()