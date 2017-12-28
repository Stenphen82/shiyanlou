import scrapy
class ShiyanlouSpider(scrapy.Spider):
    name='shiyanlou_spider'
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))


    def parse(self,response):
        for repo in response.css('li.col-12'):
            yield{
                    'name': repo.css('li.col-12 div.d-inline-block a::text').re("\n\s* (.+)"),
                    'update_time': repo.css('li.col-12 div.f6 relative-time::attr(datetime)').extract()
                    }

