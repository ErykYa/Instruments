from scrapy.spiders import Spider
import time
from ..items import InstrumentsItem


class InstrSpider(Spider):
    name = 'instr_spider'
    start_urls = [
        'https://th-tool.by/index.php?route=product/category&path=3173&path=3173&filter_categories[0]=3221&filter_categories[1]=3285&filter_categories[2]=3198&filter_categories[3]=3275&filter_categories[4]=3202&filter_categories[5]=3176&filter_categories[6]=3174&filter_categories[7]=3223&filter_manufactures[0]=153&filter_manufactures[1]=173&filter_manufactures[2]=136&filter_manufactures[3]=138&sort=p.sort_order&order=ASC&limit=600&page=1']

    def parse(self, response):
        for i in range(1, 16):
            next_page = f'https://th-tool.by/index.php?route=product/category&path=3173&path=3173&filter_categories[0]=3221&filter_categories[1]=3285&filter_categories[2]=3198&filter_categories[3]=3275&filter_categories[4]=3202&filter_categories[5]=3176&filter_categories[6]=3174&filter_categories[7]=3223&filter_manufactures[0]=153&filter_manufactures[1]=173&filter_manufactures[2]=136&filter_manufactures[3]=138&sort=p.sort_order&order=ASC&limit=600&page={i}'
            yield response.follow(next_page, callback=self.parse_item)
            # time.sleep(5)

    def parse_item(self, response):
        for instruments in response.css('div.product-layout.product-list.col-xs-12'):
            title = instruments.css('div.caption.product-info.clearfix h4 a span::text').extract()
            code = instruments.css('div.description span.dotted-line_right::text').extract()[0::4]
            vendor_code = instruments.css('div.description span.dotted-line_right::text').extract()[1::4]
            brand = instruments.css('div.description span.dotted-line_right::text').extract()[2::4]
            availability = instruments.css('div.description span.dotted-line_right::text').extract()[3::4]
            price = [i.replace(' р.', '') for i in instruments.css('div.price span::text').extract()]
            img_url = instruments.css('div.image a img.img-responsive::attr(src)').extract()
            instrumentsItem = InstrumentsItem(title=title,
                                              code=code,
                                              vendor_code=vendor_code,
                                              brand=brand,
                                              availability=availability,
                                              price=price,
                                              img_url=img_url,
                                              )
            yield instrumentsItem
