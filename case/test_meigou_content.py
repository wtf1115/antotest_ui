import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.pageobject.page_todolist_build import TodolistBuild
from gengmei_app.common.dbMysql import *
from gengmei_app.common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        美购首页->品类聚合除皱廋脸
        美购首页点击事件  此埋点丢失
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()
        testbuild.click_meigou()
        testbuild.click_czsl()
        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(10)

        result = mysql_test.query(action='welfare_home_click_section', event_time=begin_date)
        print(result)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()