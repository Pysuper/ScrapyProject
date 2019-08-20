# -*- coding: utf-8 -*-
import json

import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        base_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'
        for page in range(0, 100, 20):
            yield scrapy.Request(
                url=base_url.format(page)
            )

    def parse(self, response):
        result = json.loads(response.text)
        for data in result["subjects"]:
            print(data)
        pass
