# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
import scrapy
import hashlib
from urllib.parse import quote

from scrapy.exceptions import DropItem


class RemoveLovePipeline(object):
    def process_item(self, item, spider):
        if 'love' in item['tags']:
            raise DropItem('No love we need')
        return item


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class MongoPipeline(object):
    collection_name = 'scrapy_tutorial_quotes'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'exercise')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


class ScreenShotPipeline(object):
    """Pipeline that uses Splash to render screen shot of every Scrapy item."""

    SPLASH_URL = "http://localhost:8050/render.png?url={}"

    def process_item(self, item, spider):
        encoded_item_url = quote(spider.url_base + item["author_link"])
        screen_shot_url = self.SPLASH_URL.format(encoded_item_url)
        request = scrapy.Request(screen_shot_url)
        deferred = spider.crawler.engine.download(request, spider)
        deferred.addBoth(self.return_item, item)
        return deferred

    def return_item(self, response, item):
        if response.status != 200:
            return item
        # Save screen shot to file, filename will be hash of url.
        url = item["url"]
        url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        filename = "{}.png".format(url_hash)
        with open(filename, "wb") as f:
            f.write(response.body)
        # Store filename in item.
        item["screen_shot_filename"] = filename
        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.texts_seen = set()

    def process_item(self, item, spider):
        text_hash = hashlib.md5(item['text'].encode()).hexdigest()
        if text_hash in self.texts_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            item['text_hash'] = text_hash
            self.texts_seen.add(text_hash)
            return item
