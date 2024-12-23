# Generated by Django 5.1.4 on 2024-12-20 18:48

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_alter_searchresult_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='searchresult',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='search_sear_search__ba5371_gin'),
        ),
    ]
