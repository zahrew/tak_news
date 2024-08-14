import scrapy
from news_scraper.items import NewsScraperItem

class ZoomitSpider(scrapy.Spider):
    name = "zoomit"
    allowed_domains = ["zoomit.ir"]
    start_urls = ["https://www.zoomit.ir/live-news/"]

    def parse(self, response):
        for article in response.css('article'):
            item = NewsScraperItem()
            item['title'] = article.css('h2 a::text').get()
            item['content'] = article.css('p::text').get()
            item['source'] = article.css('h2 a::attr(href)').get()
            item['tags'] = article.css('.tag a::text').getall()
            yield item
