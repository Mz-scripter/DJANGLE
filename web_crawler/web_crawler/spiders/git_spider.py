import scrapy
import os
import json


class GitSpiderSpider(scrapy.Spider):
    name = "git-spider"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/search?q=django&type=repositories&p=38"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_urls = set()

        if os.path.exists('git_results.json'):
            with open('git_results.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.existing_urls = {item['url'] for item in data}

    def parse(self, response):
        # Extract repository links from the search results
        repos = response.css('div.Box-sc-g0xbh4-0.MHoGG.search-title a::attr(href)').getall()
        for repo in repos:
            full_url = response.urljoin(repo)
            if full_url in self.existing_urls:
                print("REPO ALREADY EXISTS")
                continue
            yield scrapy.Request(full_url, callback=self.parse_repo)
        
        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_repo(self, response):
        title = response.css('strong.mr-2.flex-self-stretch a::text').get() # repo name
        url = response.url
        readme = response.css('article.markdown-body').get().strip()

        yield {
            "title": title,
            "url": url,
            "content": readme
        }

