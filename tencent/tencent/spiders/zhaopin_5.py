import json
import scrapy
from tencent.items import TencentItem, DetailItem


class ZhaopinSpider(scrapy.Spider):
    name = 'tencent_5'
    allowed_domains = ['tencent.com']
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566111052462&pageSize=10&language=zh-cn&area=cn&pageIndex={}'

    def start_requests(self):
        """
        引擎会自动回调这个方法, 提供给引擎首次请求的URL列表
        :return:
        """
        for page in range(1, 489):
            yield scrapy.Request(
                url=self.base_url.format(page),
            )
            # break  # 测试

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
            # item["Responsibility"] = info["Responsibility"].replace("\n", "").replace("\r", "").strip()
            item["Time"] = info["LastUpdateTime"]
            # yield item  # 返回数据对象

            detail_info = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId='
            post_id = info["PostId"]
            yield scrapy.Request(
                url=detail_info + post_id,
                callback=self.parse_detail,  # 设置回调解析函数, 这里发送的request请求对象, parse()解析函数处理不了这里的请求
                meta={"item": item},    # 用meta携带item, response.meta, 字典类型
                dont_filter=False   # 如果请求发送过了, 是否过滤
            )
            # break  # 测试

    def parse_detail(self, response):
        """
        详情页解析函数
        :param request:
        :return:
        """
        response_dict = json.loads(response.text)
        item = response.meta["item"]
        item["Responsibility"] = response_dict["Data"]["Responsibility"].replace("\n", "").replace("\r", "").strip()
        item["Requirement"] = response_dict["Data"]["Requirement"].replace("\n", "").replace("\r", "").strip()
        yield item
