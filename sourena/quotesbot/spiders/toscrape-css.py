# # -*- coding: utf-8 -*-
# import scrapy


# class ToScrapeCSSSpider(scrapy.Spider):
#     name = "toscrape-css"
#     start_urls = [
#         'http://ictstartups.ir/fa/startups/list/',
#     ]

#     def parse(self, response):
#         for quote in response.css("a.startupsTitleView"):
#             yield {
#                 'title': quote.css("div.startupsContent > h3::text").extract_first(),
#                 'summary' : quote.css("div.startupsContent > p::text").extract_first(),
#                 'logo' : quote.css("div.startupsLogo > div.startupsLogoMain  ").extract_first().split("(",1)[1].split(")")[0],
#                 'detail':self.detail_parse()
#                 # 'author': quote.css("small.author::text").extract_first(),
#                 # 'tags': quote.css("div.tags > a.tag::text").extract()
#             }
    

#         next_page_url =response.css("footer.paging > ul > li >a.fa-chevron-left").attrib['href']
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))





# import scrapy
# class AuthorSpider(scrapy.Spider):
#     name = 'author'
#     start_urls = ['http://quotes.toscrape.com/']

#     def parse(self, response):
#         # follow links to author pages
#         # for href in response.css('.author + a::attr(href)'):
#         for href in response.css("div.quote > span > small.author + a::attr(href)"):
#             yield response.follow(href, self.parse_author)

#         # follow pagination links
#         for href in response.css('li.next a::attr(href)'):
#             yield response.follow(href, self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default='').strip()

#         yield {
#             'name': extract_with_css("div.author-details > h3.author-title::text"),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }
###################################################################################
# -*- coding: utf-8 -*-

import scrapy
import time

class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://ictstartups.ir/fa/startups/list/']

    def parse(self, response):
        for href in response.css("div.page >  section.container > section > a::attr(href)").getall():
            yield response.follow(href, self.parse_author)

        next_page = response.css("div.page > section.container > section > footer.paging > ul > li > a.fa-chevron-left::attr(href)").get()  
        if next_page is not None:
            time.sleep(5)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        # for href in response.css("div.page > section.container > footer.paging > ul > li > a::attr(href)"):
        #     yield response.follow(href, self.parse)
    
    # def parse_author(self, response):
    #     def extract_with_css(query):
    #         return response.css(query).get(default='').strip()

    #     yield {
    #         'site': extract_with_css("div.page > div.fullContainer > div.container > div.personalProfile > fieldset.animated > section.mui-col-md-9 > article.Specifications > div.mui-row > div.mui-col-md-6 > p.description > a::attr(href)"),
    #         #'email' : extract_with_css("div.page > div.fullContainer > div.profile > div.personalProfile > fieldset.formViewProfile > section.mui-col-md-9 > article.Specifications > div.mui-row > div.mui-col-md-6 > p.description").getall(),
    #         # 'ostan' : extract_with_css("div.page > div.fullContainer > div.container > div.personalProfile > fieldset.animated > section.mui-col-md-9 > article.Specifications > div.mui-row > div.mui-col-md-4 > span.lblEmail :: text"),
    #         # 'intro' : extract_with_css(""),
    #     }

    def parse_author(self, response):
        for quote in response.css("div.page"):
            yield { 

                'name' : quote.css("div.fullContainer > div.profile > div.personalProfile > fieldset.formViewProfile > section.mui-col-md-3 > div > h1.labelStartupsLogo::text").extract_first(),
                'MainPic' : quote.css("div.fullContainer > div.container > div.personalProfile > fieldset.formViewProfile > section.mui-col-md-3 > div.startupsLogo > div.startupsLogoMain").extract_first().split("(",1)[1].split(")")[0],
                'BackPic' : quote.css("div.fullContainer > div.container > div.personalProfile > fieldset.formViewProfile > div.startups-cover-image").extract_first().split("(",1)[1].split("\"")[0],
                'site': quote.css("div.fullContainer > div.container > div.personalProfile > fieldset.animated > section.mui-col-md-9 > article.Specifications > div.mui-row > div.mui-col-md-6 > p.description > a::attr(href)").extract_first(),
                'email' : quote.css("div.fullContainer > div.profile > div.personalProfile > fieldset.formViewProfile > section.mui-col-md-9 > article.Specifications > div.mui-row > div.mui-col-md-6 > p.description::text").extract_first().strip(),
                'region' : quote.css("div.fullContainer > div.profile > div.personalProfile > fieldset.formViewProfile > section.mui-col-md-9 > article.Specifications > div.mui-row > div.mui-col-md-4 > span::text").getall(),
                'intro' : quote.css("div.fullContainer > div.profile > div.personalProfile > fieldset.formViewProfile > section.mui-col-md-9 > article.Specifications > p.description").getall(),
                'partners' : quote.css("div.fullContainer > div.profile > fieldset.partners > div.listPartners > a.linkPicTitle > div.picTitleProfile > h4.picTitleResult::text").getall(),
        }
