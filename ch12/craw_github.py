# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem
from datetime import datetime

class CrawGithubSpider(scrapy.Spider):
    name = 'craw_github'
    
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for repo in response.css('li.col-12'):
            item = ShiyanlougithubItem()

            item['name']= repo.css('li.col-12 div.d-inline-block a::text').re_first("\n\s* (.+)"),
            item['update_time']= repo.css('li.col-12 div.f6 relative-time::attr(datetime)').extract_first()
            repository_url = response.urljoin(repo.css('li.col-12 div.d-inline-block a::attr(href)').extract_first())
            request = scrapy.Request(repository_url, callback=self.parse_details)
            request.meta['item'] = item
            yield request

    def parse_details(self,response):
        item = response.meta['item']
        item['commits']=int(response.css('li.commits span::text').re_first("\n\s* (.+)").replace(',',''))
        item['branches']=int(response.xpath('//a[contains(@href,"branch")]/span/text()').re_first("\n\s* (.+)").replace(',',''))
        item['releases']=int(response.xpath('//a[contains(@href,"release")]/span/text()').re_first("\n\s* (.+)").replace(',',''))
        yield item
