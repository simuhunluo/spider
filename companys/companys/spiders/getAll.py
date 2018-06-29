# -*- coding: utf-8 -*-
import scrapy


class GetallSpider(scrapy.Spider):
    name = 'getAll'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/citylist/?target=company']

    def parse(self, response):
        node_list = response.xpath('//*[@id="bd"]/div/div[2]/ol/li[*]')
        for node in node_list:
            urls = node.xpath('./p/span[2]/a')
            for url in urls:
                ab_url = "'https://www.liepin.com"+url.xpath('./@href').extract()[0]+"',"
                print(ab_url)
