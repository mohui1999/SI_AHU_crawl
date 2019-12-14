import scrapy
from urllib import request
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

class ArticalSpider(scrapy.Spider):
    name = 'artical'

    def start_requests(self):
        url = 'http://si.ahu.edu.cn'

        url_all = set()

        html = urlopen('http://si.ahu.edu.cn')
        bs = BeautifulSoup(html, 'html.parser')
        num = 0

        for x in bs.find_all('a', href=re.compile('^(/2019/)')):
            if 'href' in x.attrs:
                if x.attrs['href'] not in url_all:
                    new_url = x.attrs['href']
                    num = num + 1
                    print("第" + str(num) + "个链接：" + url + new_url)
                    url_all.add(url+new_url)

        print(url_all)
        urls = [
            'http://si.ahu.edu.cn/2019/1202/c9326a214597/page.htm',
            'http://si.ahu.edu.cn/2019/1128/c9326a214482/page.htm',
            'http://si.ahu.edu.cn/2019/1127/c9326a214341/page.htm'
        ]
        return [scrapy.Request(url=url,callback = self.parse)
            for url in url_all]

    def parse(self,response):
        url = response.url
        title = response.css('.arti_title').extract_first()
        print("链接是{}".format(url))
        print('标题是{}'.format(title))