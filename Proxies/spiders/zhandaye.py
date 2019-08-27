import re
import requests
from lxml import etree


class ZhandayeProxySpider(object):
    """
    站大爷
    """

    headers = {
        "Referer": "http://ip.zdaye.com/dayProxy.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    }

    def get_url_list(self):
        return ["http://ip.zdaye.com/dayProxy/{}.html".format(i) for i in range(1, 10)]

    def get_detail_url(self):
        for url in self.get_url_list():
            response = requests.get(url, headers=self.headers)
            data = etree.HTML(response.text)
            url_end_list = data.xpath('//h3/a/@href')
            for detail_url in url_end_list:
                yield "http://ip.zdaye.com/" + detail_url

    def get_proxies(self):
        for url in self.get_detail_url():
            response = requests.get(url, headers=self.headers)
            data = etree.HTML(response.text)
            rows = data.xpath('//div[@class="cont"]/text()')
            for row in rows:
                item = re.match(r'(.*?)@(\w+)', row)
                ip = item.group(2)
                port = item.group(1)
                yield "{}://{}".format(ip, port)
                # print("{}://{}".format(ip, port))

# daili66 = ZhandayeProxySpider()
# daili66.get_proxies()
