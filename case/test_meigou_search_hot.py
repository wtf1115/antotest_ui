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
        2、品类聚合
        3、搜索框
        4、点击热词
        :return:
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()
        testbuild.click_meigou()
        time.sleep(5)
        testbuild.click_czsl()
        testbuild.click_search()
        time.sleep(2)
        testbuild.click_hot_search()
        time.sleep(5)

        self.driver.background_app(5)
        time.sleep(5)

        # 美购搜索 埋点
        result = mysql_test.query(action='search_result_open', event_time=begin_date)
        assert result != ' ', 'search_result_open事件为空！'

        # result1 = mysql_test.query(action='do_search', event_time=begin_date)
        # assert len(result1) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'

        # on_click_search_pv = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name = 'search_result_welfare' order by event_time desc".format(
        #     canshu.dev_id)
        # result_do_search_pv = canshu.mysql_test.query(on_click_search_pv)
        # search_pv_create_time = result_do_search_pv[0]['event_time']
        # if begin_date > search_pv_create_time:
        #     self.log.error("搜索search_pv埋点异常")
        # else:
        #     self.log.info("搜索do_search埋点正常")
        #     timestamp = "select count(*) from maidian_history_data where event_time between '{}' and '{}' device_id ='{}' and action = 'page_view' and page_name = 'search_result_welfare' order by event_time desc".format(
        #         begin_date, search_pv_create_time, canshu.dev_id)
        #     if timestamp > 1:
        #         self.log.error("搜索search_pv埋点重复曝光")
        #     else:
        #         self.log.info("搜索search_pv埋点曝光数量正常")
        # time.sleep





if __name__ == '__main__':
    unittest.main()