# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlingAmazonProductInfoItem(scrapy.Item):
    search_keywords = scrapy.Field()
    product_asin = scrapy.Field()
    authors = scrapy.Field()
    title = scrapy.Field()
