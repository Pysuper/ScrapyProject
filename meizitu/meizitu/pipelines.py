from pymongo import MongoClient


class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item


class SaveImagePipeline(object):
    """保存图片"""

    def open_spider(self, spider):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.db = client.meizitu

    def process_item(self, item, spider):
        # 在这里写入图片
        save_path = 'images/' + item["category_1_title"] + '/' + item["img_name"]  # 街拍自拍
        if item["group_name"] != '':  # 分类
            save_path = 'images/' + item["category_1_title"] + '/' + item["group_name"] + '/' + item["img_name"]

        # TODO: 这里有URL, 有save_path, 怎么保存图片?

        item["img_path"] = save_path
        self.db.ing_info.insert(dict(item))
        print(dict(item))
        return item
