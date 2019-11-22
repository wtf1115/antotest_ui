from appium import webdriver
from gengmei.gengmei_app.pageobject.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class TodolistBuild(BasePage):

    gengmei_alert = (By.ID,"com.wanmeizhensuo.zhensuo:id/dialog_home_img_cancel")
    gengmei_ai = "com.wanmeizhensuo.zhensuo:id/item_home_area_single_iv"
    ai_scanface = (By.ID, "com.wanmeizhensuo.zhensuo:id/face_ai_analysis_tv")
    ai_photo = (By.ID, "com.wanmeizhensuo.zhensuo:id/take_photo_album_img")
    ai_phoneselect = "android.widget.RelativeLayout"
    gengmei_anly = (By.ID, "com.wanmeizhensuo.zhensuo:id/jump_over_tv")
    report_back = (By.ID, "com.wanmeizhensuo.zhensuo:id/header_back_iv")
    gengmei_scanagain = (By.ID,"com.wanmeizhensuo.zhensuo:id/face_result_tv_once_again")
    report_share = (By.ID, "com.wanmeizhensuo.zhensuo:id/face_result_iv_share")
    gengmei_skin = (By.ID, "com.wanmeizhensuo.zhensuo:id/face_result_tv_skin")
    def click_alert(self):
        """
        关闭首页广告业
        :return:
        """
        # try:
        #     time.sleep(3)
        #     self.driver.find_element_by_id("com.wanmeizhensuo.zhensuo:id/dialog_home_img_cancel").click()
        # except Exception as e:
        #     print("找不到元素 %s,%d" % (e, 1))
        # finally:
        #     try:
        #         time.sleep(3)
        #         ele = '//android.widget.ImageView[@index="0"]'
        #         self.driver.find_element_by_xpath(ele).click()
        #     except Exception as e:
        #         print("找不到元素 %s,%d" % (e, 2))
        #     finally:
        #         try:
        #             time.sleep(3)
        #             self.driver.find_elements_by_class_name("android.widget.ImageView")[0].click()
        #         except Exception as e:
        #             print("找不到元素 %s,%d" % (e, 3))
        #         finally:
        #             print("继续下一步")

        pass

    def click_ai(self):
        """
        点击首页更美ai豆腐块
        :return:
        """
        self.find_elements(By.ID, self.gengmei_ai, num=2).click()

    def click_gengmei_photo(self):
        """
        选择照片侧颜值
        :return:
        """
        self.click(*self.ai_photo)

    def select_photo(self):
        """
        从相册选择一张照片
        :return:
        """
        self.find_elements(By.CLASS_NAME, self.ai_phoneselect, num=2).click()

    def dump_analyse(self):
        """
        跳过面部分析板块
        :return:
        """
        time.sleep(5)
        self.click(*self.gengmei_anly)

    def ai_report_back(self):
        """
        进入混合型报告页
        点击退出，退出到测服，扫脸页
        :return:
        """
        time.sleep(30)
        self.click(*self.report_back)

    def ai_again(self):
        """
        进入测服结果页
        点击再测一次
        :return:
        """
        self.click(*self.gengmei_scanagain)

    def ai_share(self):
        """
        进入报告页
        点击炫耀肌龄，也就是分享
        :return:
        """
        self.click(*self.report_share)

    def ai_switch_skin(self):
        """
        进入报告页
        点击颜值分析，也就是扫脸
        :return:
        """
        self.click(*self.gengmei_skin)

    def home_search(self):
        """
        点击首页搜索
        :return:
        """
        try:
            search = self.driver.find_element_by_id("com.wanmeizhensuo.zhensuo:id/title_bar_rl_search1")
            search.click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(5)
                search = self.driver.find_elements_by_class_name("android.widget.TextView")[0]
                search.click()
                print(search)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    search ='resourceId("com.wanmeizhensuo.zhensuo:id/title_bar_rl_root").childSelector(resourceId("com.wanmeizhensuo.zhensuo:id/title_bar_rl_search"))'
                    search_click = self.driver.find_element_by_android_uiautomator(search)
                    print(search_click)
                    search_click.click()
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")

    def click_bns(self):
        """
        首页点击玻尿酸
        :return:
        """
        try:
            ele = 'className("android.widget.GridView").childSelector(text("玻尿酸"))'
            bns = self.driver.find_element_by_android_uiautomator(ele)
            bns.click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                ele ='className("android.widget.GridView").childSelector(resourceId("com.wanmeizhensuo.zhensuo:id/text")[1])'
                bns = self.driver.find_element_by_android_uiautomator(ele)
                bns.click()
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                print("继续下一步")

    def click_meigou(self):
        """
        点击美购
        :return:
        """
        try:
            meigou = self.driver.find_element_by_id("com.wanmeizhensuo.zhensuo:id/main_rl_menu_welfare1").click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                meigou = self.driver.find_element_by_id("com.wanmeizhensuo.zhensuo:id/main_tv_menu_welfare").click()
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    ele = 'resourceId("com.wanmeizhensuo.zhensuo:id/main_rl_menu_welfare").childSelector(text("美购"))'
                    bns = self.driver.find_element_by_android_uiautomator(ele)
                    bns.click()
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")


    def click_czsl(self):
        """
        点击美购里的除皱廋脸
        :return:
        """
        try:
            time.sleep(3)
            class_text = '//android.widget.TextView[@text="除皱瘦脸"]'
            self.driver.find_element_by_xpath(class_text).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                desc_class = "//*[@resource-id='com.wanmeizhensuo.zhensuo:id/text'][@text='除皱瘦脸']"
                self.driver.find_element_by_xpath(desc_class).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                print("继续下一步")

    def click_search(self):
        """
        点击美购品类聚合里面的搜索
        :return:
        """
        #  点击搜索
        try:
            time.sleep(3)
            search_id = "com.wanmeizhensuo.zhensuo:id/titlebarTopicHome_ll_search"
            self.driver.find_element_by_id(search_id).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                desc_class = '//android.widget.LinearLayout[@resource-id="com.wanmeizhensuo.zhensuo:id/titlebarTopicHome_ll_search"]'
                self.driver.find_element_by_xpath(desc_class).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    search_id = "com.wanmeizhensuo.zhensuo:id/titlebarTopicHome_tv_search"
                    self.driver.find_element_by_id(search_id).click()
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 2))
                finally:
                    print("继续下一步")

    def click_hot_search(self):
        """
        点击第一个热搜内容
        :return:
        """
        try:
            time.sleep(3)
            search_id = "com.wanmeizhensuo.zhensuo:id/flowitem_common_search_hot_tv_name"
            self.driver.find_element_by_id(search_id).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                ele = 'className("android.widget.RelativeLayout").childSelector(resourceId("com.wanmeizhensuo.zhensuo:id/flowitem_common_search_hot_tv_name"))'
                self.driver.find_element_by_android_uiautomator(ele).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 3))
            finally:
                print("继续下一步")
                time.sleep(5)

    def click_diary(self):
        """
        美购搜索中点击日记
        :return:
        """
        try:
            time.sleep(3)
            diary = "com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_diary"
            self.driver.find_element_by_id(diary).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                desc_class = '//android.widget.RadioButton[@text="日记"]'
                self.driver.find_element_by_xpath(desc_class).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    ele = '//android.widget.TextView[@resource-id="com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_diary"]'
                    self.driver.find_element_by_android_uiautomator(ele).click()
                    time.sleep(3)
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")
                    time.sleep(5)

    def click_wiki(self):
        """
        点击百科
        :return:
        """
        try:
            time.sleep(3)
            wiki = "com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_wiki"
            self.driver.find_element_by_id(wiki).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                wiki = '//android.widget.RadioButton[@text="百科"]'
                self.driver.find_element_by_xpath(wiki).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    wiki = '//android.widget.RadioButton[@resource-id="com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_wiki"]'
                    self.driver.find_element_by_android_uiautomator(wiki).click()
                    time.sleep(3)
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")
                    time.sleep(5)

    def click_post(self):
        """
        点击帖子
        :return:
        """
        try:
            time.sleep(3)
            post = "com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_post"
            self.driver.find_element_by_id(post).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                post = '//android.widget.RadioButton[@text="帖子"]'
                self.driver.find_element_by_xpath(post).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    post = '//android.widget.RadioButton[@resource-id="com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_post"]'
                    self.driver.find_element_by_android_uiautomator(post).click()
                    time.sleep(3)
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")

    def click_hospital(self):
        """
        点击医院
        :return:
        """
        try:
            time.sleep(3)
            hospital = "com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_hospital"
            self.driver.find_element_by_id(hospital).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                hospital = '//android.widget.RadioButton[@text="医院"]'
                self.driver.find_element_by_xpath(hospital).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    hospital = '//android.widget.RadioButton[@resource-id="com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_hospital"]'
                    self.driver.find_element_by_android_uiautomator(hospital).click()
                    time.sleep(3)
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")

    def click_doctor(self):
        """
        点击医生
        :return:
        """
        try:
            time.sleep(3)
            doctor = "com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_expert"
            self.driver.find_element_by_id(doctor).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                doctor = '//android.widget.RadioButton[@text="医生"]'
                self.driver.find_element_by_xpath(doctor).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    doctor = '//android.widget.RadioButton[@resource-id="com.wanmeizhensuo.zhensuo:id/commonSearchResult_rb_expert"]'
                    self.driver.find_element_by_android_uiautomator(doctor).click()
                    time.sleep(3)
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")
                    time.sleep(5)

    def click_shopping_cart(self):
        """
        点击美购首页、购物车
        :return:
        """
        try:
            time.sleep(3)
            shopping = "com.wanmeizhensuo.zhensuo:id/common_red_iv"
            self.driver.find_element_by_id(shopping).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                shopping = 'com.wanmeizhensuo.zhensuo:id/titleBarWelfareHome_rl_shopping_cart'
                self.driver.find_element_by_id(shopping).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    shopping = '//android.widget.RelativeLayout[@resource-id="com.wanmeizhensuo.zhensuo:id/common_red_iv"]'
                    self.driver.find_element_by_android_uiautomator(shopping).click()
                    time.sleep(3)
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")
                    time.sleep(5)

    def click_welfare_home_search(self):
        """
        点击美购首页搜索
        :return:
        """
        #  点击搜索
        try:
            time.sleep(3)
            search_id = "com.wanmeizhensuo.zhensuo:id/titleBarWelfareHome_rl_Search"
            self.driver.find_element_by_id(search_id).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                desc_class = '//android.widget.LinearLayout[@resource-id="com.wanmeizhensuo.zhensuo:id/titleBarWelfareHome_rl_Search"]'
                self.driver.find_element_by_xpath(desc_class).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    search_id = "com.wanmeizhensuo.zhensuo:id/titleBarWelfareHome_rl_Search"
                    self.driver.find_element_by_id(search_id).click()
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 2))
                finally:
                    print("继续下一步")

