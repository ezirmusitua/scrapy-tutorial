# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import string

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class QuoteLoader(scrapy.ItemLoader):
    default_out_processor = TakeFirst()
    text_in = MapCompose(str.strip, string.capwords)
    text_out = Join()

    author_in = str.strip
    author_out = Join()

    tags_in = MapCompose(str.strip, string.capwords)
    tags_out = Join()
