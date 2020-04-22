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
        美购首页->品类聚合除皱廋脸
        美购列表pv事件
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        testbuild.click_meigou()
        testbuild.click_czsl()
        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(10)

        result = mysql_test.query(action='page_view', event_time=begin_date,page_name = 'welfare_list')
        print(result)
        end_page_view2 = result[0]['params']
        referrer = end_page_view2['referrer']
        page_name = end_page_view2['page_name']
        assert referrer == 'welfare_home', 'referrer获取错误！'
        assert page_name == 'welfare_list', 'page_name获取错误！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'




if __name__ == '__main__':
    unittest.main()