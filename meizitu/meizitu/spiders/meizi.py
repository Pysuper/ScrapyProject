import re

import scrapy
from meizitu.items import MeizituItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['mzitu.com']
    start_urls = ['https://www.mzitu.com/', ]

    def parse(self, response):
        # 获取分类
        li_list = response.xpath("//ul[@id='menu-nav']/li/a")
        for li in li_list:
            item = MeizituItem()
            item['category_1_title'] = li.xpath('./text()').extract_first()
            item['category_1_href'] = li.xpath('./@href').extract_first()
            yield scrapy.Request(
                url=item['category_1_href'],
                callback=self.parse_list,
                meta={'item': item},
                dont_filter=True
            )

    def parse_list(self, response):
        # 获取组图列表
        item = response.meta["item"]
        li_list = response.xpath("//ul[@id='pins']/li/span[1]/a")
        if li_list:
            # 如果有值就请求:
            next_url = response.xpath("//a[text()='下一页»']/@href").extract_first()
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_list,
                meta={'item': item},
                dont_filter=True
            )
            for li in li_list:
                item["group_name"] = li.xpath("./text()").extract_first()
                item["group_href"] = li.xpath("./@href").extract_first()
                yield scrapy.Request(
                    url=item["group_href"],
                    callback=self.parse_detail,
                    meta={'item': item},
                    dont_filter=True
                )
        else:
            # li_list没有值的时候,就是街拍和自拍的 ==> 在这里处理 对于all(每日更新的未处理)
            result_list = response.xpath("//div[@id='comments']/ul/li/div/p/img")
            for result in result_list:
                item["group_name"] = ''
                item["group_href"] = ''
                item['img_url'] = result.xpath("./@data-original").extract_first()
                item["img_name"] = re.findall(r'.*/(.*)', item["img_url"])[-1]
                yield item
                if item['img_url']:  # 有值就是街拍和自拍的
                    next_url = response.xpath("//a[text()='下一页»']/@href").extract_first()
                    if next_url:
                        yield scrapy.Request(
                            url=next_url,
                            callback=self.parse_list,
                            meta={'item': response.meta["item"]},
                            dont_filter=True
                        )

    def parse_detail(self, response):
        # 获取图片信息
        item = response.meta["item"]
        item["img_url"] = response.xpath("//div[@class='main-image']/p/a/img/@src").extract_first()
        item["img_name"] = re.match(r'.*?/\d{2}/(.*\.jpg)', item["img_url"]).group(1)
        next_url = response.xpath("//span[text()='下一页»']/../@href").extract_first()
        yield item
        if next_url is not None:
            while True:
                yield scrapy.Request(
                    url=next_url,
                    callback=self.parse_detail,
                    meta={'item': response.meta["item"]},
                    dont_filter=False
                )


"""
街拍和自拍单独处理
"""
