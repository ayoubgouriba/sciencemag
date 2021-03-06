from urllib import response
from urllib.request import Request

import scrapy
from scrapy import item
from scrapy.selector import Selector
from ..items import SciencemagItem


class ScienceMagSpider(scrapy.Spider):
    name = "sciencemag"
    allowed_domains = ['sciencemag.org']
    start_urls = ["https://www.sciencemag.org/"]

    def parse(self, response):
        item = SciencemagItem()

        title = Selector(response).xpath('//h2[@class="media__headline"]/a/text()').getall()
        author = Selector(response).xpath('//p[@class="byline"]/a/text()').getall()
        date = Selector(response).xpath('//p[@class="byline"]/time/text()').getall()
        url = Selector(response).xpath('//h2[@class="media__headline"]/a/@href').getall()

        item['title'] = title
        item['author'] = author
        item['date'] = date
        item['url'] = url

        yield item
