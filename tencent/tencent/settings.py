# 项目名
BOT_NAME = 'tencent'

# 爬虫位置
SPIDER_MODULES = ['tencent.spiders']
NEWSPIDER_MODULE = 'tencent.spiders'

# 日志级别
LOG_LEVEL = "WARNING"

# 设置默认的用户身份 ==> 自己配置改成浏览器的
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

# 是否遵循robots协议, 不让你怕, 是不是就不爬了 ==> 默认True
ROBOTSTXT_OBEY = False

# 最大连接数, 默认16, 并发请求数, 默认注释32
# CONCURRENT_REQUESTS = 5

# 下载延迟
# DOWNLOAD_DELAY = 3

# 对每个域名, 同时并发请求数
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 对每个IP, 同时并发请求数
# CONCURRENT_REQUESTS_PER_IP = 16

# 是否关闭cookie, 默认开启==>False
# COOKIES_ENABLED = False

# 是否开启远程控制
# TELNETCONSOLE_ENABLED = False

# 默认请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# 设置爬虫中间件
# SPIDER_MIDDLEWARES = {
# 'tencent.middlewares.TencentSpiderMiddleware': 543,
# }

# 设置下载中间件
# DOWNLOADER_MIDDLEWARES = {
# 'tencent.middlewares.TencentDownloaderMiddleware': 543,
# }

# 设置扩展
# EXTENSIONS = {
# 'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 设置管道
ITEM_PIPELINES = {
    # 'tencent.pipelines.TencentPipeline': 300,
    'tencent.pipelines.ZhitongPipeline': 301,
    # 'tencent.pipelines.MongodbListItemPipeline': 302,
    # 'tencent.pipelines.MongodbDetailItemPipeline': 303,
    'tencent.pipelines.MongodbZhitongItemPipeline': 304,
}

# 设置用户名和密码
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# 是否缓存请求
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache' # 本地 ==> 当前文件夹下.scrapy文件夹中的httpcache中, 下次对于相同域名, 先从缓存中提取请求
HTTPCACHE_IGNORE_HTTP_CODES = [403, 404, 500, ] # 哪些 请求状态 数不需要缓存的
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'