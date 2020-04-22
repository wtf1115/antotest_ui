from appium import webdriver
import os
import unittest
from gengmei_app.page import canshu

apk_path = os.path.dirname(os.path.abspath("."))


class Testtodolist(unittest.TestCase):
       def setUp(self):
           desired_caps = {}
           desired_caps['platformName'] = 'Android'
           desired_caps['platformVersion'] = '6.0'
           desired_caps['deviceName'] = 'LE67A06380055679' # 小米：4da5b6b6
           desired_caps['androidDeviceReadyTimeout'] = '20'
           desired_caps['sessionOverride'] = True
           desired_caps['noReset'] = True
           desired_caps['appPackage'] = 'com.wanmeizhensuo.zhensuo'  # 程序包名
           desired_caps['appActivity'] = 'com.wanmeizhensuo.zhensuo.module.personal.ui.SplashActivity'  # 启动类名 com.wanmeizhensuo.zhensuo.module.personal.ui.SplashActivity
           desired_caps['unicodeKeyboard'] = True  # 安装一个中文输入法
           desired_caps['waitappActivity'] = '.module.personal.ui.SplashActivity'
           desired_caps['noReset'] = True
           self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

       def tearDown(self):

            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
