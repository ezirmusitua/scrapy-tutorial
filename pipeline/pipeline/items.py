# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader.processors import Join, TakeFirst


def strip_input(values):
    return map(lambda x: str.strip(x), values)


class QuoteItem(scrapy.Item):
    author = scrapy.Field(
        input_processor=strip_input,
        output_processor=TakeFirst()
    )
    author_link = scrapy.Field(
        output_processor=TakeFirst()
    )
    text = scrapy.Field(
        input_processor=strip_input,
        output_processor=Join()
    )
    tags = scrapy.Field()
    screen_shot_filename = scrapy.Field()
