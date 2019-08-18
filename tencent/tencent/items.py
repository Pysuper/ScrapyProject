import scrapy


class TencentItem(scrapy.Item):
    Name = scrapy.Field()  # 岗位名称
    Location = scrapy.Field()  # 位置
    BG = scrapy.Field()  #
    Category = scrapy.Field()  # 分类
    Time = scrapy.Field()  # 发布日期
    URL = scrapy.Field()  # 跳转链接


class DetailItem(scrapy.Item):
    """对于详情页的信息, 新建一个模型"""
    Responsibility = scrapy.Field()  # 描述
    Requirement = scrapy.Field()  # 岗位需求
