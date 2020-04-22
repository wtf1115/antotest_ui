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
        美购首页->浏览事件
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()
        #  点击美购首页
        testbuild.click_meigou()
        time.sleep(10)
        self.driver.background_app(5)  # 将app置于后台5秒钟，再唤起到前台
        #  美购首页 埋点
        result = mysql_test.query(action='page_view', event_time=begin_date, page_name='welfare_home')
        print(result)
        end_page_view2 = result[0]['params']
        referrer3 = end_page_view2['referrer']
        referrer_page_name = end_page_view2['page_name']
        assert referrer3 == 'home', 'referrer获取错误！'
        assert referrer_page_name == 'welfare_home', 'page_name获取错误！'
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'



        # sql_page_view = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name = 'welfare_home' order by create_time desc".format(
        #     canshu.dev_id)
        # result = canshu.mysql_test.query(sql_page_view)
        # page_view_create_time = result[0]['create_time']
        # print(type(page_view_create_time))
        # page_view_raw_data_all = result[0]['raw_data']
        # page_view_raw_data = json.loads(page_view_raw_data_all)
        # page_view_referrer = page_view_raw_data['params']['referrer']
        # page_view_page_name = page_view_raw_data['params']['page_name']
        # assert page_view_referrer == 'home', 'referrer获取错误！'
        # assert page_view_page_name == 'welfare_home', 'page_name获取错误！'
        # print("page_view: %s" % page_view_create_time)
        # if begin_date > page_view_create_time:
        #     self.log.error("美购首页page_view埋点异常")
        # else:
        #     self.log.info("美购首页page_view埋点正常")
        # time.sleep(10)
        #


if __name__ == '__main__':
    unittest.main()