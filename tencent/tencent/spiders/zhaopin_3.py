import json
from tencent.items import TencentItem
import scrapy
from math import floor, ceil


class ZhaopinSpider(scrapy.Spider):
    name = 'tencent_3'
    allowed_domains = ['tencent.com']
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566111052462&pageSize=10&language=zh-cn&area=cn&pageIndex={}'

    def start_requests(self):
        """
        引擎会自动回调这个方法, 提供给引擎首次请求的URL列表
        :return:
        """
        # return [self.base_url.format(page) for page in range(1, 489)]  # 这样为什么不行
        """写法一
        request_list = []
        for page in range(1, 489):
            request = scrapy.Request(
                url=self.base_url.format(page)
            )
            request_list.append(request)
        return request_list
        """

        """写法二"""
        for page in range(1, 489):
            yield scrapy.Request(
                url=self.base_url.format(page),
                # 如果请求时POST请求, 在这里添加两个参数返回给中央引擎
                # method="POST",
                # meta="",
            )

    def parse(self, response):
        """
        获取响应, 触发解析函数, 提取数据, 提取URL
        :param response: 下载==>中央引擎==>爬虫 的response对象
        :return: 数据 URL
        """
        response_dict = json.loads(response.text)
        response_data = response_dict["Data"]
        info_count = response_data["Count"]  # 所有显示的条数
        for info in response_data["Posts"]:
            item = TencentItem()
            item["Name"] = info["RecruitPostName"]
            item["Location"] = info["CountryName"] + info["LocationName"]
            item["BG"] = info["BGName"]
            item["Category"] = info["CategoryName"]
            item["Responsibility"] = info["Responsibility"]
            item["Time"] = info["LastUpdateTime"]
            item["URL"] = info["PostURL"]
            yield item
