import scrapy
from bs4 import BeautifulSoup
from .utils import extract_keywords


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
        title = response.css("title::text").get()
        raw_html = response.css("div#main").get()

        soup = BeautifulSoup(raw_html, 'html.parser')
        clean_text = soup.get_text(separator=' ', strip=True)
        url = response.url

        keywords = extract_keywords(clean_text)

        yield {
            "title": title,
            "url": url,
            "content": clean_text,
            "keywords": keywords
        }
