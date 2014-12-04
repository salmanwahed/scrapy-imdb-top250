# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ImdbtopsPipeline(object):
    def __init__(self):
        self.file = open('imdb_top_250.json', 'wb')

    def process_item(self, item, spider):
        item['release_date'] = item['release_date'].replace('\n', ' ')
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
