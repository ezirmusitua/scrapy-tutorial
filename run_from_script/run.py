# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess

from run_from_script import Quotes0Spider, Quotes1Spider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(Quotes0Spider)
process.crawl(Quotes1Spider)
process.start()
