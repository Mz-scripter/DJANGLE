import scrapy


class StackspiderSpider(scrapy.Spider):
    name = "stackspider"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions/tagged/django"]

    def parse(self, response):
        questions = response.css('div.s-post-summary')
        for question in questions:
            title = question.css('a.s-link::text').get().strip()
            url = question.css('a.s-link::attr(href)').get()
            full_url = f"https://stackoverflow.com{url}" if url else None

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
        content = response.css('div.postcell div.s-prose').get()

        yield {
            'Question Title': title,
            'Question URL': url,
            'Question Content': content.strip() if content else None,
        }