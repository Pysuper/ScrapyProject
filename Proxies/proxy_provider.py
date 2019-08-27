import json
from flask import Flask, request
from redis_proxy_pool import RedisProxyPool


class ProxyProvider(object):
    """
    写的一个Flask的页面，直接访问，返回IP ==> http://0.0.0.0:6868/proxies/random
    """

    def __init__(self):
        self.app = Flask(__name__)
        self.proxyPool = RedisProxyPool()

        @self.app.route('/proxies')
        def all():
            return json.dumps(self.proxyPool.all())

        @self.app.route('/proxies/random')
        def random():
            return self.proxyPool.random()

        @self.app.route('/proxies/remove', methods=['GET'])
        def removeProxy():
            self.proxyPool.decrease(request.args.get('proxy'))

    def run(self):
        self.app.run(host="0.0.0.0", port=6868)


if __name__ == '__main__':
    proxyProvider = ProxyProvider()
    proxyProvider.run()
