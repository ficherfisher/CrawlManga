# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XingqiumanhuaItem(scrapy.Item):
    title = scrapy.Field()
    chapter = scrapy.Field()
    image_urls = scrapy.Field()
