import scrapy

class BarsSpider(scrapy.Spider):
    name = "bars"

    start_urls = [
        'http://www.ebaystores.com/8020-Inc-Garage-Sale/Extrusions-Fractional-T-Slot-/_i.html',
        'http://www.ebaystores.com/8020-Inc-Garage-Sale/Extrusions-Metric-T-Slot-/_i.html'
    ]

    def parse(self, response):
        for a in response.css('div.ttl').css('a'):
            item_page = response.urljoin(a.attrib['href'])
            yield scrapy.Request(item_page, callback=self.parse_item_page)

        next_page = response.css('td.next a.enabled::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item_page(self, response):
        title = response.css('h1.it-ttl::text').extract_first()
        yield {'title': title}#, 'response': response}
