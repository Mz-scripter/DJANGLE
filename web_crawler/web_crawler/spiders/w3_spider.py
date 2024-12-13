import scrapy


class W3SpiderSpider(scrapy.Spider):
    name = "w3-spider"
    allowed_domains = ["www.w3schools.com"]
    start_urls = ["https://www.w3schools.com/django/index.php"]

    def parse(self, response):
        sidebar_links= response.css("div#leftmenuinner a::attr(href)").getall()
        base_url = "https://www.w3schools.com"

        for link in sidebar_links:
            full_url = response.urljoin(link)
            yield scrapy.Request(full_url, callback=self.parse_page)
    
    def parse_page(self, response):
        title = response.css("h1::text").get()
        content = response.css("div#main").get()
        url = response.url

        yield {
            "title": title,
            "url": url,
            "content": content,
        }
