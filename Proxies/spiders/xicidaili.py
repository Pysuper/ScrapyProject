import requests
from lxml import etree


class XiCiIPSPider():
    """
    西刺代理
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

    def grt_url_list(self):
        return ["https://www.xicidaili.com/nn/{}".format(page) for page in range(1, 100)]

    def get_proxies(self):
        for url in self.grt_url_list():
            response = requests.get(url=url, headers=self.headers)
            data = etree.HTML(response.text)
            tr_list = data.xpath('//table/tr')[1:]
            for tr in tr_list:
                ip = tr.xpath('./td[2]/text()')[0]
                port = tr.xpath('./td[3]/text()')[0]
                cate = tr.xpath('./td[6]/text()')[0]
                yield "{}://{}:{}".format(cate, ip, port)
                # print("{}://{}:{}".format(cate, ip, port))


# xici = XiCiIPSPider()
# xici.get_proxies()
