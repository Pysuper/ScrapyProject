# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaohuaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()

    cate_1_title = scrapy.Field()
    cate_1_url = scrapy.Field()

    cate_2_title = scrapy.Field()
    cate_2_url = scrapy.Field()

    cate_3_title = scrapy.Field()
    cate_3_url = scrapy.Field()

    file_title = scrapy.Field()
    file_url = scrapy.Field()
