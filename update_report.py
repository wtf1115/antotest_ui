# 核心思想就是把最新的FIELDS获取到
from BeautifulReport import BeautifulReport
import sys
import unittest
import os
import pickle
from copy import deepcopy

BASE_DIR = os.path.dirname(__file__)


def get_module(case, testsuits, targetlists, error_flag=False):
    first_class = case._tests[0]
    if isinstance(first_class, unittest.loader._FailedTest):
        # print(f'<{first_class._testMethodName + ".py"}> load failed，please check ！', )
        print(f'<{first_class.__module__}> 加入队列，准备执行！')
        testsuits.addTests(case)
    sec_class = first_class._tests[0]
    if error_flag:
        if sec_class.__class__.__name__ in targetlists:
            print(f'<{sec_class.__module__}> 加入队列，准备执行！')
            testsuits.addTests(case)
    else:
        if sec_class.__class__.__name__ not in targetlists:
            print(f'<{sec_class.__module__}> 加入队列，准备执行！')
            testsuits.addTests(case)


if __name__ == '__main__':
    args = sys.argv[1:]  # 0是 update_report.py本身
    # 可以指定跑某些错误的，python update_report.py xxx.py yyy.py zzz.py
    # 也可以直接跑所有错误的 python update_report.py
    if len(args) == 0 or args[0] == '--help':
        print('''
        ===单个暂时不支持指定case类和方法===
        
1. 支持指定脚本（多个或单个）
   >>>> python update_report.py xxx.py yyy.py zzz.py
     
2. 支持连跑所有错误的脚本
   >>>> python update_report.py --error
   
3. 支持连跑所有的新增的脚本
   >>>> python update_report.py --new
        ''')
    else:
        testsuits = unittest.TestSuite()
        all_suites = unittest.defaultTestLoader.discover(os.path.join(BASE_DIR, 'case'), pattern='test_*.py',
                                                         top_level_dir='case')
        # 获取所有的错误信息
        try:
            with open('fields_data', 'rb') as f:
                total_fields = pickle.load(f)
        except FileNotFoundError:
            total_fields = {}

        res_total = total_fields.get('testResult', [])
        errorlists = [x.get('className') for x in res_total if x.get('status') == '失败']
        hadlists = [x.get('className') for x in res_total]

        if args[0] == '--error':
            # 逆推，奶奶的，麻烦啊
            for case in all_suites:
                get_module(case, testsuits, errorlists, error_flag=True)
        elif args[0] == '--new':
            for case in all_suites:
                get_module(case, testsuits, hadlists)
        else:
            # 然后discover脚本
            args = list(map(lambda x: x + '.py' if not x.endswith('.py') else x, args))
            for case in args:
                _unit = unittest.defaultTestLoader.discover(os.path.join(BASE_DIR, 'case'), pattern=case,
                                                            top_level_dir=os.path.join(BASE_DIR, 'case'))
                if not _unit._tests:
                    print(f'<{case}> not be found，please check ！')
                    continue

                if _unit._tests:
                    testsuits.addTests(_unit)
        print(testsuits)
        beaut = BeautifulReport(testsuits)

        beaut.suites.run(beaut)  # 运行指定的脚本
        fields = beaut.stopTestRun()  # 提取dict
        # 我们主要是对 testFail testAll  testPass testResult进行更新
        # 先获取之前的fileds
        try:
            with open('fields_data', 'rb') as f:
                total_fields = pickle.load(f)
        except FileNotFoundError:
            total_fields = {}
        else:
            total_fields = total_fields or {}
        if not total_fields:
            total_fields = fields
        else:
            old_data = deepcopy(total_fields)
            for res_sub in fields['testResult']:
                for index, item in enumerate(old_data['testResult']):
                    if res_sub['className'] == item['className'] and res_sub['methodName'] == item['methodName']:
                        total_fields['testResult'][index] = res_sub
                        if res_sub['status'] != item['status']:
                            if res_sub['status'] == '成功':
                                total_fields['testPass'] += 1
                                total_fields['testFail'] -= 1
                            else:
                                total_fields['testPass'] -= 1
                                total_fields['testFail'] += 1
                        break
                else:
                    # 如果没有匹配的就插入一个
                    total_fields['testResult'].append(res_sub)
                    total_fields['testAll'] += 1
                    if res_sub['status'] == '成功':
                        total_fields['testPass'] += 1
                    else:
                        total_fields['testFail'] += 1
        beaut.log_path = 'test_report'
        beaut.filename = '最新的测试报告.html'
        beaut.FIELDS = total_fields
        beaut.output_report()
        # 最后更新一下
        with open('fields_data', 'wb') as f:
            pickle.dump(total_fields, f)
