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
        首页品类聚合->点击玻尿酸
        打开首页进入任意二级页面，首页的浏览事件记一次
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)
        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        time.sleep(10)
        testbuild.click_bns()
        time.sleep(3)
        self.driver.background_app(5)
        time.sleep(10)

        result = mysql_test.query(action='page_view', event_time=begin_date, page_name='home')
        print(result)
        end_page_view2 = result[0]['params']
        referrer_page_name = end_page_view2['page_name']
        assert referrer_page_name == 'home', 'page_name获取错误！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()