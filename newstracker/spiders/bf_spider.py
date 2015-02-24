import scrapy

from newstracker.items import NewstrackerItem

class BfSpider(scrapy.Spider):
    name = "bf_spider"
    allowed_domains = ["buzzfeed.com"]
    start_urls = ["http://www.buzzfeed.com/trending"]

    def parse(self, response):
        sel = scrapy.Selector(response)
        newss = sel.xpath('//ul[@class="list--numbered trending-posts trending-posts-now"]/li')
        items = []
        
        
        for news in newss:
            print news.extract()
            
            item = NewstrackerItem()
            item['title'] = news.xpath('div[@class="trending-post-text"]/a[@class="trending-post-title"]/text()').extract()
            item['url'] = news.xpath('div[@class="trending-post-text"]/a[@class="trending-post-title"]/@href').extract()
            items.append(item)

        return items
