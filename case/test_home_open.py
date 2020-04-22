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

        result = mysql_test.query(action='device_opened', event_time=begin_date)
        print(result)
        end_page_view = result[0]['app']
        serial_id = end_page_view['serial_id']
        assert serial_id != ' ', 'serial_id为空！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'



if __name__ == '__main__':
    unittest.main()