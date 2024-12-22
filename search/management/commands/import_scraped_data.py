import json
from django.core.management.base import BaseCommand
from search.models import SearchResult

class Command(BaseCommand):
    help = "Import scraped data from JSON into the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for item in data:
                SearchResult.objects.update_or_create(
                    url=item['url'],
                    defaults={
                        'title': item.get('title', ''),
                        'content': item.get('content', ''),
                        'keywords': item.get('keywords', []),
                        'type': item.get('type', ''),
                    }
                )
            self.stdout.write(self.style.SUCCESS(f'Data imported successfully from {file_path}!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found at {file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f'Invalid JSON file at {file_path}'))