import requests
from lxml import etree


class IP89ProxySpider(object):
    """
    89免费代理
    """

    def get_url_list(self):
        return ["http://www.89ip.cn/index_{}.html".format(i) for i in range(1, 7)]

    def get_proxies(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        }
        for url in self.get_url_list():
            response = requests.get(url, headers=headers)
            data = etree.HTML(response.text)
            rows = data.xpath('//table//tr')
            for idx in range(2, len(rows)):
                row = rows[idx]
                ip = row.xpath('./td[1]/text()')[0].strip()
                port = row.xpath('./td[2]/text()')[0].strip()
                yield "http://{}:{}".format(ip, port)
                yield "https://{}:{}".format(ip, port)
                # print("http://{}:{}".format(ip, port))

# daili66 = IP89ProxySpider()
# daili66.get_proxies()
