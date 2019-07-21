# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://ictstartups.ir/fa/startups/list/',
    ]

    def parse(self, response):
        for quote in response.xpath('//a[@class="startupsTitleView"]'):
            yield {
                'title': quote.xpath('.//div[@class="startupsContent"]/h3/text()').extract_first(),
                'summary' : quote.xpath('.//div[@class="startupsContent"]/p/text()').extract_first(),
                # 'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                # 'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        next_page_url = response.xpath('//footer[@class="paging"]/li/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

