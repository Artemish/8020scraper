import scrapy

class BarsSpider(scrapy.Spider):
    name = "bars"

    start_urls = [
        'http://www.ebaystores.com/8020-Inc-Garage-Sale/Extrusions-Fractional-T-Slot-/_i.html',
        'http://www.ebaystores.com/8020-Inc-Garage-Sale/Extrusions-Metric-T-Slot-/_i.html'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'bars-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
