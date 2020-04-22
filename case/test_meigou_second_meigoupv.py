import unittest
import datetime
import time
import json

from page.basetestcase import Testtodolist
from page import canshu
from pageobject.page_todolist_build import TodolistBuild
from common.dbMysql import *
from common.Log import Log


class Testbuild3(Testtodolist):

    log = Log()

    def test_01(self):
        """
        步骤：
        打开美购首页进入任意二级页面，美购首页的浏览事件记一次
        :return:
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()
        testbuild.click_meigou()
        time.sleep(5)
        testbuild.click_czsl()
        self.driver.background_app(5)
        time.sleep(5)

        result = mysql_test.query(action='page_view', event_time=begin_date, page_name='welfare_home')
        print(result)
        end_page_view2 = result[0]['params']
        referrer3 = end_page_view2['referrer']
        referrer_page_name = end_page_view2['page_name']
        assert referrer3 == 'home', 'referrer获取错误！'
        assert referrer_page_name == 'welfare_home', 'page_name获取错误！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()