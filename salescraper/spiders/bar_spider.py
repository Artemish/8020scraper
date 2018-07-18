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
        iframe_url = response.css('iframe::attr(src)').extract_first()
        if iframe_url is not None:
            next_page = response.urljoin(iframe_url)
            yield scrapy.Request(next_page, callback=self.parse_iframe_page)

    def parse_iframe_page(self, response):
        descr = response.css('table strong::text').extract_first()
        list_items = response.css('tr ul li font::text').extract()
        list_items += response.css('tr ul li::text').extract()
        only_pieces = filter(lambda i: 'pc' in i, list_items)
        if descr is not None:
            yield {'description': descr,
                   'list_items': list(only_pieces)}
