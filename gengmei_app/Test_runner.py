import os
import unittest
import requests
import time
from gengmei_app.common import HTMLTestRunner_cn

# report_path = os.path.dirname(os.path.realpath(__file__))+'/test_report/'
# now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
#
# HtmlFile = report_path+now+'_result.html'
# print(HtmlFile)
#
# fp = open(HtmlFile, 'wb')
#
# suite = unittest.TestLoader().discover('case', pattern='test*.py')


# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
def add_case(caseName="case_ob", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("title case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case, reportName="test_report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title=u'自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')

    # 调用add_case函数返回值
    res = runner.run(all_case)

    # 异常断定， 钉钉提醒
    error_count = res.error_count
    failure_count = res.failure_count
    number = sum((error_count, failure_count))
    if number != 0:
        dd_url = "https://oapi.dingtalk.com/robot/send?access_token=9449b0e7cb64b3421224532cffb9ec36f413f6a734d085fde83a726939e45936"
        text = "监控报警：更美-app 功能自动化有错误/失败 请及时关注邮件！"
        json_text = {
            "msgtype": "text",
            "at": {
                "atMobiles": [
                    17601625117,
                    18813051576
                    # 变为所有人 这里要改
                    # "all"

                ],
                # 变为true 就会@所有人
                "isAtAll": False
            },
            "text": {
                "content": text
            }
        }
        requests.post(url=dd_url, json=json_text, verify=False)
    else:
        print("全部执行成功啦")

    fp.close()

def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file

if __name__=='__main__':
    all_case = add_case()  # 1加载用例
    run_case(all_case)  # 2执行用例

    # # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")  # 用例文件夹
    # report_file = get_report_file(report_path)  # 3获取最新的测试报告

