# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from ..items import QuoteItem


class QuotesSpider(CrawlSpider):
    name = 'quotes'
    url_base = 'https://quotes.toscrape.com'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    rules = (
        Rule(LinkExtractor(allow='\/$', deny='/\w+/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info('Info: %s', response.url)
        items = []
        divs = response.css('div.quote')
        for quote in divs:
            item_loader = ItemLoader(item=QuoteItem(), selector=quote)
            item_loader.add_css('author', 'small.author::text')
            item_loader.add_css('author_link', 'span:nth-child(2)>a::attr(href)')
            item_loader.add_css('text', 'span.text::text')
            item_loader.add_css('tags', 'div.tags a.tag::text')
            items.append(item_loader.load_item())
        return items
