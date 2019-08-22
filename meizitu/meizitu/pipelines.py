import os
import re
import time

import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class MeizituPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item


class SaveImagePipeline(ImagesPipeline):
    """保存图片"""

    def get_media_requests(self, item, info):
        # 在发送下载请求之前调用，其实这个方法本身就是去发送下载请求的
        # print("save_image", item)
        if not os.path.exists('images'):
            os.mkdir('images')
        if not os.path.exists('images' + '/' + item["category_1_title"]):
            os.mkdir('images' + '/' + item["category_1_title"])
        if item["group_name"] == '':  # 自拍
            if not os.path.exists('images' + '/' + item["category_1_title"] + '/' + item["group_name"]):
                os.mkdir('images' + '/' + item["category_1_title"] + '/' + item["group_name"])
            for url in item["group_href_urls"]:
                item["img_url"] = url
                item["img_name"] = re.findall(r'.*/(.*)', url)[-1]
                item["img_path"] = item["category_1_title"] + '/' + item["group_name"] + '/' + item["img_name"]
                yield scrapy.Request(
                    url=url,
                    meta={"item": item},
                    dont_filter=True
                )
                time.sleep(1)

        # save_path = item["category_1_title"] + '/' + item["img_name"]  # 街拍自拍
        # if item["group_name"] != '':  # 分类
        #     save_path = item["category_1_title"] + '/' + item["group_name"] + '/' + item["img_name"]
        # item["img_path"] = save_path
        # yield scrapy.Request(
        #     url=item["img_url"],
        #     meta={"item": item},
        #     dont_filter=False
        # )
        # print(save_path, '----下载完成', item)
        # time.sleep(5)

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
