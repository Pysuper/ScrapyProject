from pprint import pprint
from pymongo import *


class TencentPipeline(object):
    def process_item(self, item, spider):
        """
        接收中央引擎的item对象, 通过管道处理, 返回
        :param item: 数据: 爬虫==>中央引擎==>数据队列
        :param spider:
        :return:
        """
        pprint(dict(item))
        return item


class MongodbPipeline(object):
    """MongoDB管道"""

    def open_spider(self, spider):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.tencent

    def process_item(self, item, spider):
        self.db.items.insert(dict(item))
