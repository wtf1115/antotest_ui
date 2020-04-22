import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.common.dbMysql import *
from gengmei_app.pageobject.page_todolist_build import TodolistBuild

from gengmei_app.common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        首页----点击日记
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        time.sleep(10)

        testbuild.click_home_diary()
        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(10)

        result = mysql_test.query(action='page_view', event_time=begin_date, page_name='diary_detail')
        print(result)
        end_page_view2 = result[0]['params']
        referrer2 = end_page_view2['referrer']
        referrer_tab_name2 = end_page_view2['referrer_tab_name']
        assert referrer2 == 'home', 'referrer获取错误！'
        assert referrer_tab_name2 == '精选', 'referrer_tab_name获取错误！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'
        print("page_view: %s" % end_page_view2)

        # sql_page_view2 = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name ='diary_detail' order by create_time desc".format(
        # canshu.dev_id)
        # result2 = canshu.mysql_test.query(sql_page_view2)
        # print(result2)
        # end_page_view2 = result[0]['create_time']
        # end_raw_data2 = result[0]['raw_data']
        # raw_data2 = json.loads(end_raw_data2)
        # print(raw_data2)
        # referrer2 = raw_data2['params']['referrer']
        # referrer_tab_name2 = raw_data2['params']['referrer_tab_name']
        # assert referrer2 == 'home', 'referrer获取错误！'
        # assert referrer_tab_name2 == '精选', 'referrer_tab_name获取错误！'
        # assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'
        # print("page_view: %s" % end_page_view2)
        # if begin_date > end_page_view2:
        #     self.log.error("page_view埋点异常")
        # else:
        #     self.log.info("page_view埋点正常")

        

if __name__ == '__main__':
    unittest.main()