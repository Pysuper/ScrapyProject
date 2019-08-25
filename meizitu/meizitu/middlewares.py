import random
from scrapy import signals
from meizitu.settings import PROXIES_LIST


def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


# 爬虫中间件-模板代码
class MeizituSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        """
        当爬虫被创建时回调
        :param crawler:
        :return:
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        当引擎把响应交给爬虫时回调
        :param response:
        :param spider:
        :return:
            None: 把请求继续向下传递
            引发异常: 触发 process_spider_exception 函数
        """
        return None

    def process_spider_output(self, response, result, spider):
        """
        当爬虫组件把数据或者url提交给引擎时回调
        :param response:
        :param result:
        :param spider:
        :return:
        """
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """
        当爬虫组件把数据或者url提交给引擎时(process_spider_input)回调异常的时候, 执行这个回调函数
        :param response:
        :param exception:
        :param spider:
        :return:
        """
        pass

    def process_start_requests(self, start_requests, spider):
        """
        当引擎从爬虫获取启动URL(start_url)时回调
        :param start_requests:
        :param spider:
        :return:
        """
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        """
        当爬虫初始化时回调
        :param spider:
        :return:
        """
        spider.logger.info('Spider opened: %s' % spider.name)


# 下载中间件-模板代码
class MeizituDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        """当爬虫被创建时回调"""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        当引擎把请求提交给下载器时回调
        :param request:
        :param spider:
        :return:
            None: 继续执行请求
            Response: 响应对象, 返回给引擎-->交给爬虫
            Request: 请求对象, 返回给引擎-->交给请求调度器
            引发异常 IgnoreRequest: 回调 process_exception 函数
        """
        return None

    def process_response(self, request, response, spider):
        """
        当下载组件把response响应交给引擎时回调
        :param request:
        :param response:
        :param spider:
        :return:
            Response: 响应对象, 把响应交给引擎--> 爬虫组件
            Request: 请求对象, 把响应交给引擎--> 请求调度器
            引发 IgnoreRequest 异常: 忽略这个响应 ==> 在爬虫里面回调errback
        """
        return response

    def process_exception(self, request, exception, spider):
        """
        当下载中间件引发异常时回调
        :param request:
        :param exception:
        :param spider:
        :return:
            None: 把异常继续向下传递, 给下一个中间件(触发process_exception)
            Response: 相应对象, 终止把异常传递给下一个中间件, 把响应交给引擎-->爬虫
            Request: 请求对象, 终止把异常传递给下一个中间件, 把请求交给引擎-->请求调度器
        """
        pass

    def spider_opened(self, spider):
        """
        当爬虫被打开时回调, 初始化一些内容的时候可以放在这里(链接数据库)
        :param spider:
        :return:
        """
        spider.logger.info('Spider opened: %s' % spider.name)


"""
编写中间件
1. 实现中间件代码
2. 在settings.py中配置启动中间件
"""


class RandomUserAgentDownloaderMiddleware(object):
    """
    设置随机User-Agent
    """

    def process_request(self, request, spider):
        request.headers["User-Agent"] = get_ua()
        return None


class RandomProxyDownloaderMiddleware(object):
    """
    设置随机IP
    """

    def process_request(self, request, spider):
        # 通过配置PROXIES_LIST, 设置随机IP
        # request.meta["proxy"] = random.choices(PROXIES_LIST)

        # 通过代理池, 配置随机IP ==>写一个Flask项目, 指定一个URL随机返回IP地址, 然后使用request访问这个URL, 获取text内容
        # IP = request.get("127.0.0.1:6868").text
        # request.meta["proxy"] = IP

        return None
