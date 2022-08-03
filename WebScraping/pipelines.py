# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import sqlite3


class WebscrapingPipeline:

    def __init__(self):
        pass

    # def create_connection(self):
    #     self.conn = sqlite3.connect('WebScrapingABC.db')
    #     self.curr = self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""create table blueMercuryProducts_tb(
    #                         ProductID int,
    #                         ProductName text,
    #                         Product_URL text,
    #                         Price
    #                         )""")

    def process_item(self, item, spider):
        return item
