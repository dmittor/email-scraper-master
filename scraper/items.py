# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmailAddressItem(scrapy.Item):
    field = scrapy.Field()
    source_url = scrapy.Field()
    title = scrapy.Field()




