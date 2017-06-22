# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider

from ..items import LeiPhoneNewsItem


class LeiphoneSpider(XMLFeedSpider):
    name = 'leiphone'
    allowed_domains = ['leiphone.com']
    start_urls = ['http://leiphone.com/feed']
    iterator = 'iternodes'  # you can change this; see the docs
    itertag = 'item'  # change it accordingly

    def parse_node(self, response, selector):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(selector.extract()))
        item = LeiPhoneNewsItem()
        item['title'] = selector.select('title::text').extract()
        item['link'] = selector.select('link::text').extract()
        item['description'] = selector.select('description::text').extract()
        return item
