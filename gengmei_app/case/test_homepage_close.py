import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.pageobject.page_todolist_build import TodolistBuild

from gengmei_app.common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        首页， 杀死app进程
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        time.sleep(10)
        self.driver.close_app()   # 强制杀死app
        time.sleep(10)

        sql_page_view = "select * from maidian_history_data where device_id ='{}' and action = 'on_app_session_over' order by create_time desc".format(
            canshu.dev_id)
        result = canshu.mysql_test.query(sql_page_view)
        end_page_view = result[0]['create_time']
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)
        app_serial_id = raw_data['app']['serial_id']
        params_duration = raw_data['params']['duration']
        app_session_id = raw_data['app_session_id']
        print("on_app_session_over: %s" % end_page_view)
        if begin_date > end_page_view:
            self.log.error("on_app_session_over埋点异常")
        else:
            self.log.info("on_app_session_over埋点正常")

        if app_serial_id:
            pass
        else:
            self.log.error("app_serial_id不存在！")

        if params_duration:
            pass
        else:
            self.log.error("params_duration不存在！")

        if app_session_id:
            pass
        else:
            self.log.error("app_session_id不存在！")

        time.sleep(10)

if __name__ == '__main__':
    unittest.main()