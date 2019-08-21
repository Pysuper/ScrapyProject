import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item


"""
资源下载:
    1. 让管道 继承自 ImagePipeline
    2. 实现2个方法
        get_media_requests 提交资源url请求对象
        item_completed 当资源请求下载完成时回调，参数中携带本地保存的地址路径
    3. 在 settings.py 中配置 IMAGES_STORE 参数表示资源下载的路径
        注意：IMAGES_STORE 配置写错，管道就不会加载成功
    4. 在 settings.py 中开启管道
"""


# 使用scrapy原生的image下载中间件
class DoubanImagePipeline(ImagesPipeline):

    # 开启scrapy时候执行，配置MongoDB连接
    def open_spider(self, spider):
        super(DoubanImagePipeline, self).open_spider(spider)
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.douban

    # 告诉引擎需要下载图片数据
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item["cover"]
        )

    # 当下载完成后执行的方法
    def item_completed(self, results, item, info):
        data = [result for ok, result in results if ok][0]
        item["img_path"] = data["path"]
        print(dict(item))
        self.db.items.insert(dict(item))
