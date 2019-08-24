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
            break

    def parse_list(self, response):
        # 获取组图列表
        # item = response.meta["item"]
        li_list = response.xpath("//ul[@id='pins']/li/span[1]/a")
        if li_list:
            # # 如果有值就请求: 获取下一页
                # next_url = response.xpath("//a[text()='下一页»']/@href").extract_first()
            # yield scrapy.Request(
            #     url=next_url,
            #     callback=self.parse_list,
            #     meta={'item': response.meta["item"]},
            #     dont_filter=True
            # )
            for li in li_list:
                item = response.meta["item"]
                item["group_name"] = li.xpath("./text()").extract_first()
                item["group_href"] = li.xpath("./@href").extract_first()
                yield scrapy.Request(
                    url=li.xpath("./@href").extract_first(),
                    callback=self.parse_group,
                    meta={'item': item},
                    dont_filter=True
                )
        else:
            pass
            # 获取下一页
            # next_url = response.xpath("//a[text()='下一页»']/@href").extract_first()
            # if next_url:
            #     yield scrapy.Request(
            #         url=next_url,
            #         callback=self.parse_list,
            #         meta={'item': response.meta["item"]},
            #         dont_filter=True
            #     )
            # li_list没有值的时候,就是街拍和自拍的 ==> 在这里处理 对于all(每日更新的未处理)
            # image_urls = response.xpath("//div[@id='comments']/ul/li/div/p/img/@data-original").extract()
            # for image_url in image_urls:
            #     item = response.meta["item"]
            #     item["group_name"] = ''
            #     item["group_href"] = ''
            #     item["img_url"] = image_url
            #     yield item

    def parse_group(self, response):
        # 获取图片信息
        max_page = response.xpath("//div[@class='pagenavi']/a")[-2].xpath("./span/text()").extract_first()
        for page in range(1, int(max_page) + 1):
            item = response.meta["item"]
            item["group_2_href"] = item["group_href"] + '/' + str(page)
            yield item
            yield scrapy.Request(
                url=item["group_2_href"],
                callback=self.parse_group_image,
                meta={'item': item},
                dont_filter=False
            )

    def parse_group_image(self, response):
        item = response.meta["item"]
        item["img_url"] = response.xpath("//div[@class='main-image']/p/a/img/@src").extract_first()
        item["img_name"] = re.match(r'.*?/\d{2}/(.*\.jpg)', item["img_url"]).group(1)
        # yield item
