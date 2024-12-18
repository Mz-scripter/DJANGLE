from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

class DjangleDb(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'])
        ]


class SearchResult(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    content = models.TextField()
    keywords = models.JSONField(null=True, blank=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.title
