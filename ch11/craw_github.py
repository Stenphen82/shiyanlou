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
            item = ShiyanlougithubItem({
                'name': repo.css('li.col-12 div.d-inline-block a::text').re_first("\n\s* (.+)"),
                'update_time': repo.css('li.col-12 div.f6 relative-time::attr(datetime)').extract_first()
                                                                                                    })
            yield item
