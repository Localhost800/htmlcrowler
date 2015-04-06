# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Iteam, Field


class HtmlCrowle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
    desc=scrapy.Field()
    author=Field()
    tag=Field()
    date=Field()

