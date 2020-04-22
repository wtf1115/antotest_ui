import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.pageobject.page_todolist_build import TodolistBuild
from gengmei_app.common.dbMysql import *
from gengmei_app.common.Log import Log


class Testbuild3(Testtodolist):

    log = Log()

    def test_01(self):
        """
        步骤：
        1、美购首页
        2、刷新
        3、美购首页浏览事件记一次
        :return:
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        # 点击美购首页
        testbuild.click_meigou()
        testbuild.switch_android_up()
        time.sleep(2)
        self.driver.background_app(5)  # 将app置于后台5秒钟，再唤起到前台

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