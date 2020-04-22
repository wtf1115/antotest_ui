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
        首页, 刷新
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        time.sleep(3)
        testbuild.switch_android_up()
        time.sleep(2)
        self.driver.background_app(5)
        time.sleep(10)

        result = mysql_test.query(action='page_view', event_time=begin_date, page_name='home')
        print(result)
        end_page_view2 = result[0]['params']
        referrer2 = end_page_view2['page_name']
        assert referrer2 == 'home', 'page_name获取错误！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'



if __name__ == '__main__':
    unittest.main()