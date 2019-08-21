import json
import scrapy
from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie_2'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/search_tags?type=movie&tag=%E7%BB%8F%E5%85%B8&source=', ]
    detail_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag={}&sort=recommend&page_limit=20&page_start='  # page为空也是首页

    def parse(self, response):
        # 获取所有tag
        result = json.loads(response.text)["tags"]
        for tag in result:
            yield scrapy.Request(
                url=self.detail_url.format(tag),
                callback=self.parse_tag,
                dont_filter=True
            )

    def parse_tag(self, response):
        result = json.loads(response.text)["subjects"]
        if len(result) > 0:
            for data in result:
                item = DoubanItem()
                item["name"] = data["title"]
                item["rate"] = data["rate"]
                item["url"] = data["url"]
                item["cover"] = data["cover"]
                yield item
            yield scrapy.Request(
                url=response.url + '20',
                callback=self.parse_tag,
                dont_filter=False,  # 是否过滤
            )
