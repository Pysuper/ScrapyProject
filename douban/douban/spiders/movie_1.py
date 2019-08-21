# -*- coding: utf-8 -*-
import json
import scrapy
from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie_1'
    tag_list = []
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        base_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag={}&sort=recommend&page_limit=20&page_start={}'
        for page in range(0, 320, 20):
            yield scrapy.Request(
                url=base_url.format(page)
            )

    def parse(self, response):
        # 这里处理的是JSON
        result = json.loads(response.text)["subjects"]
        for data in result:
            item = DoubanItem()
            item["name"] = data["title"]
            item["rate"] = data["rate"]
            item["url"] = data["url"]
            item["cover"] = data["cover"]
            yield item
