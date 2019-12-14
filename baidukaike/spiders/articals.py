from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['si.ahu.edu.cn']
    start_urls = ['http://si.ahu.edu.cn/2019/1202/c9326a214597/page.htm']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]
    custom_settings = {
                          'LOG_LEVEL': 'DEBUG',
                          # 'LOG_FILE': '5688_log_%s.txt' % time.time(),
                          'DEFAULT_REQUEST_HEADERS': {
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                         }
    }

    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//p[@class="MsoNormal"]//span//text()').extract()
        if title != None:
            print('URL is: {}'.format(url))
            print('title is: {} '.format(title))
            print('text is: {}'.format(text))
        # print('Last updated: {}'.format(lastUpdated))