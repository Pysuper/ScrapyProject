# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem

class ItinfoSpider(scrapy.Spider):
    name = 'itinfo'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ac']  # 这时第一个URL(启动URL)

    def parse(self, response):
        # 使用一次xpath, 获取上一级, 不直接获取名字
        div_list = response.xpath('//div[@class="li_txt"]')
        for div in div_list:
            item = ItcastItem()
            item["name"] = div.xpath('./h3/text()').extract_first() # 返回的是一个selector对象列表, 用extract_first拿到第一个
            item["level"] = div.xpath('./h4/text()').extract_first()
            item["description"] = div.xpath('./p/text()').extract_first()
            yield item