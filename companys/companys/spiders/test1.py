# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['liepin.com']
    # start_urls = ['https://www.liepin.com/company/150060-000/',
    #               'https://www.liepin.com/company/080030-000/',
    #               'https://www.liepin.com/company/210030-000/',
    #               'https://www.liepin.com/company/120050-000/',
    #               'https://www.liepin.com/company/010-000/',
    #               'https://www.liepin.com/company/220030-000/',
    #               'https://www.liepin.com/company/080040-000/',
    #               'https://www.liepin.com/company/110030-000/',
    #               'https://www.liepin.com/company/270030-000/',
    #               'https://www.liepin.com/company/140030-000/',
    #               'https://www.liepin.com/company/210070-000/',
    #               'https://www.liepin.com/company/250150-000/',
    #               'https://www.liepin.com/company/280180-000/',
    #               'https://www.liepin.com/company/310070-000/',
    #               'https://www.liepin.com/company/120060-000/',
    #               'https://www.liepin.com/company/110110-000/',
    #               'https://www.liepin.com/company/040-000/',
    #               'https://www.liepin.com/company/060040-000/',
    #               'https://www.liepin.com/company/280020-000/',
    #               'https://www.liepin.com/company/140110-000/',
    #               'https://www.liepin.com/company/190020-000/',
    #               'https://www.liepin.com/company/180040-000/',
    #               'https://www.liepin.com/company/180020-000/',
    #               'https://www.liepin.com/company/180080-000/',
    #               'https://www.liepin.com/company/140040-000/',
    #               'https://www.liepin.com/company/060030-000/',
    #               'https://www.liepin.com/company/180050-000/',
    #               'https://www.liepin.com/company/260060-000/',
    #               'https://www.liepin.com/company/210150-000/',
    #               'https://www.liepin.com/company/220040-000/',
    #               'https://www.liepin.com/company/310150-000/',
    #               'https://www.liepin.com/company/050030-000/',
    #               'https://www.liepin.com/company/080160-000/',
    #               'https://www.liepin.com/company/080180-000/',
    #               'https://www.liepin.com/company/210040-000/',
    #               'https://www.liepin.com/company/160030-000/',
    #               'https://www.liepin.com/company/250030-000/',
    #               'https://www.liepin.com/company/260030-000/',
    #               'https://www.liepin.com/company/050040-000/',
    #               'https://www.liepin.com/company/250040-000/',
    #               'https://www.liepin.com/company/280100-000/',
    #               'https://www.liepin.com/company/280160-000/',
    #               'https://www.liepin.com/company/060200-000/',
    #               'https://www.liepin.com/company/220050-000/',
    #               'https://www.liepin.com/company/170100-000/',
    #               'https://www.liepin.com/company/170180-000/',
    #               'https://www.liepin.com/company/050050-000/',
    #               'https://www.liepin.com/company/090020-000/',
    #               'https://www.liepin.com/company/210110-000/',
    #               'https://www.liepin.com/company/210060-000/',
    #               'https://www.liepin.com/company/090-000/',
    #               'https://www.liepin.com/company/110100-000/',
    #               'https://www.liepin.com/company/050020-000/',
    #               'https://www.liepin.com/company/110040-000/',
    #               'https://www.liepin.com/company/120020-000/',
    #               'https://www.liepin.com/company/200040-000/',
    #               'https://www.liepin.com/company/280150-000/',
    #               'https://www.liepin.com/company/280110-000/',
    #               'https://www.liepin.com/company/100-000/',
    #               'https://www.liepin.com/company/050-000/',
    #               'https://www.liepin.com/company/110-000/',
    #               'https://www.liepin.com/company/120-000/',
    #               'https://www.liepin.com/company/110150-000/',
    #               'https://www.liepin.com/company/070020-000/',
    #               'https://www.liepin.com/company/080020-000/',
    #               'https://www.liepin.com/company/130-000/',
    #               'https://www.liepin.com/company/140-000/',
    #               'https://www.liepin.com/company/140120-000/',
    #               'https://www.liepin.com/company/150-000/',
    #               'https://www.liepin.com/company/160020-000/',
    #               'https://www.liepin.com/company/150140-000/',
    #               'https://www.liepin.com/company/070080-000/',
    #               'https://www.liepin.com/company/130020-000/',
    #               'https://www.liepin.com/company/220020-000/',
    #               'https://www.liepin.com/company/140050-000/',
    #               'https://www.liepin.com/company/060140-000/',
    #               'https://www.liepin.com/company/180060-000/',
    #               'https://www.liepin.com/company/050060-000/',
    #               'https://www.liepin.com/company/160-000/',
    #               'https://www.liepin.com/company/170110-000/',
    #               'https://www.liepin.com/company/180-000/',
    #               'https://www.liepin.com/company/180140-000/',
    #               'https://www.liepin.com/company/170090-000/',
    #               'https://www.liepin.com/company/210050-000/',
    #               'https://www.liepin.com/company/250170-000/',
    #               'https://www.liepin.com/company/250200-000/',
    #               'https://www.liepin.com/company/270070-000/',
    #               'https://www.liepin.com/company/320-000/',
    #               'https://www.liepin.com/company/050210-000/',
    #               'https://www.liepin.com/company/170-000/',
    #               'https://www.liepin.com/company/160080-000/',
    #               'https://www.liepin.com/company/150090-000/',
    #               'https://www.liepin.com/company/160070-000/',
    #               'https://www.liepin.com/company/250020-000/',
    #               'https://www.liepin.com/company/200030-000/',
    #               'https://www.liepin.com/company/070090-000/',
    #               'https://www.liepin.com/company/050220-000/',
    #               'https://www.liepin.com/company/170080-000/',
    #               'https://www.liepin.com/company/190-000/',
    #               'https://www.liepin.com/company/200090-000/',
    #               'https://www.liepin.com/company/250050-000/',
    #               'https://www.liepin.com/company/070060-000/',
    #               'https://www.liepin.com/company/050150-000/',
    #               'https://www.liepin.com/company/150190-000/',
    #               'https://www.liepin.com/company/160040-000/',
    #               'https://www.liepin.com/company/200-000/',
    #               'https://www.liepin.com/company/260100-000/',
    #               'https://www.liepin.com/company/260080-000/',
    #               'https://www.liepin.com/company/060-000/',
    #               'https://www.liepin.com/company/060190-000/',
    #               'https://www.liepin.com/company/090130-000/',
    #               'https://www.liepin.com/company/310020-000/',
    #               'https://www.liepin.com/company/150030-000/',
    #               'https://www.liepin.com/company/060050-000/',
    #               'https://www.liepin.com/company/050240-000/',
    #               'https://www.liepin.com/company/150040-000/',
    #               'https://www.liepin.com/company/110050-000/',
    #               'https://www.liepin.com/company/150120-000/',
    #               'https://www.liepin.com/company/140060-000/',
    #               'https://www.liepin.com/company/250160-000/',
    #               'https://www.liepin.com/company/250060-000/',
    #               'https://www.liepin.com/company/060060-000/',
    #               'https://www.liepin.com/company/100020-000/',
    #               'https://www.liepin.com/company/210-000/',
    #               'https://www.liepin.com/company/210120-000/',
    #               'https://www.liepin.com/company/250180-000/',
    #               'https://www.liepin.com/company/260120-000/',
    #               'https://www.liepin.com/company/280040-000/',
    #               'https://www.liepin.com/company/280030-000/',
    #               'https://www.liepin.com/company/290020-000/',
    #               'https://www.liepin.com/company/310040-000/',
    #               'https://www.liepin.com/company/060210-000/',
    #               'https://www.liepin.com/company/090090-000/',
    #               'https://www.liepin.com/company/110090-000/',
    #               'https://www.liepin.com/company/120040-000/',
    #               'https://www.liepin.com/company/080070-000/',
    #               'https://www.liepin.com/company/050180-000/',
    #               'https://www.liepin.com/company/160050-000/',
    #               'https://www.liepin.com/company/280050-000/',
    #               'https://www.liepin.com/company/280140-000/',
    #               'https://www.liepin.com/company/050190-000/',
    #               'https://www.liepin.com/company/060020-000/',
    #               'https://www.liepin.com/company/060070-000/',
    #               'https://www.liepin.com/company/200020-000/',
    #               'https://www.liepin.com/company/150170-000/',
    #               'https://www.liepin.com/company/070030-000/',
    #               'https://www.liepin.com/company/110020-000/',
    #               'https://www.liepin.com/company/220-000/',
    #               'https://www.liepin.com/company/230-000/',
    #               'https://www.liepin.com/company/280130-000/',
    #               'https://www.liepin.com/company/280060-000/',
    #               'https://www.liepin.com/company/090080-000/',
    #               'https://www.liepin.com/company/090100-000/',
    #               'https://www.liepin.com/company/150070-000/',
    #               'https://www.liepin.com/company/150100-000/',
    #               'https://www.liepin.com/company/200100-000/',
    #               'https://www.liepin.com/company/280090-000/',
    #               'https://www.liepin.com/company/090060-000/',
    #               'https://www.liepin.com/company/090030-000/',
    #               'https://www.liepin.com/company/250070-000/',
    #               'https://www.liepin.com/company/140070-000/',
    #               'https://www.liepin.com/company/160060-000/',
    #               'https://www.liepin.com/company/070100-000/',
    #               'https://www.liepin.com/company/240-000/',
    #               'https://www.liepin.com/company/050070-000/',
    #               'https://www.liepin.com/company/100130-000/',
    #               'https://www.liepin.com/company/110120-000/',
    #               'https://www.liepin.com/company/250080-000/',
    #               'https://www.liepin.com/company/020-000/',
    #               'https://www.liepin.com/company/050090-000/',
    #               'https://www.liepin.com/company/130030-000/',
    #               'https://www.liepin.com/company/060080-000/',
    #               'https://www.liepin.com/company/150050-000/',
    #               'https://www.liepin.com/company/150130-000/',
    #               'https://www.liepin.com/company/140020-000/',
    #               'https://www.liepin.com/company/210020-000/',
    #               'https://www.liepin.com/company/070050-000/',
    #               'https://www.liepin.com/company/050080-000/',
    #               'https://www.liepin.com/company/170030-000/',
    #               'https://www.liepin.com/company/160130-000/',
    #               'https://www.liepin.com/company/170140-000/',
    #               'https://www.liepin.com/company/180100-000/',
    #               'https://www.liepin.com/company/250-000/',
    #               'https://www.liepin.com/company/260-000/',
    #               'https://www.liepin.com/company/260090-000/',
    #               'https://www.liepin.com/company/270-000/',
    #               'https://www.liepin.com/company/280-000/',
    #               'https://www.liepin.com/company/050170-000/',
    #               'https://www.liepin.com/company/050200-000/',
    #               'https://www.liepin.com/company/060170-000/',
    #               'https://www.liepin.com/company/090070-000/',
    #               'https://www.liepin.com/company/030-000/',
    #               'https://www.liepin.com/company/140080-000/',
    #               'https://www.liepin.com/company/260020-000/',
    #               'https://www.liepin.com/company/070070-000/',
    #               'https://www.liepin.com/company/060160-000/',
    #               'https://www.liepin.com/company/250090-000/',
    #               'https://www.liepin.com/company/210140-000/',
    #               'https://www.liepin.com/company/220070-000/',
    #               'https://www.liepin.com/company/270050-000/',
    #               'https://www.liepin.com/company/100070-000/',
    #               'https://www.liepin.com/company/060090-000/',
    #               'https://www.liepin.com/company/120070-000/',
    #               'https://www.liepin.com/company/070040-000/',
    #               'https://www.liepin.com/company/060100-000/',
    #               'https://www.liepin.com/company/080050-000/',
    #               'https://www.liepin.com/company/170020-000/',
    #               'https://www.liepin.com/company/300020-000/',
    #               'https://www.liepin.com/company/250100-000/',
    #               'https://www.liepin.com/company/250110-000/',
    #               'https://www.liepin.com/company/220100-000/',
    #               'https://www.liepin.com/company/230040-000/',
    #               'https://www.liepin.com/company/310120-000/',
    #               'https://www.liepin.com/company/270060-000/',
    #               'https://www.liepin.com/company/100090-000/',
    #               'https://www.liepin.com/company/110070-000/',
    #               'https://www.liepin.com/company/090040-000/',
    #               'https://www.liepin.com/company/150110-000/',
    #               'https://www.liepin.com/company/150180-000/',
    #               'https://www.liepin.com/company/150080-000/',
    #               'https://www.liepin.com/company/140100-000/',
    #               'https://www.liepin.com/company/270020-000/',
    #               'https://www.liepin.com/company/060110-000/',
    #               'https://www.liepin.com/company/310030-000/',
    #               'https://www.liepin.com/company/240020-000/',
    #               'https://www.liepin.com/company/180030-000/',
    #               'https://www.liepin.com/company/170040-000/',
    #               'https://www.liepin.com/company/170130-000/',
    #               'https://www.liepin.com/company/170120-000/',
    #               'https://www.liepin.com/company/180150-000/',
    #               'https://www.liepin.com/company/200110-000/',
    #               'https://www.liepin.com/company/260110-000/',
    #               'https://www.liepin.com/company/300-000/',
    #               'https://www.liepin.com/company/310130-000/',
    #               'https://www.liepin.com/company/080170-000/',
    #               'https://www.liepin.com/company/060120-000/',
    #               'https://www.liepin.com/company/060150-000/',
    #               'https://www.liepin.com/company/180090-000/',
    #               'https://www.liepin.com/company/250120-000/',
    #               'https://www.liepin.com/company/170050-000/',
    #               'https://www.liepin.com/company/230020-000/',
    #               'https://www.liepin.com/company/210100-000/',
    #               'https://www.liepin.com/company/180070-000/',
    #               'https://www.liepin.com/company/200050-000/',
    #               'https://www.liepin.com/company/260070-000/',
    #               'https://www.liepin.com/company/270100-000/',
    #               'https://www.liepin.com/company/280170-000/',
    #               'https://www.liepin.com/company/270110-000/',
    #               'https://www.liepin.com/company/310-000/',
    #               'https://www.liepin.com/company/310050-000/',
    #               'https://www.liepin.com/company/050230-000/',
    #               'https://www.liepin.com/company/050160-000/',
    #               'https://www.liepin.com/company/060230-000/',
    #               'https://www.liepin.com/company/110060-000/',
    #               'https://www.liepin.com/company/150020-000/',
    #               'https://www.liepin.com/company/090050-000/',
    #               'https://www.liepin.com/company/140090-000/',
    #               'https://www.liepin.com/company/150160-000/',
    #               'https://www.liepin.com/company/150150-000/',
    #               'https://www.liepin.com/company/050110-000/',
    #               'https://www.liepin.com/company/250130-000/',
    #               'https://www.liepin.com/company/120030-000/',
    #               'https://www.liepin.com/company/280080-000/',
    #               'https://www.liepin.com/company/050140-000/',
    #               'https://www.liepin.com/company/060130-000/',
    #               'https://www.liepin.com/company/050120-000/',
    #               'https://www.liepin.com/company/050130-000/',
    #               'https://www.liepin.com/company/180110-000/',
    #               'https://www.liepin.com/company/250140-000/',
    #               'https://www.liepin.com/company/280190-000/',
    #               'https://www.liepin.com/company/310080-000/',
    #               'https://www.liepin.com/company/060180-000/',
    #               'https://www.liepin.com/company/100080-000/',
    #               ]

    start_urls = ['https://www.liepin.com/company/150060-000/',
                  'https://www.liepin.com/company/080030-000/',
                  'https://www.liepin.com/company/210030-000/',
                  'https://www.liepin.com/company/120050-000/',
                  'https://www.liepin.com/company/010-000/',
                  'https://www.liepin.com/company/220030-000/',
                  'https://www.liepin.com/company/060050-000/'
                  ]

    def parse(self, response):
        # TODO 需要爬取对应城市的 指定行业类型 指定企业性质 因为北京分页太大
        # TODO 需要爬取企业描述，比如360，搜奇虎可能会搜不到。可以使用百度的文章标签分类API，对企业描述进行分类。
        #   比如说给360贴上 奇虎360 等标签，可以被搜索到。
        if not response.xpath('//*[@id="region"]/div[1]/div[4]/div'):
            #  该城市较小，没有分页信息，可以直接去解析抓取
            print("空的")
        else:
            if response.xpath('//*[@id="region"]/div[1]/div[4]/div/span[2]/text()').extract()[0] != "共100页":
                #  城市规模一般，分页不到100。获取到页数n，循环n次，每一页进行解析抓取
                print("城市规模一般，分页不到100"
                      + response.xpath('//*[@id="region"]/div[1]/div[4]/div/span[2]/text()').extract()[0])
            else:
                # 是大城市，分页超过100
                print("是大城市，分页超过100")
                cur_url = response.url[0:-4]
                # 行业：010 020 ...510
                cur_urls = []
                for i in range(10, 510, 10):
                    if len(str(i)) == 2:
                        cur_urls.append(cur_url+"0" + str(i))
                    else:
                        cur_urls.append(cur_url+str(i))
                # 企业性质：010 020 。。。 070 999
                kind_codes = ["010", "020", "030", "040", "050", "060", "070", "999"]
                final_urls = []
                for i in cur_urls:
                    for j in kind_codes:
                        final_urls.append(i + "-" + j + "/")

                for i in final_urls:
                    print(i)
                    # 对final_urls中的每个url进行解析抓取
