import scrapy


class MeizituItem(scrapy.Item):
    """自定义模型类"""
    category_1_title = scrapy.Field()
    category_1_href = scrapy.Field()
    group_name = scrapy.Field()
    group_href = scrapy.Field()
    group_2_href = scrapy.Field()
    group_href_urls = scrapy.Field()
    img_url = scrapy.Field()
    img_dir = scrapy.Field()
    img_dir_2 = scrapy.Field()
    img_name = scrapy.Field()
    img_path = scrapy.Field()
