import json
from django.core.management.base import BaseCommand
from search.models import DjangleDb

class Command(BaseCommand):
    help = "Import scraped data from JSON into the database"

    def handle(self, *args, **options):
        with open('C:/Users/HP/Documents/GitHub/DJANGLE/web_crawler/stack_django.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            DjangleDb.objects.get_or_create(
                url=item['Question URL'],
                defaults={
                    'title': item['Question Title'],
                    'content': item.get('Question Content', ''),
                }
            )
        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))