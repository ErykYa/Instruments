# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class InstrumentsPipeline(object):

    def open_spider(self, spider):
        hostname = '127.0.0.1'
        username = 'instruments'
        password = 'mn12lk54pgf521'
        database = 'instruments'
        self.connection = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()


    def process_item(self, item, spider):
        nulldict = {'price': 0}
        self.cur.execute(
            'INSERT INTO catalog_catalog(title, code, vendor_code, brand, availability, price, img_url)'
            ' VALUES(%s,%s,%s,%s,%s,%s,%s)'
            'ON CONFLICT (code) DO NOTHING',
            (list(item['title'])[0],
             list(item['code'])[0],
             list(item['vendor_code'])[0],
             list(item['brand'])[0],
             list(item['availability'])[0],
             list(item['price'])[0] if len(item['price']) != 0 else nulldict['price'],
             list(item['img_url'])[0]
             )
            )
        self.connection.commit()
        self.cur.execute(
            'UPDATE catalog_catalog SET price = (%s), availability = (%s) WHERE code = (%s)',
            (list(item['price'])[0] if len(item['price']) != 0 else nulldict['price'],
             list(item['availability'])[0],
             list(item['code'])[0],
             )
        )
        self.connection.commit()
        return item
