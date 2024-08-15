import scrapy
from news_scraper.items import NewsScraperItem

class ZoomitSpider(scrapy.Spider):
    name = "zoomit"
    allowed_domains = ["zoomit.ir"]
    start_urls = ["https://www.zoomit.ir/live-news"]

    def parse(self, response):
        for div in response.css('div.jjitSH'):
            item = NewsScraperItem()
            for link in div.css('a'):
                item['content'] = link.css('p::text').get()
                for titleDiv in link.css('div.iGnhay'):
                    item['title'] = titleDiv.css('span::text').get()
                    yield item
