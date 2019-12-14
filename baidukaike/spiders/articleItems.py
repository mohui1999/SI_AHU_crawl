from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from baidukaike.items import Article

class ArticleSpider(CrawlSpider):
    name = 'articleItems'
    allowed_domains = ['si.ahu.edu.cn']
    start_urls = ['http://si.ahu.edu.cn/2019/1202/c9326a214597/page.htm']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//p[@class="MsoNormal"]//span//text()').extract()
        return article