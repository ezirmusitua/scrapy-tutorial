# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class ExampleSpider(CSVFeedSpider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/feed.csv']
    delimiter = ','
    headers = ['id', 'name', 'description', 'image_link']

    # Do any adaptations you need here
    # def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        return {
            'url': row['url'],
            'name': row['name'],
            'description': row['description'],
        }
