import scrapy


class DjIndexSpider(scrapy.Spider):
    name = "dj-index"
    start_urls = ["https://docs.djangoproject.com/en/5.1/genindex/"]

    def parse(self, response):
        links = response.css('dl[class="index"] a::attr(href)').getall()

        for link in links:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_page)
    
    def parse_page(self, response):
        title = response.css('h1::text').get()
        url = response.url
        content = response.css('#docs-content').get().strip()

        yield {
            "title": title,
            "url": url,
            "content": content
        }
