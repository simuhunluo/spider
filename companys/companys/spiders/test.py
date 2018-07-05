# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/company/7514239/', 'https://www.liepin.com/company/9562527/']

    def parse(self, response):
        parse_res=response.xpath('//*[@id="company"]/div[2]/div/div/div/div[1]/p/text()').extract()
        str_empty=''
        str=str_empty.join(parse_res).strip()
        if str=='':
            print('空的')
        else:
            print("不空啊")
        print(str)