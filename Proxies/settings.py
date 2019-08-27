"""
指定一些全文件的变量
"""

# Redis端口好
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# Redis的Key
PROXIES_REDIS_KEY = "proxies"

# 使用的爬虫列表
PROXIES_SPIDERS = [
    "spiders.89ip.IP89ProxySpider",
    "spiders.xicidaili.XiCiIPSPider",
    "spiders.kuaidaili.KuaidailiSpider",
    "spiders.daili66.Daili66ProxySpider",
    "spiders.yundaili.YundailiProxySpider",
    "spiders.zhandaye.ZhandayeProxySpider",
]
