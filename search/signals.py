from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector
from .models import DjangleDb

@receiver(post_save, sender=DjangleDb)
def update_search_vector(sender, instance, **kwargs):
    from django.db import connection
    if connection.vendor == 'postgresql' and not kwargs.get('raw', False):
        vector = SearchVector('title', weight='A') + SearchVector('content', weight='B')
        if instance.search_vector != vector:
            instance.search_vector = vector
            instance.save()