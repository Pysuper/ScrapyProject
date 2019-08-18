import json
from tencent.items import TencentItem
import scrapy
from math import floor, ceil


class ZhaopinSpider(scrapy.Spider):
    name = 'tencent_2'
    allowed_domains = ['tencent.com']
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566111052462&pageSize=10&language=zh-cn&area=cn&pageIndex={}'
    # start_url = [base_url.format(page) for page in range(1, 489)] # 这样为什么不行
    start_url = []
    for page in range(1, 489):
        start_url.append(base_url.format(page))

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
