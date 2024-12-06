from django.db import models

class DjangleDb(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    content = models.TextField()
