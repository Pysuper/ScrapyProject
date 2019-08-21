# -*- coding: utf-8 -*-
import json

import scrapy
from tencent.items import ZhiTongItem


class ZhitongSpider(scrapy.Spider):
    name = 'zhitong'
    page = 0
    allowed_domains = ['www.job5156.com']
    start_urls = ["http://www.job5156.com/s/result/ajax.json?pageNo=", ]

    def parse(self, response):
        result_list = json.loads(response.text)['page']['items']
        if len(result_list) > 0:
            for result in result_list:
                item = ZhiTongItem()
                item['name'] = result['posName']
                item['salary'] = result['salaryStrByThousandMonth']
                item['company_name'] = result['comInfo']['comName']
                item['requirement_key'] = ', '.join(result['taoLabelList'])
                item['key_word'] = result['comInfo']['taoLabel']
                item['location_detail'] = result['workLocationList'][0]['provName'] + result['workLocationList'][0]['cityName'] + result['workLocationList'][0]['townName']
                item['location'] = result['workLocationsStr']
                item['company_info'] = result['comInfo']['companyIntroduction'].replace('\n', '').replace('\u3000', '').strip()
                item['scale'] = result['comInfo']['employeeNumStr']
                item['company_location'] = result['comInfo']['locationStr']
                item['nature'] = result['comInfo']['propertyStr']
                item['requirement'] = result['posDesc'].replace('\n', '').replace('\r', '').strip()
                yield item
            self.page = self.page + 1
            yield scrapy.Request(
                url=self.start_urls[0] + str(self.page),
            )
