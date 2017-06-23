# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import string

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


def stripInput(vals):
    return map(lambda x: str.strip(x), vals)


def capInput(vals):
    return map(lambda x: string.capwords(x), vals)


class QuoteItem(scrapy.Item):
    text = scrapy.Field(
        input_processor=MapCompose(stripInput, capInput),
        output_processor=Join()
    )
    author = scrapy.Field(
        input_processor=stripInput,
        out_processor=Join()
    )
    tags = scrapy.Field(
        input_processor=MapCompose(stripInput, capInput),
        output_processor=Join()
    )


class QuoteLoader(ItemLoader):
    default_out_processor = TakeFirst()
    text_in = MapCompose(stripInput, capInput)
    text_out = Join()

    author_in = stripInput
    author_out = Join()

    tags_in = MapCompose(stripInput, capInput)
    tags_out = Join()
