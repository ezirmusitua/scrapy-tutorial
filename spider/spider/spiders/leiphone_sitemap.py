# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import SitemapSpider

from ..items import LeiPhoneNewsItem


class LeiphoneSitemapSpider(SitemapSpider):
    name = "leiphone-sitemap"
    sitemap_urls = ['https://www.leiphone.com/sitemap.xml']
    sitemap_rules = [('/news/', 'parse_news')]
    other_urls = ['https://www.leiphone.com/']

    def start_requests(self):
        requests = list(super(LeiphoneSitemapSpider, self).start_requests())
        requests += [scrapy.Request(x, self.parse_homepage) for x in self.other_urls]
        return requests

    def parse_homepage(self, response):
        self.logger('hello, this is homepage %s', response.url)

    def parse_news(self, response):
        item = LeiPhoneNewsItem()
        item['title'] = response.css(
            'div.lphArticle-detail > div.article-template > div.article-title > div > h1::text')
        item['link'] = response.url
        item['description'] = response.css(
            'div.lphArticle-detail > div.article-template > div.article-title > div > div.article-lead::text')
        return item

