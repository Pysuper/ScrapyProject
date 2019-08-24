import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meizitu.items import MeizituItem


class MeiziCrawlSpider(CrawlSpider):
    name = 'meizi_crawl'
    allowed_domains = ['mzitu.com', 'sinaimg.cn', 'meizitu.net']
    start_urls = ['https://www.mzitu.com/']

    # 提取规则
    cate_title = LinkExtractor(restrict_xpaths=('//ul[@class="menu"]/li/a'))
    cate_group = LinkExtractor(restrict_xpaths=('//ul[@id="pins"]/li/a'))
    cate_group_next = LinkExtractor(restrict_xpaths=('//a[text()="下一页»"]'))
    cate_group_img_next = LinkExtractor(restrict_xpaths=('//span[text()="下一页»"]/..'))
    cate_pai_next = LinkExtractor(restrict_xpaths=('//a[text()="下一页»"]'))
    rules = (
        Rule(cate_title, follow=True),  # 标题提取
        Rule(cate_group, follow=True),  # 组图提取
        Rule(cate_group_next, follow=True),  # 组图提取
        Rule(cate_group_img_next, callback='parse_item', follow=True),  # 组图下一页提取
        Rule(cate_pai_next,callback='parse_pai', follow=True),  # 下一页提取
    )

    def parse_item(self, response):
        item = MeizituItem()
        item["img_dir"] = response.xpath('//li[@class="current-menu-parent"]/a/text()').extract_first()
        item['img_url'] = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        item['img_dir_2'] = response.xpath('//div[@class="main-image"]/p/a/img/@alt').extract_first()
        item["img_name"] = re.match(r'.*?/\d{2}/(.*\.jpg)', item["img_url"]).group(1)
        yield item

    def parse_pai(self, response):
        if response.xpath('//div[@id="comments"]'):
            img_list = response.xpath('//img[@class="lazy"]')
            for img in img_list:
                item = MeizituItem()
                item["img_dir"] = response.xpath('//li[@class="current-menu-item"]/a/text()').extract_first()
                item['img_dir_2'] = ''
                item["img_url"] = img.xpath('./@data-original').extract_first()
                item["img_name"] = re.findall(r'.*/(.*)', item["img_url"])[-1]
                yield item
