# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmailAddressItem(scrapy.Item):
    companyName = scrapy.Field()
    contactName = scrapy.Field()
    category = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()




