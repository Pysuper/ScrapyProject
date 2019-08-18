from pymongo import *
from pprint import pprint
from tencent.items import TencentItem, DetailItem


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


class MongodbListItemPipeline(object):
    """MongoDB管道 ==> 存储列表页数据"""

    def open_spider(self, spider):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.tencent

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):  # 对不同的item进行判断, 属于不同的模型类
            self.db.listitem.insert(dict(item))
        return item


class MongodbDetailItemPipeline(object):
    """MongoDB管道 ==> 存储详情页数据"""

    def open_spider(self, spider):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.tencent

    def process_item(self, item, spider):
        if isinstance(item, DetailItem):  # 对不同的item进行判断, 属于不同的模型类
            self.db.detailitem.insert(dict(item))
        return item
