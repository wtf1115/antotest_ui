import unittest
import time
import datetime

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.pageobject.page_todolist_build import TodolistBuild
from gengmei_app.page import canshu

from gengmei_app.common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        点击首页搜索
        :return:
        """
        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()

        time.sleep(30)

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        time.sleep(5)
        testbuild.home_search()
        self.driver.background_app(5)

        on_click_navbar_search = "select * from maidian_history_data where device_id ='{}' and action = 'on_click_navbar_search' order by create_time desc".format(
            canshu.dev_id)
        result = canshu.mysql_test.query(on_click_navbar_search)
        end_date_home_open = result[0]['create_time']
        print("on_click_navbar_search: %s" % end_date_home_open)
        if begin_date > end_date_home_open:
            self.log.error("on_click_navbar_search埋点异常")
        else:
            self.log.info("on_click_navbar_search埋点正常")
        time.sleep(30)


if __name__ == '__main__':
    unittest.main()