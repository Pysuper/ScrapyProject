import os

import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item


class SaveImagePipeline(ImagesPipeline):
    """保存图片"""

    # def get_media_requests(self, item, info):
    #     # 在发送下载请求之前调用，其实这个方法本身就是去发送下载请求的
    #     yield scrapy.Request(url=item["img_url"], meta={"item": item})

    def item_completed(self, results, item, info):
        """
        esults是一个list 第一个为图片下载状态,对应OK  第二个是一个tupled其中可以为path的字段对应存储路径,而item['front_image_path']是我们自定义字段,保存在item中
        :param results:
        :param item:
        :param info:
        :return:
        """
        if not os.path.exists('images'):
            os.mkdir('images')
        if not os.path.exists('images' + '/' + item["category_1_title"]):
            os.mkdir('images' + '/' + item["category_1_title"])
        if item["group_name"] != '':  # 区分分类和自拍
            if not os.path.exists('images' + '/' + item["category_1_title"] + '/' + item["group_name"]):
                os.mkdir('images' + '/' + item["category_1_title"] + '/' + item["group_name"])

        save_path = 'images/' + item["category_1_title"] + '/' + item["img_name"]  # 街拍自拍
        if item["group_name"] != '':  # 分类
            save_path = 'images/' + item["category_1_title"] + '/' + item["group_name"] + '/' + item["img_name"]
        item["img_path"] = save_path
        return item

    def get_media_requests(self, item, info):
        # 在发送下载请求之前调用，其实这个方法本身就是去发送下载请求的
        yield scrapy.Request(url=item["img_url"], meta={"item": item})

    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        save_path = item["img_path"]
        return save_path


class MongoDBPipeline(object):
    """写入数据库"""

    def open_spider(self, spider):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.meizitu

    def process_item(self, item, spider):
        self.db.ing_info.insert(dict(item))
        return item
