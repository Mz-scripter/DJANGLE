from django.core.management.base import BaseCommand
from django.contrib.postgres.search import SearchVector
from search.models import SearchResult
from django.db.models.signals import post_save
from search.signals import update_search_vector


class Command(BaseCommand):
    help = "Update the search_vector field for all SearchResults records"

    def handle(self, *args, **kwargs):
        # Disconnect the signal to prevent recursion
        post_save.disconnect(update_search_vector, sender=SearchResult)

        try:
            for record in SearchResult.objects.all():
                record.search_vector = SearchVector('title', weight='A') + SearchVector('content', weight='B') + SearchVector('keywords', weight='C')
                record.save()
                self.stdout.write(f"Updated search_vector for record ID: {record.id}")

            self.stdout.write(self.style.SUCCESS("Successfully updated all search_vector fields."))
        finally:
            # Reconnect the signal after updating
            post_save.connect(update_search_vector, sender=SearchResult)