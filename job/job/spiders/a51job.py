import scrapy
from job.items import JobItem
from urllib.parse import quote


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['search.51job.com']
    keyword = "python web"  # 去掉指定的岗位名称，全部数据10万条
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,1.html?'.format(quote(quote(keyword)))]

    def parse(self, response):
        """
        处理列表页数据
        :param response: 下载器response对象==>中央引擎==>spider
        :return:
        """
        # 先拿到正确的div列表 ==> 可以使用CSS样式选择器
        div_list = response.xpath('//div[@class="el"]')[4:]
        for div in div_list:
            item = JobItem()
            item["name"] = div.xpath('./p/span/a/text()').extract_first().strip()
            item["job_url"] = div.xpath('./p/span/a/@href').extract_first()
            item["company_name"] = div.xpath('./span[1]/a/text()').extract_first()
            item["location"] = div.xpath('./span[2]/text()').extract_first()
            item["salary"] = div.xpath('./span[3]/text()').extract_first()
            item["release_date"] = div.xpath('./span[4]/text()').extract_first()
            yield scrapy.Request(
                url=item["job_url"],
                callback=self.parse_detail,
                meta={"item": item},
                dont_filter=True,
            )
            # break  # 测试
        yield scrapy.Request(
            url=response.xpath('//a[text()="下一页"]/@href').extract_first()
        )

    def parse_detail(self, response):
        """
        处理详情页信息
        :param response: parse请求==>中央引擎==>下载器==>response对象
        :return: item对象
        """
        div_list = response.xpath('//div[@class="tCompany_main"]')
        for div in div_list:
            item = response.meta["item"]
            item["job_info"] = ''.join(div.xpath('./div[1]/div[1]/p/text()').extract())
            if item["job_info"] is None:
                item["job_info"] = ''.join(div.xpath('./div[1]/div[1]/p/span/text()').extract().strip())

            item["functional_category"] = div.xpath('./div[1]/div[1]/div[1]/p[1]/a/text()').extract_first()
            if item["functional_category"]:
                item["functional_category"].replace("\n", "").replace("\t", "").replace("\r", "").strip()  # 替换和去除空格

            item["job_keyword"] = ', '.join(div.xpath('./div[1]/div[1]/div[1]/p[2]/a/text()').extract())
            item["location_work"] = div.xpath('./div[2]/div/p/text()').extract_first().strip()
            item["company_info"] = div.xpath('./div[3]/div/text()').extract_first().strip()
            yield item
