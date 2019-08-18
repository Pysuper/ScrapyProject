import json
from tencent.items import TencentItem
import scrapy
from math import floor, ceil


class ZhaopinSpider(scrapy.Spider):
    name = 'tencent_1'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566111052462&pageSize=20&language=zh-cn&area=cn&pageIndex=1']

    def parse(self, response):
        """
        获取响应, 触发解析函数, 提取数据, 提取URL
        :param response: 下载==>中央引擎==>爬虫 的response对象
        :return: 数据 URL
        """
        response_dict = json.loads(response.text)
        response_data = response_dict["Data"]
        info_count = response_data["Count"] # 所有显示的条数
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

        # 提取下一页链接, 并且继续请求
        num = ceil(int(info_count) / 20) # 向下取整函数floor和向上取整函数ceil
        for page in range(2, num):
            next_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566111052462&pageSize=20&language=zh-cn&area=cn&pageIndex={}".format(page)

            # 1. 封装成请求对象
            request = scrapy.Request(
                url=next_url
            )

            # 2. 发送给搜索引擎
            yield request