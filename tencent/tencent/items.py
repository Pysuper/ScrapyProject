import scrapy


class TencentItem(scrapy.Item):
    Name = scrapy.Field()    # 岗位名称
    Location = scrapy.Field()   # 位置
    BG = scrapy.Field() #
    Category = scrapy.Field()   # 分类
    Responsibility = scrapy.Field() # 描述
    Time = scrapy.Field() # 发布日期
    URL = scrapy.Field()    # 跳转链接
