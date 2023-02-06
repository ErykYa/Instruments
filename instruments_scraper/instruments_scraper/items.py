from scrapy.item import Item, Field


class InstrumentsItem(Item):
    title = Field()
    code = Field()
    vendor_code = Field()
    brand = Field()
    availability = Field()
    price = Field()
    img_url = Field()
