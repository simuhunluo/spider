# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanysItem(scrapy.Item):
    companyName = scrapy.Field()    # 企业名
    url = scrapy.Field()            # 企业链接
    jobNum = scrapy.Field()         # 在招职位数量
    industry = scrapy.Field()       # 所属行业
    place = scrapy.Field()          # 公司地点