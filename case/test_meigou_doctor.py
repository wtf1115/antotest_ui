import unittest
import datetime
import time
import json

from page.basetestcase import Testtodolist
from page import canshu
from pageobject.page_todolist_build import TodolistBuild
from common.dbMysql import *
from common.Log import Log


class Testbuild4(Testtodolist):

    log = Log()

    def testbuild(self):
        """
        步骤：
        1、美购首页
        2、搜索框
        4、点击热词
        5、切换医生tab
        :return:
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()
        testbuild.click_meigou()
        testbuild.click_welfare_home_search()  # 偶现失败
        testbuild.click_doctor()
        testbuild.click_hot_search()   # 偶现失败
        time.sleep(5)
        self.driver.background_app(5)
        time.sleep(5)

        # 搜索框 埋点
        result = mysql_test.query(action='search_result_open', event_time=begin_date)
        assert result != ' ', 'search_result_open事件为空！'

        # result1 = mysql_test.query(action='do_search', event_time=begin_date)
        # assert len(result1) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'




if __name__ == '__main__':
    unittest.main()