import os
import time
import json
import redis
from pprint import pprint
from copy import deepcopy

redis_gm = redis.Redis(host='localhost')

def mitm_query(**kwargs):
    '''
    1.这个方法使用一定要执行mitmdump -s maidianRedis.py --listen-port=8899'
    2.手机一定要设备代理  port 8899，代理ip为执行机的ip
    :param kwargs:
    :return:
    '''
    if kwargs:
        action = kwargs.get('action')
        page_name = kwargs.get('page_name')
        from .dbMysql import dev_id
        kwargs['device_id'] = dev_id
        if not any((action, page_name)):
            raise Exception('action,page_name必须传至少一个！')

    #   把redis里的maidian（0，-1）全部取出来
    result = redis_gm.lrange('maidian', 0, -1)


    def inner_filter(data):
        #  设备必须过滤
        data = map(lambda x:json.loads(x),data)
        # a = deepcopy(data)
        # pprint(list(a))
        data = filter(lambda x: x.get('device', {}).get('device_id') == dev_id, data)
        if page_name:
            data = filter(lambda x: x.get('params', {}).get('page_name') == page_name, data)
        if action:
            data = filter(lambda x: x.get('type') == action, list(data))
        #  最后进行去重，ios部分会重复，数据端去重，这里也做去重判断
        _data = []
        for item in data:
            if item not in _data:
                _data.append(item)
        return _data

    filter_result = list(inner_filter(result))
    # 删掉 maidian
    redis_gm.delete('maidian')
    return filter_result
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# port = '8899'
# try:
#
#     os.popen('brew install redis')
#     os.popen('brew services start redis')
#     os.popen('pip3 install mitmproxy')
# except:
#     pass
#
#
# def openmitm():
#     os.popen(f'mitmdump -s {os.path.join(BASE_DIR, "common", "maidianRedis.py")} --listen-port={port}')
#
#
# def closemitm():
#     time.sleep(5)
#     os.system("for i in ` lsof -i:8899|awk '{print $2}'`; do kill -9  $i; done;")
#
#
# if __name__ == '__main__':
#     openmitm()
#
#     closemitm()
