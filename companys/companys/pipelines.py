# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class CompanysPipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='123qwe',
            database='salary',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        companyName = item['companyName']  # 企业名
        url = item['url']  # 企业链接
        jobNum = item['jobNum']  # 在招职位数量
        industry = item['industry']  # 所属行业
        place = item['place']  # 公司地点
        insert_sql = """
            insert IGNORE into company(`companyName`, `url`, `jobNum`, `industry`, `place`)
            values(%s,%s,%s,%s,%s);
        """
        self.cursor.execute(insert_sql, (companyName, url, jobNum, industry, place))
        self.conn.commit()
        return item
