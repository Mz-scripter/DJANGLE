import scrapy
from bs4 import BeautifulSoup
from .utils import extract_keywords


class DjDocsSpider(scrapy.Spider):
    name = "dj-docs"
    start_urls = ["https://docs.djangoproject.com/en/5.1/contents/"]

    def parse(self, response):
        links = response.css("section#s-django-documentation-contents a::attr(href)").getall()

        for link in links:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_page)
    
    def parse_page(self, response):
        title = response.css('h1::text').get()
        url = response.url
        raw_html = response.css('#docs-content').get().strip()

        soup = BeautifulSoup(raw_html, 'html.parser')
        clean_text = soup.get_text(separator=' ', strip=True)

        keywords = extract_keywords(clean_text)

        yield {
            "title": title,
            "url": url,
            "content": clean_text,
            "keywords": keywords,
            "type": "documentation"
        }
