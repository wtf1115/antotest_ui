import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.pageobject.page_todolist_build import TodolistBuild

from gengmei_app.common.Log import Log


class Testbuild3(Testtodolist):

    log = Log()

    def test_01(self):
        """
        步骤：
        1、打开搜索结果页
        2、下拉刷新一次，退出搜索结果页
        3、首页浏览事件记一次
        :return:
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()
        testbuild.click_meigou()
        time.sleep(5)
        testbuild.click_search()
        time.sleep(2)
        testbuild.switch_android_up()
        time.sleep(5)

        self.driver.background_app(5)
        time.sleep(5)

        # 搜索框 埋点
        # sql_do_search = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name ='search_home' order by event_time desc".format(
        #     canshu.dev_id)
        # result2 = canshu.mysql_test.query(sql_do_search)
        # end_page_view2 = result2[0]['event_time']
        # sql_page_view = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name ='welfare_home' and event_time BETWEEN '{}' and  '{}' ".format(
        # canshu.dev_id, begin_date, end_page_view2)
        # assert len(result2) == 1, f'埋点数量错误，预期为1个，实际为{len(result2)}'
        # if begin_date > end_page_view2:
        #     self.log.error("page_view埋点异常")
        # else:
        #     self.log.info("page_view埋点正常")



if __name__ == '__main__':
    unittest.main()