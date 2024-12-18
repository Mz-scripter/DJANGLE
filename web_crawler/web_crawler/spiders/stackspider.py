import scrapy
import json
import os
from bs4 import BeautifulSoup
from .utils import extract_keywords


class StackspiderSpider(scrapy.Spider):
    name = "stackspider"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions/tagged/django"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_urls = set()

        if os.path.exists('stack_django.json'):
            with open('stack_django.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.existing_urls = {item['url'] for item in data}

    def parse(self, response):
        questions = response.css('div.s-post-summary')
        for question in questions:
            title = question.css('a.s-link::text').get().strip()
            url = question.css('a.s-link::attr(href)').get()
            full_url = f"https://stackoverflow.com{url}" if url else None

            if full_url in self.existing_urls:
                print("Question already exists")
                continue

            if full_url:
                yield response.follow(
                    full_url,
                    self.parse_question,
                    meta={'title': title, 'url': full_url}
                )
        
        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page:
            next_page_url = f"https://stackoverflow.com{next_page}"
            yield response.follow(next_page_url, self.parse)
    
    def parse_question(self, response):
        title = response.meta['title']
        url = response.meta['url']

        raw_html = response.css('div.postcell div.s-prose').get()
        soup = BeautifulSoup(raw_html, 'html.parser')
        clean_content = soup.get_text(separator=' ', strip=True)

        keywords = extract_keywords(clean_content)

        yield {
            'title': title,
            'url': url,
            'content': clean_content,
            'keywords': keywords,
            'type': 'question'
        }