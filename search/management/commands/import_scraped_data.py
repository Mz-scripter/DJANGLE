import json
from django.core.management.base import BaseCommand
from search.models import SearchResult

class Command(BaseCommand):
    help = "Import scraped data from JSON into the database"

    def handle(self, *args, **options):
        with open('C:/Users/HP/Documents/GitHub/DJANGLE/web_crawler/stack_django.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            SearchResult.objects.get_or_create(
                url=item['url'],  # Use URL as a unique identifier
                    defaults={
                        'title': item.get('title', 'No Title'),
                        'content': item.get('content', ''),
                        'keywords': item.get('keywords', []),
                        'type': item.get('type', 'unknown'),
                }
            )
        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))