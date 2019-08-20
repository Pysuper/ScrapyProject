import scrapy


class MallItem(scrapy.Item):
    """
    自定义模型类
    """
    cate_1_title = scrapy.Field()
    cate_1_href = scrapy.Field()
    cate_2_title = scrapy.Field()
    cate_2_href = scrapy.Field()
