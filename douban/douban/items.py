import scrapy


class DoubanItem(scrapy.Item):
    # 自定义模型类
    name = scrapy.Field()
    rate = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()
    img_path = scrapy.Field()
