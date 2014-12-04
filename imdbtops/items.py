# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Movie(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rating = scrapy.Field()
    users_rated = scrapy.Field()
    duration = scrapy.Field()
    short_description = scrapy.Field()
    release_date = scrapy.Field()
    genre = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    actors = scrapy.Field()
    ranking = scrapy.Field()
    awards = scrapy.Field()