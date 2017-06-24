# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader.processors import Join, TakeFirst


def stripInput(vals):
    return map(lambda x: str.strip(x), vals)


class QuoteItem(scrapy.Item):
    author = scrapy.Field(
        input_processor=stripInput,
        out_processor=TakeFirst()
    )
    text = scrapy.Field(
        input_processor=stripInput,
        output_processor=Join()
    )
    tags = scrapy.Field()
