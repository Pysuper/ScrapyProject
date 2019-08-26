import requests
from lxml import etree


class Daili66ProxySpider(object):
    """
    66免费代理网
    """

    def get_url_list(self):
        return ["http://www.66ip.cn/{}.html".format(i) for i in range(1, 100)]

    def get_proxies(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "Referer": "http://www.66ip.cn/4.html",
            'Cookie': "yd_cookie=9558124d-779f-41e624708e6eb673732cf4b5a0f544c35057; _ydclearance=10ced59c96212a03bfdbbecb-3c78-4880-a153-fbc07b3712be-1542512435"
        }
        for url in self.get_url_list():
            response = requests.get(url, headers=headers)
            edata = etree.HTML(response.text)
            rows = edata.xpath('//table//tr')
            for idx in range(2, len(rows)):
                row = rows[idx]
                ip = row.xpath('./td[1]/text()')[0]
                port = row.xpath('./td[2]/text()')[0]
                yield "http://{}:{}".format(ip, port)
                yield "https://{}:{}".format(ip, port)

                # print("http://{}:{}".format(ip, port))

# daili66 = Daili66ProxySpider()
# daili66.get_proxies()
