# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 下午7:22
# @Author  : Zheng Xingtao
# @File    : taohua.py


from taohua.items import TaohuaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider


class TaoHuaSpider(Spider):
    name = 'taohua_2'
    allowed_domains = ['http://thzd.cc']
    start_urls = ['http://thzd.cc/forum.php']

    cate_title = LinkExtractor(restrict_xpaths=("//div[@id='levnav']/ul[1]"))
    rules = (
        Rule(cate_title, follow=True),  # 标题提取
    )

    def parse_item(self, response):
        item = TaohuaItem()
        print(response.xpath('/li/a/text()').extract_first())
        # item["cate_1_title"] = response.xpath('/li/a/text()').extract_first()
        # print(dict(item))

        return

    # def parse_pai(self, response):
    #     if response.xpath('//div[@id="comments"]'):
    #         img_list = response.xpath('//img[@class="lazy"]')
    #         for img in img_list:
    #             item = TaohuaItem()
    #             item["img_dir"] = response.xpath('//li[@class="current-menu-item"]/a/text()').extract_first()
    #             item['img_dir_2'] = ''
    #             item["img_url"] = img.xpath('./@data-original').extract_first()
    #             item["img_name"] = re.findall(r'.*/(.*)', item["img_url"])[-1]
    #             yield item