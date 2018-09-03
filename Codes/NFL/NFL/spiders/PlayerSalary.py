# -*- coding: utf-8 -*-
import scrapy

#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor

class PlayersalarySpider(scrapy.Spider):
    name = 'PlayerSalary'

    def start_requests(self):
        urls = [
            'https://www.spotrac.com/nfl/rankings/cap-hit/'
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse);

    def parse(self, response):
        for row in response.xpath('//*[@class="datatable noborder"]//tbody//tr'):
            # name = row.xpath('td//h3//a//text()')[0].extract()
            # salary = row.xpath('td//span//text()')[1].extract()
            #
            # print(name, salary)
            yield{
                'name' : row.xpath('td//h3//a//text()')[0].extract(),
                'salary' : row.xpath('td//span//text()')[1].extract()
            }
