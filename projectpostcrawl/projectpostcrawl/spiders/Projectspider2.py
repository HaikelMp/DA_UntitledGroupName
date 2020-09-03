import scrapy

class projectspider2(scrapy.Spider):
    name = "crawlimg"

    start_urls = [
        'http://192.168.217.132/freebix/'
    ]

    def parse(self, response):
        css_selector = 'img'

        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

        next_page = response.css('.next a ::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)