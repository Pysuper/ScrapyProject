import os

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'

LOG_LEVEL = 'WARNING'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 0.1
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# COOKIES_ENABLED = False

# TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Referer': 'https://www.mzitu.com',
    'Upgrade-Insecure-Requests': 1,
}

# 爬虫中间件
# SPIDER_MIDDLEWARES = {
#    'meizitu.middlewares.MeizituSpiderMiddleware': 543,
# }

# 下载中间件
# DOWNLOADER_MIDDLEWARES = {
#    'meizitu.middlewares.MeizituDownloaderMiddleware': 543,
# }

# 扩展
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 管道
ITEM_PIPELINES = {
    'meizitu.pipelines.MeizituPipeline': 300,
    # 'meizitu.pipelines.SaveImagePipeline': 301,
    # 'meizitu.pipelines.MongoDBPipeline': 302,
    'meizitu.pipelines.CrawlSaveImagePipeline': 301,
    'meizitu.pipelines.CrawlMongoDBPipeline': 302,
}

# 用户名和密码
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# 本地缓存请求
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IMAGES_STORE = os.path.join(os.path.dirname(__file__), 'images')
