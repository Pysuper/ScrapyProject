import scrapy


class JobItem(scrapy.Item):
    # 定制化模型类
    name = scrapy.Field()           # 岗位名称
    job_url = scrapy.Field()        # 详情链接
    company_name = scrapy.Field()   # 公司名称
    company_info = scrapy.Field()   # 公司信息
    location = scrapy.Field()       # 地理位置
    location_work = scrapy.Field()  # 上班地址
    salary = scrapy.Field()         # 薪资
    release_date = scrapy.Field()   # 发布日期
    job_keyword = scrapy.Field()    # 关键字
    job_info = scrapy.Field()       # 职位信息
    functional_category = scrapy.Field()    # 职能类别
