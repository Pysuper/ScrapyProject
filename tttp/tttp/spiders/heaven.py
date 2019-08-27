# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HeavenSpider(CrawlSpider):
    name = 'heaven'
    allowed_domains = ['ivsky.com']
    start_urls = ['http://ivsky.com/']

    # 链接提取器
    all_cate = LinkExtractor(restrict_xpaths='')

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
