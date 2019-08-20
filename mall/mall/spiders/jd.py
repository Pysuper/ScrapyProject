import json
import re

import scrapy
from mall.items import MallItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    # 获取首页分类数据
    def parse(self, response):
        """
        extract(): 返回的是一个数组list, 里面包含了多个string, 如果只有一个string, 则返回['ABC']这样的形式
        extract_first(): 返回的是一个string字符串, 是list数组里面的第一个字符串
        """
        cate_1_list = response.xpath('//li[@class="cate_menu_item"]/a')
        for cate_1 in cate_1_list:
            cate_1_title = cate_1.xpath('./text()').extract_first()
            cate_1_href = cate_1.xpath('./@href').extract_first()

            # print(cate_1_title, cate_1_href)  # //imall.jd.com/ 工业品
            item = MallItem()
            item["cate_1_title"] = cate_1_title
            item["cate_1_href"] = cate_1_href
            yield scrapy.Request(
                url="https://dc.3.cn/category/get?&callback=getCategoryCallback",   # 数据在pc.js的文件中，每次请求js返回书
                callback=self.parse_detail,
                meta={"item": item},
                dont_filter=True
            )
            break

    def parse_detail(self, response):
        print(response.text.encode('GBK'))
#