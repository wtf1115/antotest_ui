import unittest
import datetime
import time
import json

from page.basetestcase import Testtodolist
from page import canshu
from common.dbMysql import *
from pageobject.page_todolist_build import TodolistBuild
from common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        首页点击帖子
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        time.sleep(3)
        testbuild.click_home_user_post()
        time.sleep(3)
        self.driver.background_app(5)
        time.sleep(10)

        result = mysql_test.query(action='page_view', event_time=begin_date, page_name='user_post_detail')
        print(result)
        end_page_view2 = result[0]['params']
        referrer3 = end_page_view2['referrer']
        referrer_tab_name2 = end_page_view2['referrer_tab_name']
        assert referrer3 == 'home', 'referrer获取错误！'
        assert referrer_tab_name2 == '精选', 'referrer_tab_name获取错误！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'

        # sql_page_view2 = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name ='diary_detail' order by create_time desc".format(
        # canshu.dev_id)
        # result2 = canshu.mysql_test.query(sql_page_view2)
        # print(result2)
        # end_page_view2 = result2[0]['create_time']
        # end_raw_data2 = result2[0]['raw_data']
        # raw_data2 = json.loads(end_raw_data2)
        # print(raw_data2)
        # referrer_id2 = raw_data2['params']['referrer_id']
        # referrer2 = raw_data2['params']['referrer']
        # referrer_tab_name2 = raw_data2['params']['referrer_tab_name']
        # assert referrer2 == 'home', 'referrer获取错误！'
        # assert referrer_tab_name2 == '精选', 'referrer_tab_name获取错误！'
        # print("page_view: %s" % end_page_view2)
        # if begin_date > end_page_view2:
        #     self.log.error("page_view埋点异常")
        # else:
        #     self.log.info("page_view埋点正常")

        # sql_page_view = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' order by create_time desc".format(
        #     canshu.dev_id)
        # result3 = canshu.mysql_test.query(sql_page_view)
        # print(result3)
        # end_page_view3 = result[0]['create_time']
        # end_raw_data3 = result[0]['raw_data']
        # raw_data3 = json.loads(end_raw_data3)
        # referrer3 = raw_data3['params']['referrer']
        # assert referrer3 == 'home', 'referrer获取错误！'
        # print("page_view: %s" % end_page_view3)
        # if begin_date > end_page_view3:
        #     self.log.error("page_view埋点异常")
        # else:
        #     self.log.info("page_view埋点正常")
        #
        # time.sleep(10)

if __name__ == '__main__':
    unittest.main()