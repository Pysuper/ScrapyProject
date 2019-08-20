BOT_NAME = 'job'

SPIDER_MODULES = ['job.spiders']
NEWSPIDER_MODULE = 'job.spiders'

LOG_LEVEL="WARNING"

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

# 是否遵循ROBOTS协议
ROBOTSTXT_OBEY = True

# 最大并发量
# CONCURRENT_REQUESTS = 32

# 延迟时间
# DOWNLOAD_DELAY = 3

# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 是否关闭Cookie
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# 默认请求头
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# 爬虫中间件
# SPIDER_MIDDLEWARES = {
#    'job.middlewares.JobSpiderMiddleware': 543,
# }

# 下载中间件
# DOWNLOADER_MIDDLEWARES = {
#    'job.middlewares.JobDownloaderMiddleware': 543,
# }

# 使用的扩展
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 管道
ITEM_PIPELINES = {
   'job.pipelines.JobPipeline': 300,
   'job.pipelines.MongodbJobItemPipeline': 301,
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
