import unittest
import time
import datetime

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.pageobject.page_todolist_build import TodolistBuild
from gengmei_app.page import canshu
from gengmei_app.common.dbMysql import *
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
        time.sleep(10)
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time.sleep(5)
        testbuild.home_search()
        self.driver.background_app(5)
        result = mysql_test.query(action='on_click_navbar_search', event_time=begin_date)
        print(result)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'

        # end_page_view2 = result[0]['params']
        # referrer2 = end_page_view2['referrer']
        # referrer_tab_name2 = end_page_view2['referrer_tab_name']
        # assert referrer2 == 'home', 'referrer获取错误！'
        # assert referrer_tab_name2 == '精选', 'referrer_tab_name获取错误！'
        # assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'
        # print("page_view: %s" % end_page_view2)

        # on_click_navbar_search = "select * from maidian_history_data where device_id ='{}' and action = 'on_click_navbar_search' order by event_time desc".format(
        #     canshu.dev_id)
        # result = canshu.mysql_test.query(on_click_navbar_search)
        # print(result)
        # end_date_home_open = result[0]['event_time']
        # print(type(end_date_home_open))
        # print("on_click_navbar_search: %s" % end_date_home_open)
        # if begin_date > end_date_home_open:
        #     self.log.error("on_click_navbar_search埋点异常")
        # else:
        #     self.log.info("on_click_navbar_search埋点正常")
        #
        # time.sleep(30)



if __name__ == '__main__':
    unittest.main()