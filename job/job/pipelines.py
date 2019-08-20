"""
自定义管道
"""
from pprint import pprint
from pymongo import MongoClient


class JobPipeline(object):
    def process_item(self, item, spider):
        pprint(dict(item))
        return item

class MongodbJobItemPipeline(object):
    """MongoDB管道 ==> 存储列表页数据"""

    def open_spider(self, spider):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.job

    def process_item(self, item, spider):
        self.db.job.insert(dict(item))
        return item