import scrapy

class BarsSpider(scrapy.Spider):
    name = "bars"

    start_urls = [
        'http://www.ebaystores.com/8020-Inc-Garage-Sale/Extrusions-Fractional-T-Slot-/_i.html',
        'http://www.ebaystores.com/8020-Inc-Garage-Sale/Extrusions-Metric-T-Slot-/_i.html'
    ]

    def parse(self, response):
        for a in response.css('div.ttl').css('a'):
            yield {
                    'title': a.attrib['title'],
                    'link': a.attrib['href']
            }
