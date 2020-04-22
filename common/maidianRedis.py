from mitmproxy import http
from mitmproxy import ctx  # 这是个日志打印
import json
import logging
import gzip
import requests
import threading
from threading import Lock
import copy
import datetime
import re
import urllib3
import redis
# from base_setting import gray_device_id  #单独启动


urllib3.disable_warnings(Exception)

now = datetime.datetime.now()
ml = logging.Logger('API-LOG')
hd_f = logging.FileHandler(f'api-{now.month}-{now.day}.log', 'a')
kw = {"fmt": "【%(levelname)s %(asctime)s】\n %(message)s", "datefmt": '%Y-%m-%d %X'}
hd_f.formatter = logging.Formatter(**kw)
ml.addHandler(hd_f)

redis_gm = redis.Redis(host='localhost')

__fields__ = ['version', 't', 'channel', 'current_city_id', 'device_id', 'idfa', 'idfv', 'lat', 'lng', 'platform',
              'os_version', 'client_source', 'hybrid', 'json', 'referrer', 'app_name', 'model', 'screen',
              'manufacturer', 'uuid', 'android_device_id']

check_list = [
    r'/api/conversation/detai/\d+_\d+/',
    r'/api/hospitals/\w+/services',
    r'/api/hospitals/\w+/detail',
    r'/api/hospitals/\w+/doctors',
    r'/hybrid/service/richtext/\d+/',
    r'/hybrid/user_fans_or_following/\d+/_data',
    r'/api/doctor/\w+/services',
    r'/api/doctor/\w+/detail',
    r'.*.json',
    r'/api/conversation/detail/w+/'
]

#判断是否有灰度吧

import sys




is_gray = True if sys.argv[-2] == 'gray' else False
if is_gray:
    gray_device_id = sys.argv[-1]

# 先做一层干预
def check_lastway(item):
    return re.match(fr'{"|".join(check_list)}', item)


def maidian(*args, **kwargs):
    pass


def sendding(text):
    json_text = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                '13608913121'
            ],
            "isAtAll": False
        },
    }
    requests.post(
        'https://oapi.dingtalk.com/robot/send?access_token=f2dcfbbf9e1a88e75f3da473a91de07e14759b0550693a348992dcf7270283c1',
        json=json_text, verify=False)


class Gmaddon:
    def __init__(self):
        '''需'''
        self.host_list = ['log.igengmei.com', 'log.test.igengmei.com']

    def request(self, flow: http.HTTPFlow):
        '''do nothing here'''
        #  判断设备id是否灰度，不是灰度设备就替换设备
        if is_gray:
            fields = flow.request.query.fields
            new_fields = tuple((x, y if x != "device_id" else gray_device_id) for x, y in fields)
            flow.request.query.fields = new_fields

        if flow.request.host in self.host_list:
            # 放在redis里面
            d = json.loads(gzip.decompress(flow.request.data.content).decode())
            if isinstance(d, list):
                [redis_gm.lpush('maidian', json.dumps(item)) for item in d]
            elif isinstance(d, dict):
                redis_gm.lpush('maidian', json.dumps(d))



class Mdaddon:
    def __init__(self):
        '''需要再添加'''
        self.host_list = ['backend.igengmei.com',
                          'backend.paas-test.env',
                          'backend-pre.igengmei.com',
                          'backend.paas-week.env',
                          'xcx-week.igengmei.com',
                          'm.paas.env',
                          'm.igengmei.com']
        self.add_list = []
        self._get_had_api()

    def request(self, flow: http.HTTPFlow):
        '''do nothing here'''
        # ctx.log.info(flow.request.path.split('?')[0])

    def response(self, flow: http.HTTPFlow):
        if 'application/json' not in flow.response.headers.get('Content-Type', ''):
            return

        url, host, path, method = flow.request.url, flow.request.host, flow.request.path, flow.request.method
        path = path.split('?')[0]

        # 对code进行一层判断
        if flow.response.status_code != 200:
            sendding(f'====存在code:{flow.response.status_code}报错====\nHost:{host}\nuri:{path}\nMethod:{method}')

        if host in self.host_list:
            ctx.log.info(path)
            threading.Thread(target=self._check_need_record, args=(path, flow.request)).start()

    # 拉取已录入的接口
    def _get_had_api(self):
        # 暂时写死url
        url = 'http://62.234.155.77:8090/testapi/apiconfig'
        _data = requests.get(url).json()
        self.api_had_list = list(_data.values())
        self.api_had_list.extend(self.add_list)

    # 判断是否需要录入
    def _check_need_record(self, source, res: http.HTTPRequest):

        # 判断
        # 对纯数字的和32位长度的进行转{} ---暂时不要
        if check_lastway(source):  # 过滤一下统计的
            return
        source_fmt = source.strip('/\/')
        for item in self.api_had_list:
            item_fmt = item.strip('/\/')
            if source_fmt == item_fmt:
                return
            # 深度对比
            source_list = source_fmt.split('/')
            item_list = item_fmt.split('/')
            if len(source_list) != len(item_list):
                continue
            # 这地方很容易误杀，那么仅对纯数字和超长字母（32位-新的医生和机构）
            for i in range(len(source_list)):
                copy_from_s = copy.deepcopy(source_list)
                if copy_from_s[i].isdigit() or len(copy_from_s[i]) == 32:
                    copy_from_s[i] = '{}'
                else:
                    continue
                if copy_from_s == item_list:  # 存在
                    return

        else:
            url_params = json.dumps({k: v for k, v in dict(res.query).items() if k not in __fields__}, indent=2)
            if res.method == 'GET':
                text = f'出现疑似未录入的接口！\nHost:{res.host}\nuri:{source}\nMethod:{res.method}\nUrl_params(已去除公共封装):\n{url_params}'
            else:
                if "application/json" in res.headers.get('Content-Type', ''):  # 默认是application/x-www-form-urlencoded
                    body = json.loads(res.content)
                else:

                    _body = res.content.decode()
                    body = dict([item.split('=') for item in _body.split('&')])

                body = json.dumps(body, indent=2)
                text = f'出现疑似未录入的接口！\nHost:{res.host}\nuri:{source}\nMethod:{res.method}\nUrl_params(已去除公共封装):\n{url_params}\nRequest_body:\n{body}'
            with Lock():
                ml.warning(text)
                self.api_had_list.append(source)
                self.add_list.append(source)
            sendding(text)
            import random
            if random.random() < 0.2:
                self._get_had_api()


addons = [
    Gmaddon(),
    Mdaddon(),
]
