import scrapy


class TencentItem(scrapy.Item):
    Name = scrapy.Field()  # 岗位名称
    Location = scrapy.Field()  # 位置
    BG = scrapy.Field()  #
    Category = scrapy.Field()  # 分类
    Time = scrapy.Field()  # 发布日期
    URL = scrapy.Field()  # 跳转链接
    Responsibility = scrapy.Field()  # 描述
    Requirement = scrapy.Field()  # 岗位需求


class DetailItem(scrapy.Item):
    """对于详情页的信息, 新建一个模型"""
    Responsibility = scrapy.Field()  # 描述
    Requirement = scrapy.Field()  # 岗位需求

class ZhiTongItem(scrapy.Item):
    # 智通人才网模型类
    name = scrapy.Field()           # 名字
    salary = scrapy.Field()         # 薪资
    company_name = scrapy.Field()   # 公司名
    requirement = scrapy.Field()    # 要求
    requirement_key = scrapy.Field()    # 要求字段
    key_word = scrapy.Field()       # 关键字
    location = scrapy.Field()       # 位置
    location_detail = scrapy.Field()# 位置
    company_info = scrapy.Field()   # 公司简介
    category = scrapy.Field()       # 行业
    scale = scrapy.Field()          # 规模
    company_location = scrapy.Field()# 公司地址
    nature = scrapy.Field()         # 性质
    position = scrapy.Field()       # 当前职位

